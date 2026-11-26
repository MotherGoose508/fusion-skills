"""Check the distributable package without starting Fusion."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


class PackageTests(unittest.TestCase):
    def test_skill_entrypoints(self):
        entrypoints = sorted(SKILLS.glob("*/SKILL.md"))
        self.assertEqual(
            [path.parent.name for path in entrypoints],
            ["fusion-core", "fusion-mechanisms"],
        )
        for path in entrypoints:
            with self.subTest(skill=path.parent.name):
                sections = path.read_text(encoding="utf-8").split("---\n", 2)
                self.assertEqual(len(sections), 3)
                self.assertEqual(sections[0], "")
                header = dict(line.split(": ", 1) for line in sections[1].splitlines())
                self.assertEqual(header["name"], path.parent.name)
                self.assertRegex(header["description"], r"\S")
                self.assertTrue(sections[2].strip(), "Empty skill body")

    def test_relative_document_links_resolve_within_package(self):
        paths = [ROOT / "README.md"]
        for folder in ("docs", "profiles", "skills", "tests"):
            paths.extend((ROOT / folder).rglob("*.md"))
        for path in paths:
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                relative_path = target.partition("#")[0]
                if not relative_path or "://" in relative_path:
                    continue
                with self.subTest(file=path.relative_to(ROOT), link=target):
                    resolved = (path.parent / relative_path).resolve()
                    self.assertTrue(resolved.is_relative_to(ROOT), "Link escapes package")
                    self.assertTrue(resolved.exists(), "Missing link target")

    def test_shared_profile_templates_exist(self):
        for name in ("default", "project", "frc-team"):
            with self.subTest(profile=name):
                self.assertTrue((ROOT / "profiles" / f"{name}.md").is_file())

    def test_verification_cases_are_packaged(self):
        for number in range(1, 6):
            with self.subTest(case=number):
                self.assertEqual(len(list((ROOT / "tests/cases").glob(f"{number:02d}-*.md"))), 1)
        self.assertTrue((ROOT / "tests/evaluation-record.md").is_file())

    def test_fusion_smoke_script_is_loadable_source(self):
        directory = ROOT / "tests/fusion/FusionSkillsSmoke"
        manifest = directory / f"{directory.name}.manifest"
        config = json.loads(manifest.read_text(encoding="utf-8"))
        self.assertEqual(config["autodeskProduct"], "Fusion")
        self.assertEqual(config["type"], "script")
        script = directory / f"{directory.name}.py"
        compile(script.read_text(encoding="utf-8"), str(script), "exec")


if __name__ == "__main__":
    unittest.main()
