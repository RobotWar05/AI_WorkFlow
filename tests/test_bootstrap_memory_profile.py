from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "bootstrap_memory_profile.py"


class BootstrapMemoryProfileTests(unittest.TestCase):
    def project(self, parent: Path) -> Path:
        target = parent / "project"
        (target / ".agents").mkdir(parents=True)
        return target

    def run_tool(self, target: Path, profile: str, apply: bool = False) -> subprocess.CompletedProcess[str]:
        command = [sys.executable, "-B", str(TOOL), "--target", str(target), "--profile", profile]
        if apply:
            command.append("--apply")
        return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)

    def test_dry_run_does_not_create_projection(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            target = self.project(Path(temp))
            result = self.run_tool(target, "balanced")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("WOULD CREATE knowledge", result.stdout)
            self.assertFalse((target / "knowledge").exists())
            self.assertFalse((target / ".agents" / "memory-profile.json").exists())

    def test_dry_run_accepts_project_without_control_plane(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            target = Path(temp) / "project"
            target.mkdir()
            result = self.run_tool(target, "deep")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("PREREQUISITE", result.stdout)
            self.assertIn("WOULD CREATE knowledge", result.stdout)
            self.assertFalse((target / ".agents").exists())

    def test_apply_requires_existing_control_plane(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            target = Path(temp) / "project"
            target.mkdir()
            result = self.run_tool(target, "balanced", apply=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn("Target has no .agents control plane", result.stderr)
            self.assertFalse((target / "knowledge").exists())

    def test_none_creates_manifest_without_vault(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            target = self.project(Path(temp))
            result = self.run_tool(target, "none", apply=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((target / "knowledge").exists())
            data = json.loads((target / ".agents" / "memory-profile.json").read_text(encoding="utf-8"))
            self.assertEqual(data["profile"], "none")
            self.assertEqual(data["raw_chat_storage"], "forbidden")

    def test_balanced_creates_approval_gated_vault(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            target = self.project(Path(temp))
            result = self.run_tool(target, "balanced", apply=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((target / "knowledge" / "90-system" / "templates" / "source-record.md").is_file())
            self.assertTrue((target / "knowledge" / ".gitignore").is_file())
            self.assertFalse((target / "knowledge" / ".aiwf-index").exists())

    def test_deep_creates_manual_index_manifest_only(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            target = self.project(Path(temp))
            result = self.run_tool(target, "deep", apply=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            manifest = target / "knowledge" / "90-system" / "index-manifest.md"
            self.assertTrue(manifest.is_file())
            self.assertIn("manual-only", manifest.read_text(encoding="utf-8"))
            data = json.loads((target / ".agents" / "memory-profile.json").read_text(encoding="utf-8"))
            self.assertEqual(data["semantic_index"]["hook_capture"], "forbidden")

    def test_refuses_existing_knowledge_or_manifest(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            target = self.project(Path(temp))
            (target / "knowledge").mkdir()
            result = self.run_tool(target, "balanced", apply=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn("Refusing to overwrite", result.stderr)


if __name__ == "__main__":
    unittest.main()
