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
            "Wave 6: Integration Capstones",
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

    def test_pcie_dma_descriptor_verification_is_promoted_as_hardware_data_movement(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("pcie-dma-descriptor-verification", text)
            self.assertIn("PCIe DMA Descriptor Verification", text)
            self.assertIn("descriptor validity", text)
            self.assertIn("wraparound", text)
            self.assertIn("burst sizing", text)
            self.assertIn("completion accounting", text)
            self.assertIn("FPGA", text)
            self.assertIn("DMA", text)
            self.assertIn("public-safe", text)

    def test_axi_stream_backpressure_lab_is_promoted_as_fpga_verification(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("axi-stream-backpressure-lab", text)
            self.assertIn("AXI Stream Backpressure Lab", text)
            self.assertIn("ready/valid", text)
            self.assertIn("stall coverage", text)
            self.assertIn("no-loss packet tests", text)
            self.assertIn("skid buffer", text)
            self.assertIn("FPGA", text)
            self.assertIn("public-safe", text)

    def test_itch_to_risk_full_pipeline_is_promoted_as_end_to_end_fpga_pipeline(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("itch-to-risk-full-pipeline", text)
            self.assertIn("ITCH To Risk Full Pipeline", text)
            self.assertIn("end-to-end parse", text)
            self.assertIn("book update", text)
            self.assertIn("risk approval", text)
            self.assertIn("replay trace", text)
            self.assertIn("FPGA", text)
            self.assertIn("public-safe", text)

    def test_ptp_fault_injection_core_is_promoted_as_cpse_timing_resilience(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("ptp-fault-injection-core", text)
            self.assertIn("PTP Fault Injection Core", text)
            self.assertIn("Offset attack", text)
            self.assertIn("Drift injection", text)
            self.assertIn("Recovery", text)
            self.assertIn("Operator alert", text)
            self.assertIn("Precision Time Protocol", text)
            self.assertIn("cyber-physical", text)
            self.assertIn("public-safe", text)

    def test_lobin_style_in_network_inference_is_promoted_as_hardware_ai_acceleration(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("lobin-style-in-network-inference", text)
            self.assertIn("LOBIN-Style In-Network Inference", text)
            self.assertIn("SmartNIC/P4-style", text)
            self.assertIn("public-safe", text)
            self.assertIn("fixed-point", text)
            self.assertIn("latency/accuracy tradeoff", text)
            self.assertIn("not a production trading system", text)

    def test_quantized_lob_inference_fpga_is_promoted_as_fpga_ml_inference(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("quantized-lob-inference-fpga", text)
            self.assertIn("Quantized LOB Inference FPGA", text)
            self.assertIn("DeepLOB", text)
            self.assertIn("LOBIN", text)
            self.assertIn("public-safe", text)
            self.assertIn("fixed-point", text)
            self.assertIn("error bounds", text)
            self.assertIn("throughput estimate", text)
            self.assertIn("not a production trading system", text)

    def test_hbm_lob_layout_benchmark_is_promoted_as_memory_systems_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("hbm-lob-layout-benchmark", text)
            self.assertIn("HBM LOB Layout Benchmark", text)
            self.assertIn("LOBFrame", text)
            self.assertIn("public-safe", text)
            self.assertIn("bank conflict", text)
            self.assertIn("row locality", text)
            self.assertIn("throughput", text)
            self.assertIn("storage-layout report", text)
            self.assertIn("not a production trading system", text)

    def test_systolic_lob_feature_engine_is_promoted_as_hardware_acceleration_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("systolic-lob-feature-engine", text)
            self.assertIn("Systolic LOB Feature Engine", text)
            self.assertIn("DeepLOB", text)
            self.assertIn("public-safe", text)
            self.assertIn("matrix/vector feature projection", text)
            self.assertIn("cycle estimate", text)
            self.assertIn("limitations", text)
            self.assertIn("not a production trading system", text)

    def test_zero_dte_opening_drive_study_is_promoted_as_options_research_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("zero-dte-opening-drive-study", text)
            self.assertIn("Zero-DTE Opening Drive Study", text)
            self.assertIn("Strategy Robustness Whitepaper", text)
            self.assertIn("public-safe", text)
            self.assertIn("First 5/15/45 minute windows", text)
            self.assertIn("risk sizing", text)
            self.assertIn("slippage", text)
            self.assertIn("walk-forward report", text)
            self.assertIn("not financial advice", text)

    def test_gamma_vwap_confluence_lab_is_promoted_as_options_microstructure_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("gamma-vwap-confluence-lab", text)
            self.assertIn("Gamma/VWAP Confluence Lab", text)
            self.assertIn("Strategy Robustness Whitepaper", text)
            self.assertIn("public-safe", text)
            self.assertIn("gamma level", text)
            self.assertIn("VWAP", text)
            self.assertIn("volume pressure", text)
            self.assertIn("failed-breakout classification", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_weekly_contract_selector_benchmark_is_promoted_as_options_systems_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("weekly-contract-selector-benchmark", text)
            self.assertIn("Weekly Contract Selector Benchmark", text)
            self.assertIn("Strategy Robustness Whitepaper", text)
            self.assertIn("public-safe", text)
            self.assertIn("Same-day versus nearest-weekly comparison", text)
            self.assertIn("liquidity filters", text)
            self.assertIn("target-delta selection", text)
            self.assertIn("spread control", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_intraday_iv_expansion_monitor_is_promoted_as_volatility_research_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("intraday-iv-expansion-monitor", text)
            self.assertIn("Intraday IV Expansion Monitor", text)
            self.assertIn("Rough volatility and IV surface notes", text)
            self.assertIn("public-safe", text)
            self.assertIn("IV expansion/compression labels", text)
            self.assertIn("volatility regime", text)
            self.assertIn("spread control", text)
            self.assertIn("signal-quality report", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_open_interest_liquidity_regime_lab_is_promoted_as_options_data_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("open-interest-liquidity-regime-lab", text)
            self.assertIn("Open Interest Liquidity Regime Lab", text)
            self.assertIn("Strategy Robustness Whitepaper", text)
            self.assertIn("public-safe", text)
            self.assertIn("OI, spread, volume, and contract survivability scoring", text)
            self.assertIn("open interest growth", text)
            self.assertIn("liquidity regime", text)
            self.assertIn("contract survivability", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_first_hour_momentum_regime_lab_is_promoted_as_quant_developer_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("first-hour-momentum-regime-lab", text)
            self.assertIn("First-Hour Momentum Regime Lab", text)
            self.assertIn("LOBFrame", text)
            self.assertIn("public-safe", text)
            self.assertIn("Open, midday, and close regime splits", text)
            self.assertIn("expectancy", text)
            self.assertIn("drawdown", text)
            self.assertIn("volume confirmation", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_session_high_low_breakout_validator_is_promoted_as_trading_systems_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("session-high-low-breakout-validator", text)
            self.assertIn("Session High/Low Breakout Validator", text)
            self.assertIn("Strategy Robustness Whitepaper", text)
            self.assertIn("public-safe", text)
            self.assertIn("Premarket, regular session, and close-range breakout validation", text)
            self.assertIn("close-location value", text)
            self.assertIn("VWAP distance", text)
            self.assertIn("volume pressure", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_risk_adjusted_trade_sizing_engine_is_promoted_as_risk_systems_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("risk-adjusted-trade-sizing-engine", text)
            self.assertIn("Risk-Adjusted Trade Sizing Engine", text)
            self.assertIn("Strategy Robustness Whitepaper", text)
            self.assertIn("public-safe", text)
            self.assertIn("Kelly-capped, drawdown-capped, volatility-scaled sizing report", text)
            self.assertIn("risk budget", text)
            self.assertIn("position debit", text)
            self.assertIn("dollars at risk", text)

    def test_plant_market_control_analogy_lab_is_promoted_as_cpse_control_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("plant-market-control-analogy-lab", text)
            self.assertIn("Plant Market Control Analogy Lab", text)
            self.assertIn("Precision Time Protocol references", text)
            self.assertIn("public-safe", text)
            self.assertIn("Sensor, estimator, controller, actuator, and operator intervention model", text)
            self.assertIn("sensor health", text)
            self.assertIn("control error", text)
            self.assertIn("operator intervention", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_distributed_clock_health_dashboard_is_promoted_as_timing_systems_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("distributed-clock-health-dashboard", text)
            self.assertIn("Distributed Clock Health Dashboard", text)
            self.assertIn("Precision Time Protocol references", text)
            self.assertIn("public-safe", text)
            self.assertIn("Clock offset, drift, jitter, and degraded-state visualization", text)
            self.assertIn("fleet health score", text)
            self.assertIn("worst-node ranking", text)
            self.assertIn("operator action", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_real_time_alert_scheduler_is_promoted_as_embedded_systems_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("real-time-alert-scheduler", text)
            self.assertIn("Real-Time Alert Scheduler", text)
            self.assertIn("Real-time scheduling references", text)
            self.assertIn("public-safe", text)
            self.assertIn("Deadline, priority inversion, dropped alert, and recovery checks", text)
            self.assertIn("missed-deadline accounting", text)
            self.assertIn("queue pressure", text)
            self.assertIn("operator recovery", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_udp_control_plane_safety_monitor_is_promoted_as_networked_systems_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("udp-control-plane-safety-monitor", text)
            self.assertIn("UDP Control Plane Safety Monitor", text)
            self.assertIn("Precision Time Protocol references", text)
            self.assertIn("public-safe", text)
            self.assertIn("Packet loss, sequence gap, stale command, and operator override behavior", text)
            self.assertIn("rejected command", text)
            self.assertIn("operator override", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_sensor_fusion_market_risk_bridge_is_promoted_as_cpse_quant_overlap_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("sensor-fusion-market-risk-bridge", text)
            self.assertIn("Sensor Fusion Market Risk Bridge", text)
            self.assertIn("Kalman filtering and state estimation notes", text)
            self.assertIn("public-safe", text)
            self.assertIn("Noisy sensor analogy connected to noisy market state estimation", text)
            self.assertIn("Kalman gain", text)
            self.assertIn("posterior variance", text)
            self.assertIn("low-trust sensor", text)
            self.assertIn("residual risk", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_timing_attack_incident_runbook_is_promoted_as_security_operations_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("timing-attack-incident-runbook", text)
            self.assertIn("Timing Attack Incident Runbook", text)
            self.assertIn("Precision Time Protocol references", text)
            self.assertIn("public-safe", text)
            self.assertIn("Attack, detection, severity, mitigation, and postmortem template", text)
            self.assertIn("escalation", text)
            self.assertIn("operator communication bridge", text)
            self.assertIn("trusted-source recovery", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_evidence_ledger_dashboard_is_promoted_as_software_engineering_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("evidence-ledger-dashboard", text)
            self.assertIn("Evidence Ledger Dashboard", text)
            self.assertIn("Model-risk and evidence-gating notes", text)
            self.assertIn("public-safe", text)
            self.assertIn("Capability-to-proof dashboard with missing-evidence warnings", text)
            self.assertIn("owner coverage", text)
            self.assertIn("rejected proof", text)
            self.assertIn("blocked verdict", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_recruiter_review_path_generator_is_promoted_as_portfolio_systems_evidence(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("recruiter-review-path-generator", text)
            self.assertIn("Recruiter Review Path Generator", text)
            self.assertIn("Internal role packet docs", text)
            self.assertIn("public-safe", text)
            self.assertIn("Role-specific artifact path generated from project metadata", text)
            self.assertIn("selected repositories", text)
            self.assertIn("review steps", text)
            self.assertIn("missing link warnings", text)
            self.assertIn("coverage score", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

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

    def test_lobframe_metric_dashboard_is_promoted_as_operational_forecast_dashboard(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("lobframe-metric-dashboard", text)
            self.assertIn("LOBFrame Metric Dashboard", text)
            self.assertIn("macro F1", text)
            self.assertIn("calibration", text)
            self.assertIn("turnover", text)
            self.assertIn("cost-adjusted PnL", text)
            self.assertIn("latency pass rate", text)

    def test_hlob_depth_persistence_study_is_promoted_as_depth_ablation_research(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("hlob-depth-persistence-study", text)
            self.assertIn("HLOB Depth Persistence Study", text)
            self.assertIn("deep-level persistence", text)
            self.assertIn("ablation report", text)
            self.assertIn("shallow", text)
            self.assertIn("deep", text)
            self.assertIn("persistence features", text)

    def test_lobench_representation_lab_is_promoted_as_transferability_research(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("lobench-representation-lab", text)
            self.assertIn("LOBench Representation Lab", text)
            self.assertIn("transferability", text)
            self.assertIn("downstream tasks", text)
            self.assertIn("representation family", text)
            self.assertIn("symbol split", text)
            self.assertIn("leakage-aware", text)

    def test_lob_bench_generative_evaluator_is_promoted_as_synthetic_lob_realism_research(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("lob-bench-generative-evaluator", text)
            self.assertIn("LOB-Bench Generative Evaluator", text)
            self.assertIn("realism metrics", text)
            self.assertIn("synthetic message-by-order data", text)
            self.assertIn("event mix", text)
            self.assertIn("interarrival", text)
            self.assertIn("order lifetime", text)
            self.assertIn("invariant checks", text)
            self.assertIn("public-safe", text)

    def test_abides_agent_strategy_zoo_is_promoted_as_market_simulation_research(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("abides-agent-strategy-zoo", text)
            self.assertIn("ABIDES Agent Strategy Zoo", text)
            self.assertIn("market maker", text)
            self.assertIn("momentum", text)
            self.assertIn("noise", text)
            self.assertIn("informed", text)
            self.assertIn("latency-arbitrage", text)
            self.assertIn("deterministic event simulation", text)
            self.assertIn("agent PnL", text)
            self.assertIn("inventory risk", text)
            self.assertIn("public-safe", text)

    def test_abides_latency_impact_study_is_promoted_as_market_infrastructure_research(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("abides-latency-impact-study", text)
            self.assertIn("ABIDES Latency Impact Study", text)
            self.assertIn("pairwise latency matrix", text)
            self.assertIn("execution-quality report", text)
            self.assertIn("latency advantage", text)
            self.assertIn("fill rate", text)
            self.assertIn("opportunity loss", text)
            self.assertIn("market infrastructure", text)
            self.assertIn("public-safe", text)

    def test_market_impact_validation_suite_is_promoted_as_execution_research(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("market-impact-validation-suite", text)
            self.assertIn("Market Impact Validation Suite", text)
            self.assertIn("temporary impact", text)
            self.assertIn("permanent impact", text)
            self.assertIn("implementation shortfall", text)
            self.assertIn("decay half-life", text)
            self.assertIn("ABIDES", text)
            self.assertIn("LOBFrame", text)
            self.assertIn("public-safe", text)

    def test_exchange_in_a_box_simulator_is_promoted_as_market_simulation_capstone(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("exchange-in-a-box-simulator", text)
            self.assertIn("Exchange-in-a-Box Simulator", text)
            self.assertIn(
                "unified exchange-in-a-box simulator tying market data, matching, auctions, latency, replay, and agent strategies together",
                text,
            )
            self.assertIn("shared event schema", text)
            self.assertIn("replay correctness", text)
            self.assertIn("matching fills", text)
            self.assertIn("auction clears", text)
            self.assertIn("public-safe", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_fpga_trading_reference_architecture_is_promoted_as_hardware_capstone(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("fpga-trading-reference-architecture", text)
            self.assertIn("FPGA Trading Reference Architecture", text)
            self.assertIn("public-safe consolidated FPGA trading reference architecture", text)
            self.assertIn("shared golden models", text)
            self.assertIn("verification fixtures", text)
            self.assertIn("packet parser", text)
            self.assertIn("order book", text)
            self.assertIn("risk gate", text)
            self.assertIn("latency budget", text)
            self.assertIn("sequence integrity", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_cross_universe_strategy_benchmark_is_promoted_as_strategy_research_capstone(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("cross-universe-strategy-benchmark", text)
            self.assertIn("Cross-Universe Strategy Benchmark", text)
            self.assertIn(
                "strategy research benchmark that runs common evaluation metrics across a defined universe and stores reports",
                text,
            )
            self.assertIn("walk-forward validation", text)
            self.assertIn("expectancy", text)
            self.assertIn("profit factor", text)
            self.assertIn("max drawdown", text)
            self.assertIn("universe coverage", text)
            self.assertIn("stored reports", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_cpse_market_control_room_is_promoted_as_cpse_capstone(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("cpse-market-control-room", text)
            self.assertIn("CPSE Market Control Room", text)
            self.assertIn("timing health", text)
            self.assertIn("telemetry integrity", text)
            self.assertIn("sensor fusion", text)
            self.assertIn("control loop stability", text)
            self.assertIn("operator dashboard", text)
            self.assertIn("degraded-mode", text)
            self.assertIn("not a production trading system", text)
            self.assertIn("not a deployed industrial control system", text)

    def test_strategy_overfitting_firewall_is_promoted_as_research_governance_capstone(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("strategy-overfitting-firewall", text)
            self.assertIn("Strategy Overfitting Firewall", text)
            self.assertIn("Deflated Sharpe", text)
            self.assertIn("Probability of backtest overfitting", text)
            self.assertIn("multiple-testing penalty", text)
            self.assertIn("walk-forward consistency", text)
            self.assertIn("parameter fragility", text)
            self.assertIn("human approval", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_fpga_orderbook_verification_suite_is_promoted_as_hardware_verification_capstone(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("fpga-orderbook-verification-suite", text)
            self.assertIn("FPGA Orderbook Verification Suite", text)
            self.assertIn("golden model replay", text)
            self.assertIn("sequence monotonicity", text)
            self.assertIn("crossed book", text)
            self.assertIn("risk gate", text)
            self.assertIn("coverage matrix", text)
            self.assertIn("RTL boundary", text)
            self.assertIn("SystemVerilog assertion", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_lob_alpha_decay_research_lab_is_promoted_as_microstructure_capstone(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("lob-alpha-decay-research-lab", text)
            self.assertIn("LOB Alpha Decay Research Lab", text)
            self.assertIn("signal half-life", text)
            self.assertIn("horizon decay", text)
            self.assertIn("cost-adjusted edge", text)
            self.assertIn("information coefficient", text)
            self.assertIn("turnover cost drag", text)
            self.assertIn("limit order book", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_exchange_microburst_simulator_is_promoted_as_market_infrastructure_capstone(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("exchange-microburst-simulator", text)
            self.assertIn("Exchange Microburst Simulator", text)
            self.assertIn("exchange microburst", text)
            self.assertIn("queue pressure", text)
            self.assertIn("tail latency", text)
            self.assertIn("packet drops", text)
            self.assertIn("capacity planning", text)
            self.assertIn("market infrastructure", text)
            self.assertIn("operator actions", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)

    def test_ouch_order_entry_gateway_simulator_is_promoted_as_order_entry_infrastructure(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("ouch-order-entry-gateway-simulator", text)
            self.assertIn("OUCH Order Entry Gateway Simulator", text)
            self.assertIn("OUCH-style order entry", text)
            self.assertIn("session sequencing", text)
            self.assertIn("risk rejection", text)
            self.assertIn("throttle pressure", text)
            self.assertIn("ack latency", text)
            self.assertIn("order gateway", text)
            self.assertIn("market infrastructure", text)
            self.assertIn("operator actions", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)
            self.assertIn("not a real OUCH implementation", text)

    def test_drop_copy_reconciliation_engine_is_promoted_as_post_trade_infrastructure(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("drop-copy-reconciliation-engine", text)
            self.assertIn("Drop-Copy Reconciliation Engine", text)
            self.assertIn("drop-copy reconciliation", text)
            self.assertIn("gateway decisions", text)
            self.assertIn("execution reports", text)
            self.assertIn("quantity mismatch", text)
            self.assertIn("sequence gaps", text)
            self.assertIn("duplicate execution report", text)
            self.assertIn("operator escalation", text)
            self.assertIn("market infrastructure", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)
            self.assertIn("not connected to a broker or exchange", text)

    def test_session_heartbeat_failover_monitor_is_promoted_as_session_liveness_infrastructure(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("session-heartbeat-failover-monitor", text)
            self.assertIn("Session Heartbeat Failover Monitor", text)
            self.assertIn("session heartbeat", text)
            self.assertIn("session liveness", text)
            self.assertIn("heartbeat gaps", text)
            self.assertIn("primary backup failover", text)
            self.assertIn("split-brain warnings", text)
            self.assertIn("failover SLA", text)
            self.assertIn("operator escalation", text)
            self.assertIn("market infrastructure", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)
            self.assertIn("not connected to a broker or exchange", text)

    def test_low_latency_trading_system_capstone_is_promoted_as_integrated_market_infrastructure(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("low-latency-trading-system-capstone", text)
            self.assertIn("Low-Latency Trading System Capstone", text)
            self.assertIn("market data feed handler", text)
            self.assertIn("sequence-gap detection", text)
            self.assertIn("limit order book reconstruction", text)
            self.assertIn("pre-trade risk gate", text)
            self.assertIn("order gateway", text)
            self.assertIn("drop-copy reconciliation", text)
            self.assertIn("session heartbeat failover", text)
            self.assertIn("deterministic replay", text)
            self.assertIn("latency budget", text)
            self.assertIn("integrated market infrastructure", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)
            self.assertIn("not connected to a broker or exchange", text)

    def test_fpga_smartnic_market_data_core_is_promoted_as_line_rate_hardware_infrastructure(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("fpga-smartnic-market-data-core", text)
            self.assertIn("FPGA SmartNIC Market Data Core", text)
            self.assertIn("SmartNIC flow table", text)
            self.assertIn("market data packet parser", text)
            self.assertIn("sequence-gap detection", text)
            self.assertIn("hardware timestamp normalization", text)
            self.assertIn("DMA descriptor budgeting", text)
            self.assertIn("AXI Stream boundary", text)
            self.assertIn("PCIe DMA boundary", text)
            self.assertIn("line-rate market infrastructure", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)
            self.assertIn("not connected to a broker or exchange", text)

    def test_market_data_feed_quality_gate_is_promoted_as_feed_trust_infrastructure(self) -> None:
        required_files = [
            ROOT / "README.md",
            ROOT / "PROJECTS.md",
            ROOT / "FLAGSHIP_SYSTEMS_MAP.md",
            ROOT / "ADVANCED_RESEARCH_BUILD_QUEUE.md",
            ROOT / "PORTFOLIO_EVIDENCE_LEDGER.md",
            ROOT / "ROLE_PACKETS.md",
        ]
        for path in required_files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("market-data-feed-quality-gate", text)
            self.assertIn("Market Data Feed Quality Gate", text)
            self.assertIn("feed quality gate", text)
            self.assertIn("sequence-gap detection", text)
            self.assertIn("timestamp sanity", text)
            self.assertIn("stale-feed detection", text)
            self.assertIn("crossed quote", text)
            self.assertIn("operator verdict", text)
            self.assertIn("public-safe", text)
            self.assertIn("not financial advice", text)
            self.assertIn("not a production trading system", text)
            self.assertIn("not connected to a broker or exchange", text)


if __name__ == "__main__":
    unittest.main()
