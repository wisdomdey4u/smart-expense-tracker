import os
import unittest
from unittest.mock import patch

import main


class SupabaseConfigTests(unittest.TestCase):
    def test_uses_supabase_key_when_present(self):
        with patch.dict(os.environ, {"SUPABASE_URL": "https://example.supabase.co", "SUPABASE_KEY": "abc123"}, clear=True):
            self.assertEqual(main.get_supabase_credentials(), ("https://example.supabase.co", "abc123"))

    def test_falls_back_to_supabase_kek(self):
        with patch.dict(os.environ, {"SUPABASE_URL": "https://example.supabase.co", "SUPABASE_KEK": "abc123"}, clear=True):
            self.assertEqual(main.get_supabase_credentials(), ("https://example.supabase.co", "abc123"))

    def test_normalizes_uppercase_scheme(self):
        with patch.dict(os.environ, {"SUPABASE_URL": "HTTPS://example.supabase.co", "SUPABASE_KEY": "abc123"}, clear=True):
            self.assertEqual(main.get_supabase_credentials(), ("https://example.supabase.co", "abc123"))


if __name__ == "__main__":
    unittest.main()
