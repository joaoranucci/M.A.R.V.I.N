"""One executor per data directory; OS releases the lock after a crash."""
import os


class InstanceLock:
    def __init__(self, directory):
        directory.mkdir(parents=True, exist_ok=True)
        self.stream = (directory / "marvin.lock").open("a+b")
        self.stream.seek(0, 2)
        if self.stream.tell() == 0:
            self.stream.write(b"0")
            self.stream.flush()
        self.stream.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(self.stream.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            self.stream.close()
            raise RuntimeError("O MARVIN já está usando esta pasta de dados. Encerre a outra instância antes de abrir novamente.") from exc

    def close(self):
        if not self.stream.closed:
            self.stream.close()
