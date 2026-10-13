"""In-process protocol tests. No radio, device, microphone or cloud is touched."""
import base64
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import tempfile
import threading
import unittest
import wave

from marvin.device_link import (FragmentReassembler, LinkSimulator, ProtocolError,
                               demo, fragment_message, make_message)


class SimulatedCrash(BaseException):
    pass


class LinkTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.db = self.root / "link.db"
        self.effects = []
        def record(args, cancelled):
            self.effects.append(dict(args))
            return {"ok": True, "count": len(self.effects)}
        self.simulator = LinkSimulator(self.db, {"record": record})
        self.simulator.hello([1], ["control", "status", "media:audio", "media:image"])
        self.session = self.simulator.start_session()

    def command(self, sequence=1, message_id="stable-call", **args):
        return make_message(self.session, sequence, "CONTROL", {"command": "record", "args": args}, message_id)

    def test_version_and_capabilities_must_be_negotiated(self):
        with self.assertRaises(ProtocolError):
            self.simulator.hello([2], ["control"])
        with self.assertRaises(ProtocolError):
            self.simulator.hello([True], ["control"])
        agreed = self.simulator.hello([1, 2], ["status", "flying"], 256)
        self.assertEqual(agreed["capabilities"], ["status"])
        self.assertEqual(agreed["mtu"], 256)
        self.session = self.simulator.start_session()
        with self.assertRaises(ProtocolError):
            self.simulator.receive(self.command())
        self.assertEqual(self.effects, [])

    def test_replay_after_disconnect_and_restart_does_not_repeat_effect(self):
        command = self.command(value="original")
        first = self.simulator.receive(command)
        self.assertEqual(first["state"], "completed")
        self.assertEqual(self.simulator.receive(command)["result"], first["result"])
        self.simulator.disconnect()
        self.simulator = LinkSimulator(self.db, self.simulator.handlers)
        self.simulator.hello([1], ["control"])
        self.session = self.simulator.start_session()
        with self.assertRaises(ProtocolError):
            self.simulator.receive(command)
        replay = self.simulator.receive(self.command(value="original"))
        self.assertTrue(replay["replayed"])
        self.assertEqual(replay["result"], first["result"])
        self.assertEqual(len(self.effects), 1)

    def test_reused_id_with_changed_command_is_rejected(self):
        self.simulator.receive(self.command(value=1))
        with self.assertRaisesRegex(ProtocolError, "conflitante"):
            self.simulator.receive(self.command(value=2))
        self.assertEqual(len(self.effects), 1)

    def test_old_unknown_sequence_rejected_and_new_id_allows_intended_repeat(self):
        self.simulator.receive(self.command(sequence=5))
        with self.assertRaisesRegex(ProtocolError, "Sequência antiga"):
            self.simulator.receive(self.command(sequence=4, message_id="older"))
        self.simulator.receive(self.command(sequence=6, message_id="new-call"))
        self.assertEqual(len(self.effects), 2)

    def test_concurrent_duplicate_has_one_effect(self):
        command = self.command()
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(lambda _: self.simulator.receive(command), range(8)))
        self.assertEqual(len(self.effects), 1)
        self.assertEqual(sum(not result["replayed"] for result in results), 1)

    def test_crash_after_effect_is_uncertain_after_restart_not_replayed(self):
        def crash(args, cancelled):
            self.effects.append("effect before crash")
            raise SimulatedCrash()
        self.simulator.handlers["record"] = crash
        command = self.command()
        with self.assertRaises(SimulatedCrash):
            self.simulator.receive(command)
        restarted = LinkSimulator(self.db, {"record": crash})
        restarted.hello([1], ["control"])
        session = restarted.start_session()
        retry = make_message(session, 1, "CONTROL", command["payload"], command["message_id"])
        result = restarted.receive(retry)
        self.assertEqual(result["state"], "needs_reconciliation")
        self.assertIsNone(result["result"])
        self.assertTrue(result["replayed"])
        self.assertEqual(len(self.effects), 1)

    def test_handler_error_does_not_mean_safe_to_retry(self):
        def fail(args, cancelled):
            self.effects.append("already changed")
            raise OSError("details must not be dumped into logs")
        self.simulator.handlers["record"] = fail
        result = self.simulator.receive(self.command())
        self.assertEqual(result["state"], "needs_reconciliation")
        self.assertEqual(self.simulator.receive(self.command())["state"], "needs_reconciliation")
        self.assertEqual(len(self.effects), 1)

    def test_cancel_interrupts_cooperative_handler_and_clears_media_buffers(self):
        started = threading.Event()
        def block(args, cancelled):
            started.set()
            interrupted = cancelled.wait(3)
            return {"ok": not interrupted, "interrupted": interrupted}
        self.simulator.handlers["record"] = block
        media = make_message(self.session, 10, "MEDIA_AUDIO", {"format": "pcm_s16le", "data": "A" * 4000})
        self.simulator.receive_frame(fragment_message(media)[0])
        self.assertGreater(self.simulator.fragments.buffered_bytes, 0)
        with ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(self.simulator.receive, self.command())
            self.assertTrue(started.wait(2))
            response = self.simulator.receive(make_message(self.session, 2, "CANCEL", {}))
            result = future.result(timeout=3)
        self.assertEqual(response["state"], "cancelled")
        self.assertTrue(result["result"]["interrupted"])
        self.assertEqual(self.simulator.fragments.buffered_bytes, 0)
        with self.assertRaises(ProtocolError):
            self.simulator.receive(self.command(sequence=3, message_id="after-cancel"))

    def test_file_audio_and_test_image_transfer_report_only_bytes_and_hash(self):
        audio_path = self.root / "silence.wav"
        with wave.open(str(audio_path), "wb") as audio:
            audio.setnchannels(1)
            audio.setsampwidth(2)
            audio.setframerate(16000)
            audio.writeframes(b"\x00\x00" * 160)
        image_path = self.root / "fixture.png"
        # Byte transfer fixture; neither parser nor decoder validation is claimed.
        image_path.write_bytes(b"\x89PNG\r\n\x1a\n" + b"simulated-image-bytes")
        for index, (kind, path, media_format) in enumerate((("MEDIA_AUDIO", audio_path, "wav"), ("MEDIA_IMAGE", image_path, "png")), 1):
            data = path.read_bytes()
            message = make_message(self.session, index, kind, {"format": media_format, "data": base64.b64encode(data).decode("ascii")})
            result = None
            for frame in fragment_message(message):
                result = self.simulator.receive_frame(frame) or result
            self.assertEqual(result["state"], "received")
            self.assertEqual(result["result"]["bytes"], len(data))
            self.assertEqual(result["result"]["sha256"], hashlib.sha256(data).hexdigest())
        self.assertEqual(self.effects, [])

    def test_invalid_fields_and_unregistered_commands_do_not_execute(self):
        for field, value in [("version", True), ("size", False), ("sequence", -1), ("type", []), ("message_id", "bad id")]:
            command = self.command()
            command[field] = value
            with self.subTest(field=field), self.assertRaises(ProtocolError):
                self.simulator.receive(command)
        command = make_message(self.session, 1, "CONTROL", {"command": "unregistered", "args": {}})
        with self.assertRaises(ProtocolError):
            self.simulator.receive(command)
        self.assertEqual(self.effects, [])

    def test_demo_executes_mutation_once_across_replays(self):
        result = demo()
        self.assertTrue(result["simulated"])
        self.assertEqual(result["actual_handler_calls"], 1)
        self.assertTrue(result["after_reconnect"]["replayed"])


class FragmentTests(unittest.TestCase):
    def message(self, message_id="sample", count=1000):
        return make_message("test-session", 1, "MEDIA_AUDIO", {"format": "pcm", "data": "A" * count}, message_id)

    def test_out_of_order_and_duplicate_fragments_fit_mtu(self):
        message = self.message()
        frames = fragment_message(message, 256)
        self.assertTrue(all(len(frame) <= 256 for frame in frames))
        self.assertGreater(len(frames), 1)
        reassembler = FragmentReassembler(256)
        self.assertIsNone(reassembler.feed(frames[-1]))
        self.assertIsNone(reassembler.feed(frames[-1]))
        result = None
        for frame in reversed(frames[:-1]):
            result = reassembler.feed(frame) or result
        self.assertEqual(result, message)
        self.assertEqual(reassembler.buffered_bytes, 0)

    def test_conflicting_duplicate_discards_buffer(self):
        frame = fragment_message(self.message(), 256)[0]
        reassembler = FragmentReassembler(256)
        reassembler.feed(frame)
        forged = json.loads(frame)
        forged["b"] = base64.b64encode(b"different").decode("ascii")
        with self.assertRaisesRegex(ProtocolError, "conflitante"):
            reassembler.feed(json.dumps(forged).encode())
        self.assertEqual(reassembler.buffered_bytes, 0)

    def test_buffer_limits_backpressure_and_ttl_drop_old_media(self):
        reassembler = FragmentReassembler(256, max_buffers=1, ttl_seconds=2)
        first = fragment_message(self.message("first"), 256)[0]
        second = fragment_message(self.message("second"), 256)[0]
        reassembler.feed(first, now=1)
        with self.assertRaisesRegex(ProtocolError, "Backpressure"):
            reassembler.feed(second, now=2)
        self.assertIsNone(reassembler.feed(second, now=4))
        self.assertEqual(list(reassembler.buffers), [("test-session", "second")])
        bounded = FragmentReassembler(256, max_total_bytes=1)
        with self.assertRaisesRegex(ProtocolError, "limite de bytes"):
            bounded.feed(first)
        self.assertEqual(bounded.buffered_bytes, 0)

    def test_oversized_payload_and_invalid_frame_count_rejected(self):
        with self.assertRaises(ProtocolError):
            fragment_message(self.message(count=70000))
        frame = json.loads(fragment_message(self.message())[0])
        frame["n"] = 100000
        with self.assertRaises(ProtocolError):
            FragmentReassembler().feed(json.dumps(frame).encode())
        with self.assertRaises(ProtocolError):
            FragmentReassembler(256).feed(b"x" * 257)


if __name__ == "__main__":
    unittest.main()
