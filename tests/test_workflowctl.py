from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("workflowctl", ROOT / "tools" / "workflowctl.py")
assert SPEC and SPEC.loader
workflowctl = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflowctl)


class WorkflowCtlTests(unittest.TestCase):
    def test_path_overlap_respects_segment_boundaries(self) -> None:
        self.assertTrue(workflowctl.paths_overlap("src/api", "src/api/routes.py"))
        self.assertFalse(workflowctl.paths_overlap("src/api", "src/apis/routes.py"))

    def test_path_allowed_requires_child_of_write_scope(self) -> None:
        self.assertTrue(workflowctl.path_allowed("tests/api/test_x.py", ["tests/api/"]))
        self.assertFalse(workflowctl.path_allowed("deploy/prod.yml", ["tests/api/"]))

    def test_scope_rejects_absolute_and_traversal_paths(self) -> None:
        for value in ("../secret", "C:\\secret", "/etc/passwd"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                workflowctl.normalize_scope(value)

    def test_custom_datetime_checker_rejects_invalid_value(self) -> None:
        schema = {"type": "string", "format": "date-time"}
        validator = workflowctl.Draft202012Validator(schema, format_checker=workflowctl.FORMAT_CHECKER)
        self.assertTrue(list(validator.iter_errors("not-a-date")))

    def test_orchestration_fixtures_match_expected_codes(self) -> None:
        suite = workflowctl.load_json(ROOT / "evals" / "cases" / "v2-orchestration-suite.json")
        for case in suite["cases"]:
            with self.subTest(case=case["id"]):
                self.assertEqual(workflowctl.semantic_case(case), set(case["expected_errors"]))

    def test_generated_adapters_are_deterministic_and_marked(self) -> None:
        expected = workflowctl.expected_adapters()
        self.assertEqual(len(expected), 27)
        self.assertTrue(all(workflowctl.GENERATED_HEADER in content for content in expected.values()))
        self.assertEqual(workflowctl.adapter_drift(), [])

    def test_worker_cannot_close_parent_task(self) -> None:
        machine = workflowctl.load_json(ROOT / "orchestration" / "state-machines" / "task-lifecycle.json")
        event = workflowctl.load_json(ROOT / "contracts" / "examples" / "invalid" / "status-event-illegal-transition.json")
        self.assertEqual(workflowctl.status_event_codes(event, machine), {"ILLEGAL_TRANSITION", "ROLE_NOT_ALLOWED"})

    def test_read_only_adapters_keep_write_tools_out(self) -> None:
        expected = workflowctl.expected_adapters()
        claude = expected[ROOT / ".claude" / "agents" / "researcher.md"]
        antigravity = expected[ROOT / ".agents" / "agents" / "researcher.md"]
        codex = expected[ROOT / ".codex" / "agents" / "researcher.toml"]
        self.assertNotIn("Edit, Write", claude)
        self.assertNotIn("replace_file_content", antigravity)
        self.assertIn('sandbox_mode = "read-only"', codex)

    def test_route_registry_is_complete_and_files_exist(self) -> None:
        errors: list[str] = []
        workflowctl.validate_routes(errors)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
