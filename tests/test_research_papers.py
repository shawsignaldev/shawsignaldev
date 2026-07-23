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

    def test_reproducibility_guide_has_exact_verification_commands(self) -> None:
        path = ROOT / "REPRODUCIBILITY_GUIDE.md"
        self.assertTrue(path.exists(), "missing reproducibility guide")
        text = path.read_text(encoding="utf-8")
        required = [
            "Reproducibility Guide",
            "Profile verification",
            "Site verification",
            "Representative repository verification",
            "gh run list",
            "python -m unittest discover -s tests -v",
            "python -m pytest -q -p no:cacheprovider",
            "git status --short",
            "shawsignaldev.github.io",
            "fpga-low-latency-market-data-engine",
            "agentic-strategy-search-lab",
            "market-data-tickerplant-simulator",
            "What this proves",
            "What this does not prove",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        packet = (ROOT / "RECRUITER_PACKET.md").read_text(encoding="utf-8")
        self.assertIn("REPRODUCIBILITY_GUIDE.md", readme)
        self.assertIn("REPRODUCIBILITY_GUIDE.md", packet)

    def test_flagship_systems_map_turns_repos_into_research_programs(self) -> None:
        path = ROOT / "FLAGSHIP_SYSTEMS_MAP.md"
        self.assertTrue(path.exists(), "missing flagship systems map")
        text = path.read_text(encoding="utf-8")
        required = [
            "Flagship Systems Map",
            "Why this exists",
            "Flagship 1: Low-Latency Market Data and FPGA Trading Datapath",
            "Flagship 2: Limit Order Book Intelligence and Market Simulation",
            "Flagship 3: Options Microstructure and 0DTE Research OS",
            "Flagship 4: AI-Governed Quant Research Factory",
            "Flagship 5: Cyber-Physical Timing, Control, and Operator Systems",
            "Primary thesis",
            "Core repositories",
            "Paper-backed foundation",
            "Proof artifacts reviewers should inspect",
            "Next research upgrades",
            "DeepLOB",
            "ABIDES",
            "LOBFrame",
            "High Frequency Trading Acceleration using FPGAs",
            "not isolated repo count",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        packet = (ROOT / "RECRUITER_PACKET.md").read_text(encoding="utf-8")
        self.assertIn("FLAGSHIP_SYSTEMS_MAP.md", readme)
        self.assertIn("FLAGSHIP_SYSTEMS_MAP.md", packet)

    def test_advanced_research_build_queue_has_paper_anchored_project_specs(self) -> None:
        path = ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md"
        self.assertTrue(path.exists(), "missing advanced research build queue")
        text = path.read_text(encoding="utf-8")
        required = [
            "Advanced Research Build Queue",
            "Selection standard",
            "Flagship system",
            "Repository concept",
            "Role signal",
            "Paper anchor",
            "Proof required before promotion",
            "Wave 1: Flagship Hardening",
            "Wave 2: Paper Reproduction and Benchmarking",
            "Wave 3: Hardware Acceleration and Formal Verification",
            "Wave 4: Options and Intraday Trading Research",
            "Wave 5: Cyber-Physical and Operator Systems",
            "DeepLOB",
            "ABIDES",
            "LOBFrame",
            "LOB-Bench",
            "LOBIN",
            "High Frequency Trading Acceleration using FPGAs",
            "not count-only expansion",
        ]
        for phrase in required:
            self.assertIn(phrase, text)
        self.assertGreaterEqual(text.count("|"), 160)

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        packet = (ROOT / "RECRUITER_PACKET.md").read_text(encoding="utf-8")
        self.assertIn("ADVANCED_RESEARCH_BUILD_QUEUE.md", readme)
        self.assertIn("ADVANCED_RESEARCH_BUILD_QUEUE.md", packet)

    def test_shared_market_packet_fixtures_is_promoted_as_flagship_infrastructure(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("shared-market-packet-fixtures", text)
            self.assertIn("Shared Market Packet Fixtures", text)

    def test_fpga_orderflow_formal_properties_is_promoted_as_hardware_verification(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("fpga-orderflow-formal-properties", text)
            self.assertIn("FPGA Orderflow Formal Properties", text)
            self.assertIn("halt latch", text)
            self.assertIn("bounded acknowledgement latency", text)

    def test_lob_benchmark_report_generator_is_promoted_as_quant_research_infrastructure(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("lob-benchmark-report-generator", text)
            self.assertIn("LOB Benchmark Report Generator", text)
            self.assertIn("cost-adjusted", text)
            self.assertIn("Brier", text)
            self.assertIn("latency pass", text)

    def test_market_sim_scenario_library_is_promoted_as_abides_style_fixtures(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("market-sim-scenario-library", text)
            self.assertIn("Market Sim Scenario Library", text)
            self.assertIn("ABIDES", text)
            self.assertIn("deterministic seeds", text)
            self.assertIn("latency", text)
            self.assertIn("liquidity", text)

    def test_synthetic_options_chain_generator_is_promoted_as_options_research_infrastructure(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("synthetic-options-chain-generator", text)
            self.assertIn("Synthetic Options Chain Generator", text)
            self.assertIn("IV skew", text)
            self.assertIn("open interest", text)
            self.assertIn("target-delta", text)

    def test_option_replay_report_engine_is_promoted_as_options_pnl_attribution(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("option-replay-report-engine", text)
            self.assertIn("Option Replay Report Engine", text)
            self.assertIn("contract PnL", text)
            self.assertIn("theta drag", text)
            self.assertIn("volatility contribution", text)
            self.assertIn("verdict", text)

    def test_research_queue_state_machine_is_promoted_as_ai_research_governance(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("research-queue-state-machine", text)
            self.assertIn("Research Queue State Machine", text)
            self.assertIn("evidence-gated", text)
            self.assertIn("promoted", text)
            self.assertIn("watchlisted", text)
            self.assertIn("human approval", text)

    def test_degraded_mode_operator_console_is_promoted_as_cpse_operator_system(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("degraded-mode-operator-console", text)
            self.assertIn("Degraded Mode Operator Console", text)
            self.assertIn("Precision Time Protocol", text)
            self.assertIn("operator acknowledgement", text)
            self.assertIn("recovery", text)
            self.assertIn("safe mode", text)

    def test_deeplob_leakage_test_harness_is_promoted_as_quant_ml_hygiene(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("deeplob-leakage-test-harness", text)
            self.assertIn("DeepLOB Leakage Test Harness", text)
            self.assertIn("chronological split", text)
            self.assertIn("label horizon", text)
            self.assertIn("lookahead leakage", text)
            self.assertIn("baseline metrics", text)


if __name__ == "__main__":
    unittest.main()
