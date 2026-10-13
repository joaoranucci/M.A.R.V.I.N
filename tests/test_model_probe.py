import base64
import io
import json
import os
import struct
import unittest
import zlib
from unittest.mock import patch

from marvin.model_probe import make_synthetic_png, request_json


class TestModelProbe(unittest.TestCase):
    def test_png_signature_dimensions_and_pixels(self):
        data = base64.b64decode(make_synthetic_png())
        self.assertTrue(data.startswith(b'\x89PNG\r\n\x1a\n'))
        self.assertEqual(struct.unpack('>II', data[16:24]), (16,16))
        content = zlib.decompress(data[41:-16])
        self.assertEqual(len(content), 16*(1+16*3))
        self.assertEqual(content[1:4], b'\xf0\x20\x20')
        self.assertEqual(content[1+8*3:1+8*3+3], b'\xff\xff\xff')

    def test_endpoint_alias(self):
        from marvin.visual_agent import VisualSettings
        with patch.dict(os.environ,{'UI_TARS_BASE_URL':'http://127.0.0.1:8080/v1','UI_TARS_MODEL':'ui-tars-local'}):
            c=VisualSettings.from_env()
            self.assertEqual(c.model,'ui-tars-local')

    def test_setup_scripts_restrict_bind_and_have_checksums(self):
        from pathlib import Path
        base=Path(__file__).resolve().parent.parent
        install=(base/'local_model'/'install.ps1').read_text()
        start=(base/'local_model'/'start.ps1').read_text()
        self.assertIn('Get-FileHash',install)
        self.assertIn('cuda-12.4-x64',install)
        self.assertIn('--no-mmproj-offload',start)
        self.assertIn("'127.0.0.1'",start)
        self.assertNotIn("'0.0.0.0'",start)


if __name__=='__main__':unittest.main()
