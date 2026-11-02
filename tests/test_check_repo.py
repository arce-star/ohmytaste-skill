import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_repo", ROOT / "scripts" / "check_repo.py")
check_repo = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(check_repo)


class CheckRepoTests(unittest.TestCase):
    def test_repository_passes_checks(self):
        self.assertEqual(check_repo.run_checks(ROOT), [])

    def test_frontmatter_parser_reads_required_fields(self):
        fields, body = check_repo.parse_frontmatter(
            "---\nname: example-skill\ndescription: Example description\n---\n# Body\n"
        )
        self.assertEqual(fields["name"], "example-skill")
        self.assertEqual(fields["description"], "Example description")
        self.assertIn("# Body", body)

    def test_frontmatter_parser_rejects_missing_delimiter(self):
        with self.assertRaises(ValueError):
            check_repo.parse_frontmatter("name: invalid\n")


if __name__ == "__main__":
    unittest.main()
