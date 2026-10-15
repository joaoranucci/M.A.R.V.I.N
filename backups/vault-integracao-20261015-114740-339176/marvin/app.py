"""Tk adapter for the portable MARVIN runtime. Workers never access Tk widgets."""
from __future__ import annotations
import json
import os
from pathlib import Path
import queue
import threading
import re
import webbrowser
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

from .config import ROOT, VERSION, load_config, save_preferences, reload_gemini_config
from .brain import Brain, safe_error_detail
from .action_agent import ActionAgent, project_intent
from .workspace import ProjectWorkspace
from .self_edit import SourceEditor
from .commands import detect, normalize
from .memory import Memory
from .instance import InstanceLock
from .telemetry import EventLog
from .runtime import Runtime, TaskControl, request_text
from .visual_agent import VisualAgent, visual_intent, visual_risk
from .voice import VOICE_OPTIONS, OFFLINE_VOICE, DEFAULT_VOICE, listen, listen_wake, speak, cancel_speech, is_speaking
from .orb import Orb

BG, PANEL, ACCENT, FG, MUTED = "#0a101b", "#111c2c", "#57c7ef", "#eaf5fb", "#a1b7cb"


class MarvinApp:
    def __init__(self):
        self.data_dir = load_config()
        self.instance_lock = InstanceLock(self.data_dir)
        self.event_log = EventLog(self.data_dir / "logs")
        self.memory = Memory(self.data_dir / "marvin.db")
        self.workspace = ProjectWorkspace()
        self.source_editor = SourceEditor(ROOT)
        self.brain = Brain(self.memory)
        self.ui = queue.Queue(maxsize=256)
        self.closing = self.busy = self.visual_running = False
        self.pending = []
        self.token = TaskControl()
        self.wake_stop, self.wake_pause = threading.Event(), threading.Event()
        self.wake_thread = None
        self._workers = set()
        self.visual_agent = VisualAgent()
        self.action_agent = ActionAgent(self.brain, self.memory, self.workspace, self.source_editor,
            confirm_overwrite=self._confirm_overwrite, confirm_execution=self._confirm_execution)
        self.runtime = Runtime(self.memory, self.workspace, self.action_agent,
                               emit=self.runtime_event,
                               confirm_action=self._confirm_action)
        self.window = tk.Tk()
        self.window.title("MARVIN — " + VERSION)
        self.window.geometry("1200x850")
        self.window.minsize(1080, 760)
        self.window.configure(bg=BG)
        self.tts_enabled = tk.BooleanVar(value=os.getenv("MARVIN_SPEAK", "true").lower() == "true")
        self.wake_enabled = tk.BooleanVar(value=os.getenv("MARVIN_WAKE", "true").lower() == "true")
        self.privacy = tk.BooleanVar(value=False)
        selected = os.getenv("MARVIN_VOICE", DEFAULT_VOICE)
        self.voice_selected = tk.StringVar(value=selected if selected in VOICE_OPTIONS else OFFLINE_VOICE)
        header = tk.Frame(self.window, bg=BG)
        header.pack(fill="x", padx=20, pady=(15, 8))
        tk.Label(header, text="◈  M A R V I N", bg=BG, fg=ACCENT, font=("Segoe UI Semibold", 23)).pack(side="left")
        self.mode = tk.Label(header, text="LOCAL · API ainda não validada", bg=BG, fg=MUTED, font=("Segoe UI", 10))
        self.mode.pack(side="right")
        body = tk.Frame(self.window, bg=BG)
        body.pack(fill="both", expand=True, padx=20, pady=8)
        sidebar = tk.Frame(body, bg="#0b1524", width=260)
        sidebar.pack(side="left", fill="y", padx=(0, 14))
        sidebar.pack_propagate(False)
        tk.Label(sidebar, text="NÚCLEO MARVIN", fg=ACCENT, bg="#0b1524", font=("Segoe UI Semibold", 13)).pack(pady=(18, 0))
        self.orb = Orb(sidebar, self.activity)
        self.orb.pack(fill="x")
        self.activity_label = tk.Label(sidebar, text="Pronto para conversar", fg=FG, bg="#0b1524", wraplength=220, font=("Segoe UI", 11))
        self.activity_label.pack(padx=14, pady=8)
        tk.Label(sidebar, text="CONVERSA · MEMÓRIA · PESQUISA", fg=MUTED, bg="#0b1524", font=("Segoe UI", 8)).pack(pady=12)
        self.barge_enabled = tk.BooleanVar(value=os.getenv("MARVIN_BARGE_IN", "true").lower()=="true")
        tk.Checkbutton(sidebar, text="Interromper ao falar", variable=self.barge_enabled, command=self.persist_controls,
                       bg="#0b1524", fg=FG, selectcolor=PANEL).pack(anchor="w", padx=14)
        tk.Label(sidebar, text="Sensibilidade do microfone", fg=MUTED, bg="#0b1524").pack(anchor="w", padx=14, pady=(12,0))
        try:
            threshold = float(os.getenv("MARVIN_BARGE_THRESHOLD", "650"))
        except ValueError:
            threshold = 650
        self.barge_threshold = tk.DoubleVar(value=threshold)
        tk.Scale(sidebar, from_=150, to=4000, resolution=50, orient="horizontal", variable=self.barge_threshold,
                 command=lambda _: self.persist_barge_threshold(), bg="#0b1524", fg=MUTED,
                 highlightthickness=0, troughcolor=PANEL, length=215).pack(padx=14)
        tk.Label(sidebar, text="Valor menor detecta fala mais baixa.\nCom caixas de som, ajuste para evitar eco.",
                 wraplength=220, fg=MUTED, bg="#0b1524", font=("Segoe UI",9)).pack(padx=14,pady=8)
        self.reasoning = tk.StringVar(value=os.getenv("MARVIN_REASONING", "equilibrado"))
        tk.Label(sidebar, text="Raciocínio", fg=MUTED, bg="#0b1524").pack(anchor="w", padx=14, pady=(12,4))
        reasoning_box = ttk.Combobox(sidebar, textvariable=self.reasoning, values=("rapido", "equilibrado", "profundo"), state="readonly", width=22)
        reasoning_box.pack(padx=14)
        reasoning_box.bind("<<ComboboxSelected>>", lambda _: self.persist_controls())
        self.search_provider = tk.StringVar(value=os.getenv("MARVIN_SEARCH_PROVIDER", "google"))
        tk.Label(sidebar, text="Pesquisa com fontes", fg=MUTED, bg="#0b1524").pack(anchor="w", padx=14, pady=(12,4))
        provider_box = ttk.Combobox(sidebar, textvariable=self.search_provider, values=("google", "brave", "searxng"), state="readonly", width=22)
        provider_box.pack(padx=14)
        provider_box.bind("<<ComboboxSelected>>", lambda _: self.persist_controls())
        self.chat = scrolledtext.ScrolledText(body, bg=PANEL, fg=FG, wrap="word", state="disabled",
            font=("Segoe UI", 11), relief="flat", padx=14, pady=12)
        self.chat.pack(side="left", fill="both", expand=True)
        for tag, color in (("you", ACCENT), ("marvin", FG), ("status", MUTED)):
            self.chat.tag_config(tag, foreground=color, spacing1=8)
        input_row = tk.Frame(self.window, bg=BG)
        input_row.pack(fill="x", padx=20, pady=6)
        self.text = tk.Entry(input_row, bg=PANEL, fg=FG, insertbackground=FG, font=("Segoe UI", 12), relief="flat")
        self.text.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 8))
        self.text.bind("<Return>", lambda _: self.send())
        self.send_button = self.button(input_row, "ENVIAR", self.send)
        self.mic_button = self.button(input_row, "FALAR", self.start_listening)
        self.button(input_row, "CANCELAR", self.cancel_all, color="#e69797")
        self.button(input_row, "PAUSAR / CONTINUAR", self.toggle_pause)
        audio_row = tk.Frame(self.window, bg=BG)
        audio_row.pack(fill="x", padx=20, pady=5)
        tk.Checkbutton(audio_row, text="Responder por voz", variable=self.tts_enabled, bg=BG, fg=FG,
            selectcolor=PANEL, command=self.persist_controls).pack(side="left")
        self.voice_box = ttk.Combobox(audio_row, textvariable=self.voice_selected, values=VOICE_OPTIONS, state="readonly", width=24)
        self.voice_box.pack(side="left", padx=6)
        self.voice_box.bind("<<ComboboxSelected>>", lambda _: self.persist_controls())
        tk.Checkbutton(audio_row, text="Ativar com Marvin", variable=self.wake_enabled, bg=BG, fg=FG,
            selectcolor=PANEL, command=self.update_wake).pack(side="left")
        tk.Checkbutton(audio_row, text="Privacidade", variable=self.privacy, bg=BG, fg=FG,
            selectcolor=PANEL, command=self.toggle_privacy).pack(side="right")
        tools = tk.Frame(self.window, bg=BG)
        tools.pack(fill="x", padx=20, pady=5)
        for label, fn in (("PROJETOS", self.open_workspace), ("TAREFAS", self.show_tasks),
                ("MEMÓRIA", self.show_memory), ("LEMBRETES", self.show_reminders),
                ("DIAGNÓSTICO", self.diagnostics), ("ÁUDIO", self.audio_settings), ("REVISAR CÓDIGO", self.review_code)):
            self.button(tools, label, fn)
        tools2 = tk.Frame(self.window, bg=BG)
        tools2.pack(fill="x", padx=20, pady=3)
        self.button(tools2, "AGENTE VISUAL", self.visual_from_text)
        self.button(tools2, "TESTAR VOZ", self.test_voice)
        self.button(tools2, "TESTAR IA", self.test_google)
        self.button(tools2, "RECARREGAR IA", self.reload_ai)
        self.button(tools2, "LISTAR APPS", lambda: self.process("liste os aplicativos"))
        self.status = tk.Label(self.window, text="Pronto", bg=BG, fg=MUTED, anchor="w", wraplength=960)
        self.status.pack(fill="x", padx=20, pady=(5, 12))
        self.window.bind("<Escape>", lambda _: self.cancel_all())
        self.window.bind("<Control-space>", lambda _: self.start_listening())
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.append("marvin", "Pronto, João. Projetos, memória e tarefas ficam salvos neste computador. "
            "Use Esc para cancelar e Ctrl+Espaço para falar. Enquanto estou ocupado, você pode pedir status ou colocar outro pedido na fila.")
        if self.runtime.recovered:
            self.append("status", "Há tarefas interrompidas para revisar em TAREFAS. Nenhuma ação foi repetida automaticamente.")
        self.text.focus_set()
        self.window.after(80, self.poll_ui)
        self.window.after(500, self.update_wake)
        self.window.after(1000, self.poll_reminders)
        self.window.after(150, self.update_activity)

    def activity(self):
        if self.privacy.get():
            return "Privacidade"
        if is_speaking():
            return "Falando"
        if getattr(self, "interrupted_listening", False):
            return "Ouvindo"
        return "Pensando" if self.busy else "Pronto"

    def update_activity(self):
        if self.closing:
            return
        self.activity_label.configure(text=self.activity())
        self.window.after(150, self.update_activity)

    def persist_barge_threshold(self):
        save_preferences(self.data_dir, {"MARVIN_BARGE_THRESHOLD": self.barge_threshold.get()})

    def button(self, parent, label, fn, color=ACCENT):
        b = tk.Button(parent, text=label, command=fn, bg=PANEL, fg=color, relief="flat", padx=8, pady=6, font=("Segoe UI", 9))
        b.pack(side="left", padx=(0, 5))
        return b

    def runtime_event(self, event):
        self.event_log.record(event)
        self.post("event", event)

    def worker(self, fn, name="MARVIN-worker"):
        def guarded():
            try:
                fn()
            finally:
                self._workers.discard(threading.current_thread())
        thread = threading.Thread(target=guarded, daemon=True, name=name)
        self._workers.add(thread)
        thread.start()
        return thread

    def post(self, kind, data=None):
        if self.closing:
            return
        try:
            self.ui.put((kind, data), timeout=1)
        except queue.Full:
            # Never block workers indefinitely on diagnostics/backpressure.
            if kind in {"finish", "reply", "ask"}:
                while not self.closing:
                    try:
                        self.ui.put((kind, data), timeout=.2)
                        break
                    except queue.Full:
                        continue

    def append(self, tag, value):
        self.chat.configure(state="normal")
        self.chat.insert("end", {"you": "VOCÊ", "marvin": "MARVIN", "status": "SISTEMA"}.get(tag, tag) + "  •  ", tag)
        value = str(value)
        offset = 0
        for match in re.finditer(r"\[([^\]]+)\]\((https?://[^\s)]+)\)", value):
            self.chat.insert("end", value[offset:match.start()], tag)
            link_tag = "source_" + str(len(self.chat.tag_names()))
            self.chat.insert("end", match.group(1), (tag, link_tag))
            self.chat.tag_config(link_tag, foreground=ACCENT, underline=True)
            self.chat.tag_bind(link_tag, "<Button-1>", lambda event, url=match.group(2): webbrowser.open(url))
            offset = match.end()
        self.chat.insert("end", value[offset:] + "\n\n", tag)
        # Bound the visible transcript; history remains in SQLite.
        if int(self.chat.index("end-1c").split(".")[0]) > 2000:
            self.chat.delete("1.0", "400.0")
        self.chat.configure(state="disabled")
        self.chat.see("end")

    def poll_ui(self):
        if self.closing:
            return
        for _ in range(40):
            try:
                kind, data = self.ui.get_nowait()
            except queue.Empty:
                break
            if kind == "ask":
                title, body, event, answer, token = data
                if not token.is_set():
                    answer.append(messagebox.askyesno(title, body, parent=self.window))
                event.set()
            elif kind == "event":
                payload = data["payload"]
                if data["type"] == "task.progress":
                    self.status.configure(text=payload.get("message", ""))
                elif data["type"] == "task.finished":
                    self.append("status", "Tarefa " + data["task_id"][:8] + " · " + payload["state"])
                else:
                    self.status.configure(text=data["type"] + " · " + str(data.get("task_id") or "")[:8])
            elif kind == "status":
                self.status.configure(text=str(data)[:220])
                if str(data).startswith("Aguardando"):
                    self.interrupted_listening = False
            elif kind == "reply":
                self.append("marvin", data)
                if self.brain.active_model:
                    self.mode.configure(text="HÍBRIDO · " + self.brain.active_model + " (última chamada)")
            elif kind == "note":
                self.append("status", data)
            elif kind == "heard":
                token, text = data
                if token is not self.token:
                    continue
                self.busy = False
                if not self.token.is_set() and text:
                    self.process(text)
                else:
                    self.finish()
            elif kind == "wake_command":
                stop, text = data
                if stop is self.wake_stop and not stop.is_set() and not self.privacy.get() and self.wake_enabled.get():
                    self.interrupted_listening = False
                    self.process(text)
            elif kind == "barge":
                if data is self.wake_stop and not data.is_set() and not self.privacy.get():
                    self.interrupted_listening = True
                    self.status.configure(text="Fala interrompida · estou ouvindo você")
            elif kind == "wake_error":
                self.wake_enabled.set(False)
                self.append("status", "Ativação indisponível: " + str(data)[:350] + " Use texto ou configure ÁUDIO.")
            elif kind == "wake_active":
                self.interrupted_listening = True
                self.status.configure(text="Marvin ativado. Ouvindo seu comando…")
                self.window.bell()
            elif kind == "finish":
                self.finish()
            elif kind == "panel":
                self.panel(*data)
        self.window.after(80, self.poll_ui)

    def set_busy(self):
        self.busy = True
        self.wake_pause.set()
        self.mic_button.configure(state="disabled")

    def finish(self):
        self.busy = self.visual_running = False
        self.mic_button.configure(state="normal")
        if self.pending:
            question, task_id = self.pending.pop(0)
            self.process(question, task_id)
            return
        self.wake_pause.clear()
        self.update_wake(persist=False)
        self.status.configure(text="Pronto · texto disponível · Esc cancela")

    def persist_controls(self):
        save_preferences(self.data_dir, {"MARVIN_SPEAK": str(self.tts_enabled.get()).lower(),
            "MARVIN_WAKE": str(self.wake_enabled.get()).lower(), "MARVIN_VOICE": self.voice_selected.get(),
            "MARVIN_BARGE_IN": str(self.barge_enabled.get()).lower(),
            "MARVIN_REASONING": self.reasoning.get(), "MARVIN_SEARCH_PROVIDER": self.search_provider.get()})

    def update_wake(self, persist=True):
        if persist:
            self.persist_controls()
        if not self.wake_enabled.get() or self.privacy.get():
            self.wake_stop.set()
            return
        if self.busy or (self.wake_thread and self.wake_thread.is_alive()):
            return
        self.wake_stop, self.wake_pause = threading.Event(), threading.Event()
        stop, pause = self.wake_stop, self.wake_pause
        def worker():
            try:
                listen_wake(lambda q: self.post("wake_command", (stop, q)), lambda s: self.post("status", s), stop, pause,
                            on_wake=lambda: self.post("wake_active"), on_barge=lambda: self.post("barge", stop))
            except Exception as exc:
                if not stop.is_set():
                    self.post("wake_error", str(exc))
        self.wake_thread = self.worker(worker, name="MARVIN-wake")

    def toggle_privacy(self):
        if self.privacy.get():
            self.cancel_all()
            self.wake_stop.set()
            self.append("status", "Privacidade ativa: microfone e agente visual suspensos. Lembretes ficam no painel.")
        else:
            self.update_wake()

    def send(self):
        question = self.text.get().strip()
        if question:
            self.text.delete(0, "end")
            try:
                self.process(question)
            except Exception as exc:
                self.append("status", str(exc)[:350])

    def process(self, question, task_id=None):
        self.interrupted_listening = False
        n = normalize(request_text(question))
        if n in {"pare", "para", "cancelar", "cancele", "pare de falar", "parar"}:
            self.cancel_all()
            return
        if n in {"status", "como esta a tarefa", "qual o progresso"}:
            self.append("marvin", self.runtime.status())
            return
        if self.busy and n in {"espere", "espera", "pause", "continue", "continuar"}:
            self.runtime.resume() if n.startswith("continu") else self.runtime.pause()
            return
        if self.busy:
            if len(self.pending) >= 8:
                self.append("status", "A fila já tem 8 pedidos. Aguarde ou cancele.")
                return
            task = self.runtime.prepare(question) if task_id is None else self.runtime.tasks.get(task_id)
            self.pending.append((question, task["id"]))
            self.append("status", "Pedido na fila: " + question)
            return
        if not project_intent(question) and visual_intent(question) and os.getenv("MARVIN_VISUAL", "true").lower() == "true":
            self.run_visual(question, task_id)
            return
        task_id = task_id or self.runtime.prepare(question)["id"]
        self.token = TaskControl()
        token = self.token
        self.set_busy()
        self.append("you", question)
        should_speak, voice = self.tts_enabled.get(), self.voice_selected.get()
        def worker():
            try:
                result = self.runtime.run(question, task_id=task_id, control=token)
                self.post("reply", result["answer"])
                if should_speak and not token.is_set():
                    speak(result["answer"], voice=voice, cancel_event=token, status=lambda s: self.post("status", s))
            except Exception as exc:
                self.post("note", "Falha: " + str(exc)[:350])
            finally:
                self.post("finish")
        self.worker(worker, name="MARVIN-task")

    def cancel_all(self):
        self.interrupted_listening = False
        self.token.set()
        self.runtime.cancel()
        cancel_speech()
        self.visual_agent.cancel()
        for _, task_id in self.pending:
            self.runtime.tasks.set_state(task_id, "cancelled", "Cancelado na fila.")
        self.pending.clear()
        self.append("status", "Cancelamento solicitado. Efeitos concluídos ficam registrados; chamadas em andamento respeitam seu tempo limite.")

    def toggle_pause(self):
        if self.runtime.control:
            self.runtime.resume() if self.runtime.control.paused.is_set() else self.runtime.pause()
        else:
            self.append("status", "Pausa disponível entre etapas de tarefas. Para áudio ou agente visual, use CANCELAR.")

    def start_listening(self):
        if self.busy or self.privacy.get():
            return
        self.token = TaskControl()
        token = self.token
        self.set_busy()
        self.interrupted_listening = True
        self.wake_stop.set()
        def worker():
            try:
                if self.wake_thread:
                    self.wake_thread.join(timeout=6)
                    if self.wake_thread.is_alive():
                        raise RuntimeError("A captura anterior ainda está encerrando.")
                heard = listen(status=lambda s: self.post("status", s), cancel_event=token)
                self.post("heard", (token, heard))
            except Exception as exc:
                self.post("note", "Microfone: " + str(exc)[:450])
                self.post("finish")
        self.worker(worker, name="MARVIN-mic")

    def ask_worker(self, title, body):
        event, answer = threading.Event(), []
        token = self.token
        self.post("ask", (title, body, event, answer, token))
        for _ in range(450):
            if token.is_set() or self.closing:
                return False
            if event.wait(.2):
                return bool(answer and answer[0])
        return False

    def _confirm_overwrite(self, path):
        return self.ask_worker("Substituir arquivo", "Substituir este arquivo? Será preservado um backup.\n\n" + str(path))

    def _confirm_execution(self, details):
        return self.ask_worker("Executar verificação", "Este comando executa código do projeto com as permissões do usuário.\n\n" + json.dumps(details, ensure_ascii=False, indent=2))

    def _confirm_action(self, description):
        return self.ask_worker("Confirmar ação", description)

    def panel(self, title, content):
        window = tk.Toplevel(self.window)
        window.title("MARVIN · " + title)
        window.geometry("880x560")
        window.configure(bg=BG)
        text = scrolledtext.ScrolledText(window, bg=PANEL, fg=FG, wrap="word", font=("Consolas", 10))
        text.pack(fill="both", expand=True, padx=12, pady=12)
        text.insert("end", content)
        text.configure(state="disabled")
        return window

    def show_tasks(self):
        tasks = self.runtime.tasks.list_tasks(limit=30)
        content = []
        for task in tasks:
            content.append(json.dumps(task, ensure_ascii=False, indent=2))
            content.append(json.dumps(self.runtime.tasks.steps(task["id"]), ensure_ascii=False, indent=2))
        self.panel("Tarefas e evidências", "\n\n".join(content) or "Nenhuma tarefa.")

    def show_memory(self):
        facts = self.memory.list_facts()
        popup = self.panel("Memória", json.dumps(facts, ensure_ascii=False, indent=2))
        row = tk.Frame(popup, bg=BG)
        row.pack(fill="x", padx=12, pady=6)
        entry = tk.Entry(row, width=40)
        entry.pack(side="left")
        def remove():
            try:
                if self.busy:
                    raise RuntimeError("Aguarde a tarefa atual para editar a memória.")
                if not self.memory.delete_fact(int(entry.get())):
                    raise ValueError("ID de lembrança não encontrado.")
                popup.destroy()
                self.show_memory()
            except Exception as exc:
                messagebox.showerror("Memória", str(exc), parent=popup)
        self.button(row, "EXCLUIR ID", remove)
        replacement = tk.Entry(popup, width=80)
        replacement.pack(fill="x", padx=12, pady=5)
        def edit():
            try:
                if self.busy:
                    raise RuntimeError("Aguarde a tarefa atual para editar a memória.")
                self.memory.edit_fact(int(entry.get()), replacement.get())
                popup.destroy()
                self.show_memory()
            except Exception as exc:
                messagebox.showerror("Memória", str(exc), parent=popup)
        self.button(popup, "SUBSTITUIR TEXTO DO ID", edit)
        def export():
            path = self.data_dir / "memory-export.json"
            path.write_text(json.dumps(self.memory.export(), ensure_ascii=False, indent=2), encoding="utf-8")
            self.append("status", "Memória exportada para " + str(path))
        self.button(row, "EXPORTAR", export)
        self.button(row, "LIMPAR HISTÓRICO E FATOS", self.clear_memory)

    def show_reminders(self):
        self.panel("Lembretes", "Funcionam enquanto o MARVIN está aberto.\n\n" + json.dumps(self.runtime.scheduler.list_reminders(), ensure_ascii=False, indent=2))

    def poll_reminders(self):
        if self.closing:
            return
        try:
            for item in self.runtime.scheduler.claim_due():
                self.append("marvin", "Lembrete: " + item["message"])
                self.runtime.scheduler.ack(item["id"], item["claim_token"])
        except Exception as exc:
            self.status.configure(text="Lembretes: " + str(exc)[:160])
        self.window.after(3000, self.poll_reminders)

    def diagnostics(self):
        from .health import collect_health, format_health
        def collect():
            try:
                self.post("panel", ("Diagnóstico local", format_health(collect_health(ROOT, self.data_dir, include_hardware=True))))
            except Exception as exc:
                self.post("note", "Diagnóstico: " + str(exc)[:300])
        self.worker(collect, name="MARVIN-health")

    def audio_settings(self):
        from .voice import audio_devices
        try:
            info = audio_devices()
        except Exception as exc:
            self.panel("Áudio", "Bibliotecas/dispositivos indisponíveis: " + str(exc) + "\nExecute INSTALAR.bat para instalar os recursos opcionais.")
            return
        popup = self.panel("Áudio", json.dumps(info, ensure_ascii=False, indent=2) + "\nPrefira nome do dispositivo a índice. Reinicie a escuta após mudar. Voz durante TTS não é full duplex; use Esc.")
        row = tk.Frame(popup, bg=BG)
        row.pack(fill="x", padx=12, pady=10)
        mic, output = tk.Entry(row), tk.Entry(row)
        for label, entry, key in (("Microfone", mic, "MARVIN_MIC_DEVICE"), ("Saída", output, "MARVIN_OUTPUT_DEVICE")):
            tk.Label(row, text=label, bg=BG, fg=FG).pack(side="left")
            entry.pack(side="left", padx=5)
            entry.insert(0, os.getenv(key, ""))
        def save():
            if self.busy:
                return
            save_preferences(self.data_dir, {"MARVIN_MIC_DEVICE": mic.get(), "MARVIN_OUTPUT_DEVICE": output.get(), "MARVIN_MIC_RATE": "auto"})
            self.wake_stop.set()
            self.window.after(1500, lambda: self.update_wake(persist=False))
            popup.destroy()
        self.button(row, "SALVAR", save)

    def open_workspace(self):
        try:
            os.startfile(str(self.workspace.root))
        except Exception as exc:
            self.append("status", "Projetos em " + str(self.workspace.root) + " · " + str(exc)[:150])

    def review_code(self):
        proposals = self.source_editor.pending()
        if not proposals:
            self.append("status", "Nenhuma proposta de código pendente.")
            return
        meta = proposals[0]
        try:
            popup = self.panel("Revisão de código", meta.get("reason", "") + "\n\nVerificações da proposta:\n" +
                json.dumps(meta.get("verification", {"runtime_tests": "not_run"}), ensure_ascii=False, indent=2) +
                "\n\n" + self.source_editor.diff(meta["id"]))
        except Exception as exc:
            self.append("status", str(exc))
            return
        def apply():
            if self.busy:
                messagebox.showinfo("Código", "Aguarde terminar a tarefa.", parent=popup)
                return
            if not messagebox.askyesno("Aplicar proposta", "Aplicar os arquivos revisados com backup? Reinicie depois da alteração.", parent=popup):
                return
            try:
                result = self.source_editor.apply_reviewed(meta["id"])
                self.append("status", json.dumps(result, ensure_ascii=False))
                popup.destroy()
            except Exception as exc:
                messagebox.showerror("Código", str(exc), parent=popup)
        self.button(popup, "APROVAR E APLICAR", apply)

    def visual_from_text(self):
        question = self.text.get().strip()
        if question and not self.busy:
            self.text.delete(0, "end")
            self.run_visual(question)

    def run_visual(self, question, task_id=None):
        if self.privacy.get():
            self.append("status", "Desative Privacidade para autorizar uma captura.")
            if task_id:
                self.runtime.tasks.set_state(task_id, "waiting_user", "Captura bloqueada por Privacidade.")
            return
        readiness = self.visual_agent.readiness()
        if not readiness.startswith("Integração SDK instalada"):
            self.append("status", readiness)
            if task_id:
                self.runtime.tasks.set_state(task_id, "failed", readiness)
            return
        if not messagebox.askyesno("Agente visual", "Autorizar captura de tela e controle de mouse/teclado para:\n\n" + question[:500] + "\n\nConfira o endpoint e mantenha a tela visível. Esc solicita interrupção."):
            if task_id:
                self.runtime.tasks.set_state(task_id, "cancelled")
            return
        task_id = task_id or self.runtime.prepare(question)["id"]
        self.set_busy()
        self.visual_running = True
        self.token = TaskControl()
        token = self.token
        self.append("you", question)
        def worker():
            with self.runtime.desktop_lock:
                self.runtime.tasks.set_state(task_id, "running")
                self.runtime.tasks.begin_step(task_id, "visual:1", "visual_agent", {"task": question})
                try:
                    answer = self.visual_agent.run(question, notify=lambda k, m: self.post("status", m), cancel_event=token)
                    state = "cancelled" if token.is_set() else "needs_reconciliation"
                    result = {"ok": False, "status": "needs_reconciliation", "message": answer}
                except Exception as exc:
                    answer = str(exc)[:500]
                    state = "cancelled" if token.is_set() else "failed"
                    result = {"ok": False, "status": state, "message": answer}
                self.runtime.tasks.finish_step(task_id, "visual:1", result)
                self.runtime.tasks.set_state(task_id, state, answer)
                self.post("reply", answer)
                self.post("finish")
        self.worker(worker, name="MARVIN-visual")

    def test_voice(self):
        if self.busy:
            return
        self.token = TaskControl()
        self.set_busy()
        voice, token = self.voice_selected.get(), self.token
        def worker():
            try:
                used = speak("Olá, João. Sou o Marvin. Confira se você consegue me ouvir.", voice=voice, cancel_event=token, status=lambda s: self.post("status", s))
                self.post("note", "Reprodução encerrada usando " + used + ". A audibilidade precisa ser conferida por você.")
            except Exception as exc:
                self.post("note", "Áudio: " + str(exc)[:450])
            finally:
                self.post("finish")
        self.worker(worker, name="MARVIN-voice-test")

    def reload_ai(self):
        if self.busy or self.visual_running:
            self.append("status", "Aguarde a tarefa terminar antes de recarregar a IA.")
            return
        try:
            reload_gemini_config(ROOT)
            replacement = Brain(self.memory)
        except Exception as exc:
            self.append("status", "Configuração não alterada: " + safe_error_detail(exc))
            return
        previous = self.brain
        self.brain = replacement
        self.action_agent.brain = replacement
        try:
            previous.close()
        except Exception:
            pass
        self.mode.configure(text="LOCAL · API ainda não validada")
        self.append("status", f"IA recarregada: {replacement.provider} / {replacement.configured_model}. Use TESTAR IA para validar acesso e cota.")

    def test_google(self):
        if self.busy:
            return
        self.token = TaskControl()
        self.set_busy()
        self.post("note", f"Teste de {self.brain.provider}: geração curta, usa a cota/saldo configurado da API.")
        def worker():
            try:
                self.post("note", self.brain.diagnose())
            except Exception as exc:
                self.post("note", "Diagnóstico IA: " + safe_error_detail(exc))
            finally:
                self.post("finish")
        self.worker(worker, name="MARVIN-google-test")

    def clear_memory(self):
        if not self.busy and messagebox.askyesno("Limpar memória", "Excluir histórico, contexto e lembranças? Backups de migração e o registro de tarefas são mantidos."):
            self.memory.clear()
            self.append("status", "Memória de conversa apagada.")

    def on_close(self):
        if self.closing:
            return
        self.cancel_all()
        self.closing = True
        self.wake_stop.set()
        for after_id in self.window.tk.call("after", "info"):
            try:
                self.window.after_cancel(after_id)
            except tk.TclError:
                pass
        self.window.destroy()
        # Keep the instance lock until all old workers exit. They can still own
        # a microphone, API request or desktop operation after the window closes.
        def release():
            for thread in list(self._workers):
                if thread is not threading.current_thread():
                    thread.join()
            self.brain.close()
            self.event_log.close()
            self.instance_lock.close()
        threading.Thread(target=release, daemon=True, name="MARVIN-close").start()

    def run(self):
        self.window.mainloop()


def main():
    MarvinApp().run()


if __name__ == "__main__":
    main()
