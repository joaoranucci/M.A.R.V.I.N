"""Prefer the built desktop; retain the lightweight classic interface."""
import importlib.util
from pathlib import Path
import sys

if __name__ == "__main__":
    legacy = "--legacy" in sys.argv
    if legacy:
        sys.argv.remove("--legacy")
    ready = (Path(__file__).parent / "desktop/dist/index.html").is_file()
    ready = ready and all(importlib.util.find_spec(m) for m in ("fastapi", "uvicorn", "webview"))
    if ready and not legacy:
        from marvin.desktop import main
    else:
        from marvin.app import main
    main()
