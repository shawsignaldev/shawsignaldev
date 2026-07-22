# Portfolio Evidence Ledger

This ledger maps portfolio claims to public proof artifacts. It is designed for recruiters, hiring managers, and engineers who need a fast way to separate demonstrated evidence from roadmap ambition.

## Evidence Matrix

| Capability | Public proof artifacts | Validation method | Honest boundary |
| --- | --- | --- | --- |
| Low-latency market data | `fpga-low-latency-market-data-engine`, `fpga-udp-market-data-feed-handler`, `nasdaq-itch-parser-rtl-lab`, `market-data-tickerplant-simulator`, [Market Data Infrastructure Whitepaper](papers/market-data-infrastructure-whitepaper.md) | Parser/state tests, Python golden models, GitHub Actions, system-design docs, validation evidence, reading map | Public examples are reference models and design slices, not production exchange-certified feed handlers. |
| Strategy robustness | `agentic-strategy-search-lab`, `walk-forward-auto-optimizer`, `strategy-survivorship-analyzer`, `realistic-fill-backtester`, `backtest-result-warehouse`, [Strategy Robustness Whitepaper](papers/strategy-robustness-whitepaper.md) | Walk-forward splits, promotion/reject logic, expectancy/drawdown/profit-factor scoring, result warehouse summaries, green CI | The portfolio does not claim a universal profitable strategy or live execution edge. It proves research-process discipline. |
| FPGA and hardware verification | `fpga-nanosecond-orderbook-risk-gate`, `fpga-latency-arbitration-crossbar`, `fpga-pcie-market-data-dma-engine`, `uvm-lite-verification-harness`, `fpga-cdc-metastability-lab`, [FPGA Trading Architecture Whitepaper](papers/fpga-trading-architecture-whitepaper.md) | Self-checking tests, golden-model comparison, RTL-boundary docs, verification plans, role packets | Public repos do not claim timing closure, board deployment, or proprietary toolchain results unless specifically documented. |
| Market infrastructure operations | `event-sourced-market-feed-pipeline`, `market-data-schema-contracts`, `market-data-reconciliation-engine`, `fix-session-replay-analyzer`, `hft-config-drift-detector`, `alert-event-bus-adapters` | Deterministic replay, schema checks, reconciliation verdicts, alert normalization tests, public docs | Public fixtures are sanitized and deterministic; they do not include private feeds or operational credentials. |
| Cyber-physical systems | `cpse-engineering-labs`, `sensor-fusion-risk-monitor`, `real-time-scheduler-lab`, `industrial-control-sim-lab`, `distributed-clock-sync-lab`, `edge-device-health-monitor` | Sensor/network examples, timing calculations, scheduling checks, control-simulation summaries, documented safety boundaries | CPSE examples show educational engineering breadth rather than deployed industrial control systems. |
| AI research governance | `llm-market-hypothesis-auditor`, `paper-to-alpha-reproduction-suite`, `paper-to-code-research-agent`, `prompt-eval-lab`, `model-risk-validation-lab`, `research-lineage-ledger` | Evidence gates, prompt-eval tests, missing-evidence checks, research lineage, human approval boundaries | AI tools support research workflow and auditing; they do not replace human approval or make autonomous financial decisions. |
| Recruiter-facing organization | [ROLE_PACKETS.md](ROLE_PACKETS.md), [RECRUITER_PACKET.md](RECRUITER_PACKET.md), [RESEARCH_READING_MAP.md](RESEARCH_READING_MAP.md), [Technical Depth Matrix](TECHNICAL_DEPTH_MATRIX.md), live portfolio site | Profile CI, site static checks, role packets, whitepapers, reading map, public Pages deployment | Organization improves reviewability but does not itself prove depth; it points reviewers to artifacts that do. |

## Evidence Standards

Every strong repository should provide:

- A clear problem statement.
- A deterministic example or safe fixture.
- Tests or structure checks in CI.
- Documentation that distinguishes implemented behavior from roadmap items.
- Security and public-data boundaries.
- A recruiter-readable explanation of why the project matters.

## What Counts As Strong Evidence

Strong evidence includes executable tests, CI results, source files, architecture notes, validation reports, whitepapers, role packets, and the research reading map. Weak evidence includes vague claims, unsupported performance numbers, unlinked project names, or broad statements without a runnable or inspectable artifact.

## What Still Needs More Depth

The portfolio is now broad and organized, but the strongest future gains come from integration:

1. A unified exchange-in-a-box simulator tying market data, matching, auctions, latency, replay, and agent strategies together.
2. A consolidated FPGA trading reference architecture with shared golden models and verification fixtures.
3. A strategy research benchmark that runs common evaluation metrics across a defined universe and stores reports.
4. A CPSE capstone that connects timing, telemetry, sensors, control loops, and operator dashboards.

Those are the natural next proof layers after the current 200-repository portfolio, whitepapers, reading map, and role packets.

