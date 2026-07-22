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

    def test_research_reading_map_links_papers_to_projects(self) -> None:
        path = ROOT / "RESEARCH_READING_MAP.md"
        self.assertTrue(path.exists(), "missing research reading map")
        text = path.read_text(encoding="utf-8")
        required = [
            "DeepLOB",
            "ABIDES",
            "LOBFrame",
            "High Frequency Trading Acceleration using FPGAs",
            "Precision Time Protocol",
            "https://arxiv.org/abs/1808.03668",
            "https://arxiv.org/abs/1904.12066",
            "https://arxiv.org/html/2403.09267",
            "https://people.ucsc.edu/~hlitz/papers/hft_fpga.pdf",
            "https://arxiv.org/abs/1603.00707",
            "Evidence-bearing repositories",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        packet = (ROOT / "RECRUITER_PACKET.md").read_text(encoding="utf-8")
        self.assertIn("RESEARCH_READING_MAP.md", readme)
        self.assertIn("RESEARCH_READING_MAP.md", packet)

    def test_role_packets_are_curated_for_target_jobs(self) -> None:
        path = ROOT / "ROLE_PACKETS.md"
        self.assertTrue(path.exists(), "missing role packets")
        text = path.read_text(encoding="utf-8")
        required = [
            "Hardware / FPGA Engineer",
            "Quant Developer",
            "Market Infrastructure Engineer",
            "Cyber-Physical Systems Engineer",
            "AI / Software Engineer",
            "Research papers to read first",
            "Primary repositories",
            "Interview narrative",
            "Risk and evidence boundary",
            "fpga-low-latency-market-data-engine",
            "agentic-strategy-search-lab",
            "market-data-tickerplant-simulator",
            "cpse-engineering-labs",
            "llm-market-hypothesis-auditor",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        packet = (ROOT / "RECRUITER_PACKET.md").read_text(encoding="utf-8")
        self.assertIn("ROLE_PACKETS.md", readme)
        self.assertIn("ROLE_PACKETS.md", packet)

    def test_evidence_ledger_maps_capabilities_to_proof(self) -> None:
        path = ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md"
        self.assertTrue(path.exists(), "missing portfolio evidence ledger")
        text = path.read_text(encoding="utf-8")
        required = [
            "Evidence Ledger",
            "Capability",
            "Public proof artifacts",
            "Validation method",
            "Honest boundary",
            "Low-latency market data",
            "Strategy robustness",
            "FPGA and hardware verification",
            "Cyber-physical systems",
            "AI research governance",
            "Recruiter-facing organization",
            "green CI",
            "role packets",
            "whitepapers",
            "reading map",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        packet = (ROOT / "RECRUITER_PACKET.md").read_text(encoding="utf-8")
        self.assertIn("PORTFOLIO_EVIDENCE_LEDGER.md", readme)
        self.assertIn("PORTFOLIO_EVIDENCE_LEDGER.md", packet)


if __name__ == "__main__":
    unittest.main()
