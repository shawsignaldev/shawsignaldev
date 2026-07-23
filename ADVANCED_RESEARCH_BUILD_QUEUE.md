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
| Market simulation | market-impact-validation-suite | Quant developer | ABIDES, LOBFrame | Temporary and permanent impact estimates with limitations |

## Wave 3: Hardware Acceleration and Formal Verification

| Flagship system | Repository concept | Role signal | Paper anchor | Proof required before promotion |
| --- | --- | --- | --- | --- |
| Low-latency FPGA datapath | itch-to-risk-full-pipeline | FPGA systems | High Frequency Trading Acceleration using FPGAs | End-to-end parse, book update, risk approval, and replay trace |
| Low-latency FPGA datapath | pcie-dma-descriptor-verification | Hardware engineering | High Frequency Trading Acceleration using FPGAs | Descriptor validity, wraparound, burst sizing, and completion accounting |
| Low-latency FPGA datapath | axi-stream-backpressure-lab | FPGA verification | High Frequency Trading Acceleration using FPGAs | Ready/valid stall coverage and no-loss packet tests |
| Low-latency FPGA datapath | ptp-fault-injection-core | Timing systems | Precision Time Protocol references | Offset attack, drift, recovery, and operator alert scenarios |
| Hardware AI acceleration | lobin-style-in-network-inference | SmartNIC/P4 | LOBIN | In-network feature extraction model and latency/accuracy tradeoff note |
| Hardware AI acceleration | quantized-lob-inference-fpga | FPGA ML | DeepLOB, LOBIN | Fixed-point feature pipeline with error bounds and throughput estimate |
| Hardware AI acceleration | hbm-lob-layout-benchmark | Memory systems | LOBFrame | Bank conflict, row locality, throughput, and storage-layout report |
| Hardware AI acceleration | systolic-lob-feature-engine | Hardware acceleration | DeepLOB | Matrix/vector feature projection and cycle estimate with limitations |

## Wave 4: Options and Intraday Trading Research

| Flagship system | Repository concept | Role signal | Paper anchor | Proof required before promotion |
| --- | --- | --- | --- | --- |
| Options research | zero-dte-opening-drive-study | Options strategy research | Strategy Robustness Whitepaper | First 5/15/45 minute windows, risk sizing, slippage, and walk-forward report |
| Options research | gamma-vwap-confluence-lab | Options microstructure | Strategy Robustness Whitepaper | Gamma level, VWAP, volume pressure, and failed-breakout classification |
| Options research | weekly-contract-selector-benchmark | Options systems | Strategy Robustness Whitepaper | Same-day versus nearest-weekly comparison with liquidity filters |
| Options research | intraday-iv-expansion-monitor | Volatility research | Rough volatility and IV surface notes | IV expansion/compression labels and signal-quality report |
| Options research | open-interest-liquidity-regime-lab | Options data | Strategy Robustness Whitepaper | OI, spread, volume, and contract survivability scoring |
| Quant research | first-hour-momentum-regime-lab | Quant developer | LOBFrame | Open, midday, and close regime splits with expectancy and drawdown |
| Quant research | session-high-low-breakout-validator | Trading systems | Strategy Robustness Whitepaper | Premarket, regular session, and close-range breakout validation |
| Quant research | risk-adjusted-trade-sizing-engine | Risk systems | Strategy Robustness Whitepaper | Kelly-capped, drawdown-capped, volatility-scaled sizing report |

## Wave 5: Cyber-Physical and Operator Systems

| Flagship system | Repository concept | Role signal | Paper anchor | Proof required before promotion |
| --- | --- | --- | --- | --- |
| CPSE systems | plant-market-control-analogy-lab | Cyber-physical systems | Precision Time Protocol references | Sensor, estimator, controller, actuator, and operator intervention model |
| CPSE systems | distributed-clock-health-dashboard | Timing systems | Precision Time Protocol references | Clock offset, drift, jitter, and degraded-state visualization |
| CPSE systems | real-time-alert-scheduler | Embedded/software systems | Real-time scheduling references | Deadline, priority inversion, dropped alert, and recovery checks |
| CPSE systems | udp-control-plane-safety-monitor | Networked systems | Precision Time Protocol references | Packet loss, sequence gap, stale command, and operator override behavior |
| CPSE systems | sensor-fusion-market-risk-bridge | CPSE/quant overlap | Kalman filtering and state estimation notes | Noisy sensor analogy connected to noisy market state estimation |
| CPSE systems | timing-attack-incident-runbook | Security operations | Precision Time Protocol references | Attack, detection, severity, mitigation, and postmortem template |
| Operator tooling | evidence-ledger-dashboard | Software engineering | Model-risk and evidence-gating notes | Capability-to-proof dashboard with missing-evidence warnings |
| Operator tooling | recruiter-review-path-generator | Portfolio systems | Internal role packet docs | Role-specific artifact path generated from project metadata |

## Promotion Rules

The queue is useful only if each project earns promotion. A project stays in backlog until it has tests, CI, clear docs, public-safe examples, and a measured or explicitly bounded claim. The best projects should then be reflected in `FLAGSHIP_SYSTEMS_MAP.md`, `ROLE_PACKETS.md`, `PORTFOLIO_EVIDENCE_LEDGER.md`, and the public site.
