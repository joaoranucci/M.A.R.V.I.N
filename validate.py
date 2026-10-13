"""Run the offline test suite and save a factual, local validation report."""
import argparse
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import platform
import sys
import time
import unittest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('docs/validation-results.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    suite = unittest.defaultTestLoader.discover(str(root/'tests'))
    stream = io.StringIO()
    started = time.monotonic()
    result = unittest.TextTestRunner(stream=stream, verbosity=1).run(suite)
    from importlib.metadata import version, PackageNotFoundError
    try:
        sdk = version('google-genai')
    except PackageNotFoundError:
        sdk = None
    report = {'executed_at_utc': datetime.now(timezone.utc).isoformat(), 'python': platform.python_version(),
              'system': platform.system(), 'google_genai': sdk, 'tests_run': result.testsRun,
              'failures': len(result.failures), 'errors': len(result.errors), 'skipped': len(result.skipped),
              'successful': result.wasSuccessful(), 'duration_seconds': round(time.monotonic()-started, 3),
              'scope': 'offline automated tests; real temporary files, child processes and withdrawn Tk; model/network/audio adapters simulated',
              'output': stream.getvalue()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(stream.getvalue())
    print('Relatório:', args.output)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(main())
