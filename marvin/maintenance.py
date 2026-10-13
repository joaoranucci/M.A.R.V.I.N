"""Code-only snapshots and recovery. .env, user data, models and projects are never restored here."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import uuid

from .config import ROOT


def source_files(root):
    root = Path(root).resolve()
    patterns = ("*.py", "*.bat", "*.md", "requirements*.txt", "VERSAO.txt", ".env.example",
                "marvin/*.py", "tests/*.py", "docs/*.md", "local_model/*.ps1",
                "ui_tars_bridge/runner.mjs", "ui_tars_bridge/package.json")
    paths = set()
    for pattern in patterns:
        for path in root.glob(pattern):
            if path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root):
                paths.add(path)
    return sorted(paths)


def snapshot(root=ROOT):
    root = Path(root).resolve()
    name = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + "-" + uuid.uuid4().hex[:6]
    directory = root / "data" / "upgrade_backups" / name
    if not directory.resolve().is_relative_to(root):
        raise ValueError("Backup fora da instalação.")
    directory.mkdir(parents=True)
    files = {}
    for path in source_files(root):
        relative = path.relative_to(root).as_posix()
        contents = path.read_bytes()
        target = directory / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(contents)
        files[relative] = hashlib.sha256(contents).hexdigest()
    (directory / "manifest.json").write_text(json.dumps({"version": 1, "files": files}, indent=2), encoding="utf-8")
    return directory


def restore_code(directory, root=ROOT):
    root, directory = Path(root).resolve(), Path(directory).resolve()
    if not directory.is_relative_to(root / "data" / "upgrade_backups") or not directory.is_dir():
        raise ValueError("Escolha uma pasta dentro de data/upgrade_backups.")
    allowed = {p.relative_to(directory).as_posix(): p for p in source_files(directory)}
    manifest_path = directory / "manifest.json"
    if manifest_path.exists():
        files = json.loads(manifest_path.read_text(encoding="utf-8"))["files"]
        if set(files) != set(allowed):
            raise ValueError("O conjunto de arquivos do backup foi alterado.")
        for relative, expected in files.items():
            if hashlib.sha256(allowed[relative].read_bytes()).hexdigest() != expected:
                raise ValueError("Backup alterado: " + relative)
    if not allowed:
        raise ValueError("Backup sem código reconhecido.")
    for relative in allowed:
        target = root / relative
        if target.is_symlink() or not target.resolve().is_relative_to(root):
            raise ValueError("Destino inválido: " + relative)
    current = snapshot(root)
    changed = []
    try:
        for relative, source in allowed.items():
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_name(target.name + ".restore-tmp")
            temporary.write_bytes(source.read_bytes())
            temporary.replace(target)
            changed.append(relative)
    except Exception:
        for relative in reversed(changed):
            prior = current / relative
            if prior.exists():
                shutil.copy2(prior, root / relative)
        raise
    return {"files_restored": len(changed), "previous_code_backup": str(current),
            "message": "Código restaurado. Dados, .env e modelos preservados. Reinicie o MARVIN."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("snapshot", "restore-code"))
    parser.add_argument("--snapshot", dest="directory")
    args = parser.parse_args()
    if args.action == "snapshot":
        print(snapshot())
    else:
        if not args.directory:
            parser.error("Informe --snapshot data/upgrade_backups/NOME")
        print("Feche o MARVIN. O código da instalação será substituído; dados e .env serão preservados.")
        if input("Digite RESTAURAR para confirmar: ").strip() != "RESTAURAR":
            raise SystemExit("Cancelado.")
        print(json.dumps(restore_code(args.directory), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
