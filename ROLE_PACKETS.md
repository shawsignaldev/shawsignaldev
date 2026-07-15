# Role Packets

This file gives hiring teams a direct review path by role. The portfolio has broad coverage, so the useful signal is not "open everything." The useful signal is choosing the right few repositories, papers, and interview narratives for the role being evaluated.

## Hardware / FPGA Engineer

### Research papers to read first

- [FPGA Trading Architecture Whitepaper](papers/fpga-trading-architecture-whitepaper.md)
- [Market Data Infrastructure Whitepaper](papers/market-data-infrastructure-whitepaper.md)
- [Research Reading Map](RESEARCH_READING_MAP.md), especially FPGA HFT acceleration and Precision Time Protocol references

### Primary repositories

- `fpga-low-latency-market-data-engine`
- `fpga-nanosecond-orderbook-risk-gate`
- `fpga-udp-market-data-feed-handler`
- `fpga-latency-arbitration-crossbar`
- `fpga-pcie-market-data-dma-engine`
- `nasdaq-itch-parser-rtl-lab`
- `multicast-feed-arbitration-fpga`
- `ptp-nanosecond-timestamp-core`
- `uvm-lite-verification-harness`
- `fpga-cdc-metastability-lab`

### Interview narrative

The story is hardware/software co-design for market infrastructure. Python golden models clarify behavior, hardware-style modules express deterministic data paths, and tests document parser, sequencer, risk, and timing boundaries. The strongest signal is not an inflated latency claim. It is awareness of packet parsing, state transitions, timestamp discipline, backpressure, reset/CDC risk, formal-style verification, and honest operating limits.

### Risk and evidence boundary

Public repositories do not claim production exchange certification, board deployment, or final timing closure. They provide reviewable design slices, deterministic tests, and documentation that show the right engineering instincts for a 2027 graduate hardware role.

## Quant Developer

### Research papers to read first

- [Strategy Robustness Whitepaper](papers/strategy-robustness-whitepaper.md)
- [Market Data Infrastructure Whitepaper](papers/market-data-infrastructure-whitepaper.md)
- [Research Reading Map](RESEARCH_READING_MAP.md), especially DeepLOB, LOBFrame, ABIDES, and execution literature

### Primary repositories

- `agentic-strategy-search-lab`
- `walk-forward-auto-optimizer`
- `strategy-survivorship-analyzer`
- `backtest-result-warehouse`
- `realistic-fill-backtester`
- `spread-impact-slippage-estimator`
- `queue-reactive-orderbook-model`
- `lob-transformer-reproduction`
- `market-microstructure-research-platform`
- `llm-market-hypothesis-auditor`

### Interview narrative

The story is research governance rather than isolated indicators. Strategy candidates are generated, scored, compared, penalized for drawdown and fragility, and promoted only with evidence. The portfolio shows awareness that expectancy, profit factor, drawdown, costs, turnover, sample size, and regime behavior all matter. AI assistance is framed as hypothesis generation and auditing, not as an authority that bypasses human review.

### Risk and evidence boundary

The public portfolio does not claim a universal profitable strategy. It demonstrates the system a quant developer would build to make strategy claims testable, reject weak ideas quickly, and preserve reproducible evidence.

## Market Infrastructure Engineer

### Research papers to read first

- [Market Data Infrastructure Whitepaper](papers/market-data-infrastructure-whitepaper.md)
- [FPGA Trading Architecture Whitepaper](papers/fpga-trading-architecture-whitepaper.md)
- [Research Reading Map](RESEARCH_READING_MAP.md), especially ABIDES and low-latency market-data references

### Primary repositories

- `market-data-tickerplant-simulator`
- `event-sourced-market-feed-pipeline`
- `market-data-schema-contracts`
- `market-data-reconciliation-engine`
- `market-replay-hardware-harness`
- `fix-session-replay-analyzer`
- `opra-options-feed-normalizer`
- `market-halt-circuit-breaker-simulator`
- `execution-router-simulator`
- `hft-config-drift-detector`

### Interview narrative

The story is stateful infrastructure under uncertainty. A market-data system needs contracts, sequencing, replay, reconciliation, telemetry, and operating boundaries before analytics can be trusted. The repositories show how external events become validated internal state and how failures become visible to operators.

### Risk and evidence boundary

The portfolio uses deterministic public fixtures and sanitized examples. It does not include private feeds or production connectivity. That is intentional: employers can inspect the architecture without needing restricted data or credentials.

## Cyber-Physical Systems Engineer

### Research papers to read first

- [FPGA Trading Architecture Whitepaper](papers/fpga-trading-architecture-whitepaper.md)
- [Market Data Infrastructure Whitepaper](papers/market-data-infrastructure-whitepaper.md)
- [Research Reading Map](RESEARCH_READING_MAP.md), especially timing, PTP, distributed clock, and operator-system references

### Primary repositories

- `cpse-engineering-labs`
- `sensor-fusion-risk-monitor`
- `real-time-scheduler-lab`
- `industrial-control-sim-lab`
- `distributed-clock-sync-lab`
- `edge-device-health-monitor`
- `embedded-signal-processing-lab`
- `udp-telemetry-control-plane`
- `time-sync-attack-simulator`
- `operator-console-design-system`

### Interview narrative

The story is cyber-physical thinking applied to finance and engineered systems. External signals enter through sensors, networks, feeds, or operators. The system validates those signals, estimates state, manages timing, applies controls, and reports failures. This connects CPSE coursework to market infrastructure without pretending that trading systems and embedded systems are identical.

### Risk and evidence boundary

The CPSE repositories are public educational systems with sanitized data. They are designed to show breadth across sensing, networking, timing, control, and operator visibility.

## AI / Software Engineer

### Research papers to read first

- [Strategy Robustness Whitepaper](papers/strategy-robustness-whitepaper.md)
- [Market Data Infrastructure Whitepaper](papers/market-data-infrastructure-whitepaper.md)
- [Research Reading Map](RESEARCH_READING_MAP.md), especially paper-to-code, model risk, LOB forecasting, and evidence-gated research

### Primary repositories

- `llm-market-hypothesis-auditor`
- `paper-to-alpha-reproduction-suite`
- `paper-to-code-research-agent`
- `repo-context-engineer`
- `ai-runbook-operator`
- `prompt-eval-lab`
- `ai-dashboard-commentary-engine`
- `model-risk-validation-lab`
- `research-lineage-ledger`
- `m2m-learning-systems`

### Interview narrative

The story is practical AI tooling with guardrails. The portfolio uses AI as a workflow accelerator for research briefs, hypotheses, reports, and audits. It keeps human approval and evidence gates explicit. This is the right posture for applied AI in finance-adjacent systems: useful automation, clear limits, and reproducible artifacts.

### Risk and evidence boundary

The repositories avoid live financial decision automation and sensitive data. They demonstrate how to build AI-assisted systems that remain inspectable, testable, and bounded.

## How To Use This File

For a fast screen, read the role section, open the first three repositories, and skim the matching whitepaper. For a deeper screen, follow the evidence map into tests, docs, and CI results. The intended signal is breadth with organization: many repositories, but each role has a coherent path through them.

