# Flagship Systems Map

## Why this exists

The portfolio is meant to read as a set of flagship research programs, not isolated repo count. The useful signal for employers is that each repository belongs to a larger technical thesis with tests, public documentation, reproducibility boundaries, and a clear review path.

This map groups the strongest public repositories into five systems that match the roles I am targeting for 2027: hardware and FPGA engineering, quant development, market infrastructure, cyber-physical systems, and AI/software engineering.

## Flagship 1: Low-Latency Market Data and FPGA Trading Datapath

### Primary thesis

Market data systems need deterministic parsing, sequencing, timestamping, buffering, pre-trade controls, and replay before speed claims are meaningful.

### Core repositories

- `fpga-low-latency-market-data-engine`
- `fpga-nanosecond-orderbook-risk-gate`
- `itch-to-risk-full-pipeline` (ITCH To Risk Full Pipeline: FPGA-oriented public-safe end-to-end parse, book update, risk approval, and replay trace)
- `fpga-udp-market-data-feed-handler`
- `fpga-latency-arbitration-crossbar`
- `axi-stream-backpressure-lab` (AXI Stream Backpressure Lab: FPGA public-safe ready/valid stall coverage, skid buffer stress, packet-boundary recovery, and no-loss packet tests)
- `fpga-pcie-market-data-dma-engine`
- `shared-market-packet-fixtures` (Shared Market Packet Fixtures)
- `fpga-orderflow-formal-properties` (FPGA Orderflow Formal Properties: halt latch and bounded acknowledgement latency property pack)
- `pcie-dma-descriptor-verification` (PCIe DMA Descriptor Verification: FPGA and DMA public-safe descriptor validity, wraparound, burst sizing, and completion accounting)
- `nasdaq-itch-parser-rtl-lab`
- `multicast-feed-arbitration-fpga`
- `lobin-style-in-network-inference` (LOBIN-Style In-Network Inference: SmartNIC/P4-style public-safe fixed-point order-book feature scoring with latency/accuracy tradeoff reporting; not a production trading system)
- `quantized-lob-inference-fpga` (Quantized LOB Inference FPGA: DeepLOB and LOBIN anchored public-safe fixed-point LOB inference with error bounds and throughput estimate; not a production trading system)
- `ptp-nanosecond-timestamp-core`
- `axi-lite-register-map-generator`
- `uvm-lite-verification-harness`

### Paper-backed foundation

- High Frequency Trading Acceleration using FPGAs: https://people.ucsc.edu/~hlitz/papers/hft_fpga.pdf
- IEEE 1588 / Precision Time Protocol references from `RESEARCH_READING_MAP.md`

### Proof artifacts reviewers should inspect

- Python golden models paired with RTL-style modules.
- Self-checking tests and CI evidence.
- Explicit honest boundaries around board deployment, timing closure, and production certification.
- The FPGA Trading Architecture Whitepaper.

### Next research upgrades

- Add cocotb-style verification examples where toolchain access is available.
- Add a shared packet fixture format across ITCH, UDP, DMA, risk, and replay repositories.
- Add formal-style property documentation for ordering, backpressure, kill switch, halt latch, bounded acknowledgement latency, and sequence-gap invariants.

## Flagship 2: Limit Order Book Intelligence and Market Simulation

### Primary thesis

Useful quant ML requires market microstructure realism: limit order book features, queue position, latency, exchange state, fill assumptions, costs, and walk-forward evaluation.

### Core repositories

- `market-microstructure-research-platform`
- `deeplob-reproduction-lab`
- `deeplob-leakage-test-harness` (DeepLOB Leakage Test Harness: benchmark hygiene with chronological split, label horizon audit, lookahead leakage detection, tensor shape checks, and baseline metrics)
- `hlob-depth-persistence-study` (HLOB Depth Persistence Study: deep-level persistence features, shallow-versus-deep ablation report, and horizon persistence scores)
- `lobench-representation-lab` (LOBench Representation Lab: representation family comparisons, symbol split transferability, downstream tasks, leakage-aware reporting, and transfer matrix scoring)
- `lob-bench-generative-evaluator` (LOB-Bench Generative Evaluator: realism metrics for public-safe synthetic message-by-order data, event mix, interarrival, order lifetime, invariant checks, and generator ranking)
- `hlob-feature-research`
- `lobframe-benchmark-suite`
- `lobframe-metric-dashboard` (LOBFrame Metric Dashboard: operational forecast dashboard with macro F1, calibration, turnover, cost-adjusted PnL, latency pass rate, and promotion gates)
- `lob-benchmark-report-generator` (LOB Benchmark Report Generator: cost-adjusted, Brier, latency pass, and Markdown reports)
- `abides-market-sim-lab`
- `abides-agent-strategy-zoo` (ABIDES Agent Strategy Zoo: public-safe deterministic event simulation for market maker, momentum, noise, informed, and latency-arbitrage agents with agent PnL and inventory risk)
- `abides-latency-impact-study` (ABIDES Latency Impact Study: market infrastructure pairwise latency matrix, latency advantage, fill rate, opportunity loss, and execution-quality report)
- `market-impact-validation-suite` (Market Impact Validation Suite: ABIDES and LOBFrame anchored public-safe execution research with temporary impact, permanent impact, implementation shortfall, decay half-life, child-order scoring, and limitations reporting)
- `market-sim-scenario-library` (Market Sim Scenario Library: ABIDES-style stress, halt, auction, latency, and liquidity-drought fixtures with deterministic seeds)
- `queue-reactive-orderbook-model`
- `lob-transformer-reproduction`
- `realistic-fill-backtester`
- `market-impact-propagator-lab`
- `backtest-result-warehouse`
- `shared-market-packet-fixtures` (Shared Market Packet Fixtures)

### Paper-backed foundation

- DeepLOB: https://arxiv.org/abs/1808.03668
- ABIDES: https://arxiv.org/abs/1904.12066
- LOBFrame: https://arxiv.org/abs/2403.09267
- HLOB: https://arxiv.org/html/2405.18938v3

### Proof artifacts reviewers should inspect

- LOB feature transforms and leakage-safe label framing.
- Discrete-event exchange sequencing and latency-aware ordering.
- Fill and slippage models that prevent inflated backtest claims.
- Strategy robustness and market data whitepapers.

### Next research upgrades

- Create a shared benchmark report comparing simple baselines, DeepLOB-style features, transformer-style features, and queue-reactive execution assumptions.
- Add synthetic distribution-shift scenarios for stress, halts, auctions, and liquidity droughts.
- Add feature-store lineage so every model input can be traced to event-time data.

## Flagship 3: Options Microstructure and 0DTE Research OS

### Primary thesis

Short-dated options research needs contract selection, liquidity checks, gamma and IV context, estimated Greeks, risk sizing, and explicit uncertainty when full historical chain data is unavailable.

### Core repositories

- `zero-dte-options-backtester`
- `options-ev-estimator`
- `synthetic-options-chain-generator` (Synthetic Options Chain Generator: IV skew, Greeks, open interest, and target-delta fixtures)
- `option-replay-report-engine` (Option Replay Report Engine: per-contract PnL attribution across fees, liquidity cost, theta drag, volatility contribution, reward-to-risk, and promotion verdicts)
- `gamma-exposure-estimator`
- `dealer-gamma-feedback-lab`
- `options-flow-anomaly-detector`
- `iv-surface-microstructure-lab`
- `contract-routing-risk-engine`
- `options-liquidity-scanner`
- `options-pnl-attribution-engine`
- `earnings-iv-crush-model`

### Paper-backed foundation

- Volatility surface, jump diffusion, rough volatility, and option PnL attribution references from `RESEARCH_READING_MAP.md`.
- Internal Strategy Robustness Whitepaper for promotion gates and options-data assumptions.

### Proof artifacts reviewers should inspect

- Black-Scholes style utilities and estimated option PnL decomposition.
- Contract filters for expiry, delta, spread, volume, and risk.
- Separate treatment of same-day and nearest-weekly assumptions.
- Honest distinction between historical estimate and real chain snapshot.

### Next research upgrades

- Add a public synthetic options-chain generator calibrated to stock move, IV, delta, theta, and spread assumptions.
- Add per-contract replay reports that separate entry edge from liquidity and decay drag.
- Add paper-trading journal exports that never imply live brokerage automation.

## Flagship 4: AI-Governed Quant Research Factory

### Primary thesis

AI should accelerate hypothesis generation, literature review, experiment planning, and report writing, while promotion remains evidence-gated and human-approved.

### Core repositories

- `agentic-strategy-search-lab`
- `research-queue-state-machine` (Research Queue State Machine: evidence-gated proposed, tested, challenged, promoted, watchlisted, and rejected research workflow with human approval gates)
- `ai-quant-research-os`
- `agentic-quant-researcher`
- `paper-to-alpha-reproduction-suite`
- `paper-to-code-research-agent`
- `llm-market-hypothesis-auditor`
- `research-lineage-ledger`
- `reproducible-experiment-registry`
- `model-risk-validation-lab`
- `prompt-eval-lab`

### Paper-backed foundation

- DeepLOB, ABIDES, LOBFrame, and model-risk material linked from `RESEARCH_READING_MAP.md`.
- Strategy Robustness Whitepaper for scoring, promotion gates, walk-forward validation, and limitations.

### Proof artifacts reviewers should inspect

- Evidence gates and missing-evidence checks.
- Markdown reports with human-readable verdicts.
- Experiment fingerprints and lineage records.
- Prompt and hypothesis evaluation boundaries.

### Next research upgrades

- Add a unified research queue where each idea moves through proposed, tested, challenged, promoted, watchlisted, or rejected states.
- Add a reviewer mode that explains why a strategy failed before suggesting variants.
- Add benchmark fixtures that show the same candidate evaluated across symbols, regimes, and timeframes.

## Flagship 5: Cyber-Physical Timing, Control, and Operator Systems

### Primary thesis

Trading infrastructure and cyber-physical systems share the same engineering concerns: timing, observability, control loops, failure detection, operator visibility, and safe actuation boundaries.

### Core repositories

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
- `degraded-mode-operator-console` (Degraded Mode Operator Console: normal, degraded, fault, operator-acknowledged, and recovery states with Precision Time Protocol context, safe mode operator cards, operator acknowledgement gates, and recovery checks)
- `ptp-fault-injection-core` (PTP Fault Injection Core: Precision Time Protocol public-safe Offset attack, Drift injection, Recovery, and Operator alert scenarios for cyber-physical timing resilience)

### Paper-backed foundation

- Precision Time Protocol and distributed timing references from `RESEARCH_READING_MAP.md`.
- FPGA Trading Architecture Whitepaper for timing, state, and operator boundary framing.

### Proof artifacts reviewers should inspect

- Timing and scheduling checks.
- Sensor/network examples with public-safe fixtures.
- Operator runbooks and status surfaces.
- Security and threat-model notes around timing manipulation.

### Next research upgrades

- Add a simulated plant plus market-data control analogy showing sensor input, estimator, controller, actuator, and operator intervention.
- Promote timing-fault injection reports and recovery-path documentation across `ptp-fault-injection-core` and related operator dashboards.
- Extend degraded-mode dashboards from operator cards into richer live timing and recovery-path views.

## Portfolio-Level Standards

- Every flagship system should have at least one whitepaper or technical note.
- Every public claim should map to a repository, test, CI run, screenshot, or explicit limitation.
- Every research repo should distinguish implemented evidence from future roadmap.
- Every finance-adjacent repo should avoid private credentials, account data, and live-trading promises.
- Every recruiter path should reduce noise by pointing to the few best artifacts for that role.
