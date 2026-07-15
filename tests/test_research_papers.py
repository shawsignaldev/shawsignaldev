from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ResearchPaperTests(unittest.TestCase):
    def test_three_central_whitepapers_exist_with_recruiter_evidence(self) -> None:
        expected = [
            "market-data-infrastructure-whitepaper.md",
            "strategy-robustness-whitepaper.md",
            "fpga-trading-architecture-whitepaper.md",
        ]
        for filename in expected:
            path = ROOT / "papers" / filename
            self.assertTrue(path.exists(), f"missing {filename}")
            text = path.read_text(encoding="utf-8")
            self.assertIn("Evidence Map", text)
            self.assertIn("Limits and Honest Boundaries", text)
            self.assertIn("Recruiter Signal", text)
            self.assertGreaterEqual(len(text.split()), 900)

    def test_readme_and_recruiter_packet_link_papers(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        packet = (ROOT / "RECRUITER_PACKET.md").read_text(encoding="utf-8")
        for filename in [
            "market-data-infrastructure-whitepaper.md",
            "strategy-robustness-whitepaper.md",
            "fpga-trading-architecture-whitepaper.md",
        ]:
            self.assertIn(f"papers/{filename}", readme)
            self.assertIn(f"papers/{filename}", packet)


if __name__ == "__main__":
    unittest.main()
