import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("package_skill", ROOT / "scripts" / "package_skill.py")
package_skill = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(package_skill)


class PackageSkillTests(unittest.TestCase):
    def test_zip_is_self_contained_and_has_expected_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "skill.zip"
            package_skill.build_zip(output, ROOT / "skills" / "ohmytaste")
            self.assertTrue(output.is_file())
            with zipfile.ZipFile(output) as archive:
                names = archive.namelist()
                self.assertIn("ohmytaste/SKILL.md", names)
                self.assertIn("ohmytaste/references/evidence-and-search.md", names)
                self.assertIn("ohmytaste/references/taste-and-critique.md", names)
                self.assertIn("ohmytaste/assets/research-proposal.tex", names)
                self.assertTrue(all(name.startswith("ohmytaste/") for name in names))
                self.assertNotIn("README.md", names)

    def test_zip_build_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.zip"
            second = Path(tmp) / "second.zip"
            package_skill.build_zip(first, ROOT / "skills" / "ohmytaste")
            package_skill.build_zip(second, ROOT / "skills" / "ohmytaste")
            self.assertEqual(first.read_bytes(), second.read_bytes())


if __name__ == "__main__":
    unittest.main()
