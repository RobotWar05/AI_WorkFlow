from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_sensitive_data", ROOT / "tools" / "check_sensitive_data.py")
assert SPEC and SPEC.loader
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class SensitiveDataTests(unittest.TestCase):
    def test_detects_high_confidence_patterns_without_fixture_secrets(self) -> None:
        aws = "AK" + "IA" + "1234567890ABCDEF"
        github = "gh" + "p_" + "a" * 20
        openai = "sk-" + "b" * 20
        private_key = "-----BEGIN " + "PRIVATE KEY-----"
        self.assertEqual(checker.findings_for_text(aws), {"aws-access-key"})
        self.assertEqual(checker.findings_for_text(github), {"github-token"})
        self.assertEqual(checker.findings_for_text(openai), {"openai-style-key"})
        self.assertEqual(checker.findings_for_text(private_key), {"private-key"})

    def test_ignores_regular_policy_text(self) -> None:
        self.assertEqual(checker.findings_for_text("Never store a password or API key in a prompt."), set())


if __name__ == "__main__":
    unittest.main()
