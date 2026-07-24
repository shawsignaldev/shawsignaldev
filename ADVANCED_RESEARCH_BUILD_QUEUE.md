# Advanced Research Build Queue

## Selection standard

This is not count-only expansion. A repository only belongs in this queue if it can strengthen a target role narrative, connect to a flagship system, cite a paper anchor or rigorous engineering reference, and define proof required before promotion.

The standard for a promoted project is:

- It has a README, architecture note, limitations, tests, and CI.
- It has deterministic public fixtures or synthetic data.
- It states what is implemented and what is not implemented.
- It maps to a target role: hardware/FPGA, quant developer, market infrastructure, cyber-physical systems, or AI/software engineering.
- It makes one narrow technical claim that can be verified from public artifacts.

## Wave 1: Flagship Hardening

| Flagship system | Repository concept | Role signal | Paper anchor | Proof required before promotion |
| --- | --- | --- | --- | --- |
| Low-latency FPGA datapath | Shared Market Packet Fixtures (`shared-market-packet-fixtures`) | Market infrastructure | High Frequency Trading Acceleration using FPGAs | Shared event schema, parser fixtures, tests across at least three repos |
| Low-latency FPGA datapath | FPGA Orderflow Formal Properties (`fpga-orderflow-formal-properties`) | FPGA verification | High Frequency Trading Acceleration using FPGAs | Safety and liveness properties for sequence, replay, exposure caps, halt latch behavior, valid side encoding, bounded acknowledgement latency, and coverage matrix review |
| LOB intelligence | LOB Benchmark Report Generator (`lob-benchmark-report-generator`) | Quant developer | DeepLOB, LOBFrame | Reproducible report comparing baseline, queue, and deep-feature metrics with cost-adjusted PnL, Brier calibration, latency pass rates, and Markdown reports |
| LOB intelligence | Market Sim Scenario Library (`market-sim-scenario-library`) | Quant research | ABIDES | Stress, halt, auction, latency, and liquidity-drought scenarios with deterministic seeds, event traces, latency matrices, CSV export, and Markdown reports |
| Options research | Synthetic Options Chain Generator (`synthetic-options-chain-generator`) | Options research | Strategy Robustness Whitepaper | Generated chain with IV skew, Greeks, bid/ask spread, volume, open interest, expiry checks, liquidity scores, and target-delta selection |
| Options research | Option Replay Report Engine (`option-replay-report-engine`) | Quant developer | Strategy Robustness Whitepaper | Per-contract PnL attribution separating contract PnL, fees, liquidity cost, theta drag, volatility contribution, reward-to-risk, quality scoring, and Promote/Watchlist/Reject verdicts |
| AI research factory | Research Queue State Machine (`research-queue-state-machine`) | AI/software engineering | Model-risk and evidence-gating notes | evidence-gated proposed, tested, challenged, promoted, watchlisted, and rejected state transitions with missing-evidence checks, audit trails, Markdown reports, and human approval gates |
| CPSE systems | Degraded Mode Operator Console (`degraded-mode-operator-console`) | Cyber-physical systems | Precision Time Protocol references | Normal, degraded, fault, operator-acknowledged, and recovery states with safe mode operator cards, operator acknowledgement gates, recovery checks, audit trails, and Markdown reports |

## Wave 2: Paper Reproduction and Benchmarking

| Flagship system | Repository concept | Role signal | Paper anchor | Proof required before promotion |
| --- | --- | --- | --- | --- |
| LOB intelligence | DeepLOB Leakage Test Harness (`deeplob-leakage-test-harness`) | Quant ML | DeepLOB | Public-safe synthetic LOB fixtures, tensor shape checks, chronological split, label horizon audit, lookahead leakage detection, baseline metrics, and Markdown reports |
| LOB intelligence | LOBFrame Metric Dashboard (`lobframe-metric-dashboard`) | Quant developer | LOBFrame | Accuracy, macro F1, Brier score, calibration, turnover, cost-adjusted PnL, latency pass rate, explicit promotion gates, and Markdown reports |
| LOB intelligence | HLOB Depth Persistence Study (`hlob-depth-persistence-study`) | Quant research | HLOB | deep-level persistence features, public-safe depth fixtures, shallow-versus-deep ablation report, horizon persistence scores, and explicit limitations |
| LOB intelligence | LOBench Representation Lab (`lobench-representation-lab`) | Quant ML | LOBench | representation family comparisons, public-safe symbol split transferability, leakage-aware downstream tasks, transfer matrix scoring, and Markdown reports |
| LOB intelligence | LOB-Bench Generative Evaluator (`lob-bench-generative-evaluator`) | AI research | LOB-Bench | realism metrics for public-safe synthetic message-by-order data, event mix, interarrival, order lifetime, invariant checks, generator ranking, and Markdown reports |
| Market simulation | ABIDES Agent Strategy Zoo (`abides-agent-strategy-zoo`) | Quant simulation | ABIDES | public-safe deterministic event simulation for market maker, momentum, noise, informed, and latency-arbitrage agents with agent PnL, inventory risk, fill counts, latency, and Markdown reports |
| Market simulation | ABIDES Latency Impact Study (`abides-latency-impact-study`) | Market infrastructure | ABIDES | public-safe pairwise latency matrix, latency advantage, fill rate, opportunity loss, slippage, and execution-quality report |
| Market simulation | Market Impact Validation Suite (`market-impact-validation-suite`) | Quant developer | ABIDES, LOBFrame | public-safe temporary impact, permanent impact, implementation shortfall, decay half-life, child-order scoring, and limitations reporting |

## Wave 3: Hardware Acceleration and Formal Verification

| Flagship system | Repository concept | Role signal | Paper anchor | Proof required before promotion |
| --- | --- | --- | --- | --- |
| Low-latency FPGA datapath | ITCH To Risk Full Pipeline (`itch-to-risk-full-pipeline`) | FPGA systems | High Frequency Trading Acceleration using FPGAs | FPGA-oriented public-safe end-to-end parse, book update, risk approval, and replay trace |
| Low-latency FPGA datapath | PCIe DMA Descriptor Verification (`pcie-dma-descriptor-verification`) | Hardware engineering | High Frequency Trading Acceleration using FPGAs | FPGA and DMA public-safe descriptor validity, wraparound, burst sizing, completion accounting, and Markdown report evidence |
| Low-latency FPGA datapath | AXI Stream Backpressure Lab (`axi-stream-backpressure-lab`) | FPGA verification | High Frequency Trading Acceleration using FPGAs | FPGA public-safe ready/valid stall coverage, skid buffer stress, packet-boundary recovery, and no-loss packet tests |
| Low-latency FPGA datapath | PTP Fault Injection Core (`ptp-fault-injection-core`) | Timing systems | Precision Time Protocol references | public-safe Offset attack, Drift injection, Recovery, and Operator alert scenarios for cyber-physical timing resilience |
| Hardware AI acceleration | LOBIN-Style In-Network Inference (`lobin-style-in-network-inference`) | SmartNIC/P4 | LOBIN | SmartNIC/P4-style public-safe fixed-point order-book feature scoring with latency/accuracy tradeoff reporting; not a production trading system |
| Hardware AI acceleration | Quantized LOB Inference FPGA (`quantized-lob-inference-fpga`) | FPGA ML | DeepLOB, LOBIN | public-safe fixed-point LOB inference with error bounds and throughput estimate; not a production trading system |
| Hardware AI acceleration | HBM LOB Layout Benchmark (`hbm-lob-layout-benchmark`) | Memory systems | LOBFrame | public-safe HBM storage-layout report with bank conflict, row locality, and throughput evidence; not a production trading system |
| Hardware AI acceleration | Systolic LOB Feature Engine (`systolic-lob-feature-engine`) | Hardware acceleration | DeepLOB | public-safe matrix/vector feature projection with cycle estimate and limitations; not a production trading system |

## Wave 4: Options and Intraday Trading Research

| Flagship system | Repository concept | Role signal | Paper anchor | Proof required before promotion |
| --- | --- | --- | --- | --- |
| Options research | Zero-DTE Opening Drive Study (`zero-dte-opening-drive-study`) | Options strategy research | Strategy Robustness Whitepaper | public-safe First 5/15/45 minute windows, risk sizing, slippage, and walk-forward report evidence; not financial advice |
| Options research | Gamma/VWAP Confluence Lab (`gamma-vwap-confluence-lab`) | Options microstructure | Strategy Robustness Whitepaper | public-safe gamma level, VWAP, volume pressure, and failed-breakout classification evidence; not financial advice and not a production trading system |
| Options research | Weekly Contract Selector Benchmark (`weekly-contract-selector-benchmark`) | Options systems | Strategy Robustness Whitepaper | public-safe Same-day versus nearest-weekly comparison, liquidity filters, target-delta selection, and spread control; not financial advice and not a production trading system |
| Options research | Intraday IV Expansion Monitor (`intraday-iv-expansion-monitor`) | Volatility research | Rough volatility and IV surface notes | public-safe IV expansion/compression labels, volatility regime, spread control, and signal-quality report evidence; not financial advice and not a production trading system |
| Options research | Open Interest Liquidity Regime Lab (`open-interest-liquidity-regime-lab`) | Options data | Strategy Robustness Whitepaper | public-safe OI, spread, volume, and contract survivability scoring with open interest growth and liquidity regime evidence; not financial advice and not a production trading system |
| Quant research | First-Hour Momentum Regime Lab (`first-hour-momentum-regime-lab`) | Quant developer | LOBFrame | public-safe Open, midday, and close regime splits with expectancy, drawdown, and volume confirmation evidence; not financial advice and not a production trading system |
| Quant research | Session High/Low Breakout Validator (`session-high-low-breakout-validator`) | Trading systems | Strategy Robustness Whitepaper | public-safe Premarket, regular session, and close-range breakout validation with close-location value, VWAP distance, and volume pressure evidence; not financial advice and not a production trading system |
| Quant research | Risk-Adjusted Trade Sizing Engine (`risk-adjusted-trade-sizing-engine`) | Risk systems | Strategy Robustness Whitepaper | public-safe Kelly-capped, drawdown-capped, volatility-scaled sizing report with risk budget, position debit, and dollars at risk evidence |

## Wave 5: Cyber-Physical and Operator Systems

| Flagship system | Repository concept | Role signal | Paper anchor | Proof required before promotion |
| --- | --- | --- | --- | --- |
| CPSE systems | Plant Market Control Analogy Lab (`plant-market-control-analogy-lab`) | Cyber-physical systems | Precision Time Protocol references | public-safe Sensor, estimator, controller, actuator, and operator intervention model with sensor health, control error, and operator intervention evidence; not financial advice and not a production trading system |
| CPSE systems | Distributed Clock Health Dashboard (`distributed-clock-health-dashboard`) | Timing systems | Precision Time Protocol references | public-safe Clock offset, drift, jitter, and degraded-state visualization with fleet health score, worst-node ranking, and operator action evidence; not financial advice and not a production trading system |
| CPSE systems | real-time-alert-scheduler | Embedded/software systems | Real-time scheduling references | Deadline, priority inversion, dropped alert, and recovery checks |
| CPSE systems | udp-control-plane-safety-monitor | Networked systems | Precision Time Protocol references | Packet loss, sequence gap, stale command, and operator override behavior |
| CPSE systems | sensor-fusion-market-risk-bridge | CPSE/quant overlap | Kalman filtering and state estimation notes | Noisy sensor analogy connected to noisy market state estimation |
| CPSE systems | timing-attack-incident-runbook | Security operations | Precision Time Protocol references | Attack, detection, severity, mitigation, and postmortem template |
| Operator tooling | evidence-ledger-dashboard | Software engineering | Model-risk and evidence-gating notes | Capability-to-proof dashboard with missing-evidence warnings |
| Operator tooling | recruiter-review-path-generator | Portfolio systems | Internal role packet docs | Role-specific artifact path generated from project metadata |

## Promotion Rules

The queue is useful only if each project earns promotion. A project stays in backlog until it has tests, CI, clear docs, public-safe examples, and a measured or explicitly bounded claim. The best projects should then be reflected in `FLAGSHIP_SYSTEMS_MAP.md`, `ROLE_PACKETS.md`, `PORTFOLIO_EVIDENCE_LEDGER.md`, and the public site.
