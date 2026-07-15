# Research Reading Map

This map connects the public portfolio to serious research literature and engineering references. It is not meant to claim that every repository fully reproduces every paper. It is a reviewer guide: what the paper contributes, which repositories show related implementation evidence, and what the honest next step would be.

## Market Microstructure and Limit Order Books

| Source | Why It Matters | Evidence-bearing repositories | Next extension |
| --- | --- | --- | --- |
| DeepLOB: Deep Convolutional Neural Networks for Limit Order Books, https://arxiv.org/abs/1808.03668 | Establishes CNN/LSTM-style representation learning for limit order book price movement prediction and sensitivity analysis. | `deeplob-reproduction-lab`, `neural-lob-transformer-lab`, `market-microstructure-research-platform` | Add a unified LOB tensor benchmark with leakage checks, model cards, and walk-forward splits. |
| LOBFrame / Deep Limit Order Book Forecasting, https://arxiv.org/html/2403.09267 | Frames large-scale NASDAQ LOB forecasting, evaluation, and benchmark infrastructure. | `lobframe-benchmark-suite`, `lob-transformer-reproduction`, `queue-reactive-orderbook-model` | Create a public benchmark harness that compares handcrafted, transformer, and queue-reactive features on synthetic-safe fixtures. |
| Deep Learning for Limit Order Books, https://arxiv.org/abs/1601.01987 | Shows how spatial structure deep in the order book can be modeled with large-scale neural methods. | `graph-lob-gnn-lab`, `neural-lob-transformer-lab`, `hlob-feature-research` | Add deeper order-book level simulation and uncertainty-aware evaluation. |

## Market Simulation and Agent-Based Research

| Source | Why It Matters | Evidence-bearing repositories | Next extension |
| --- | --- | --- | --- |
| ABIDES: Towards High-Fidelity Market Simulation for AI Research, https://arxiv.org/abs/1904.12066 | Defines a message-based agent simulation environment modeled around exchange protocols and configurable network latency. | `abides-market-sim-lab`, `synthetic-market-data-generator`, `market-replay-hardware-harness` | Build a unified exchange-in-a-box simulator with auctions, halts, latency, agent strategies, and replayable experiment reports. |
| Event-Based Limit Order Book Simulation under a Neural Hawkes Process, https://arxiv.org/html/2502.17417v1 | Connects event-driven LOB modeling with Neural Hawkes processes and multi-event market simulation. | `hawkes-order-flow-lab`, `hawkes-liquidity-clustering-lab`, `queue-position-fill-probability-lab` | Add event-type intensity modeling and simulator calibration reports. |

## Execution, Strategy Robustness, and Research Governance

| Source | Why It Matters | Evidence-bearing repositories | Next extension |
| --- | --- | --- | --- |
| Almgren-Chriss style optimal execution literature, https://www.math.nyu.edu/~almgren/papers/optliq.pdf | Provides a classic framework for balancing execution cost and risk over time. | `optimal-execution-rl-lab`, `adaptive-order-slicing-lab`, `spread-impact-slippage-estimator`, `market-impact-propagator-lab` | Add transaction-cost-aware strategy promotion gates and execution-sensitive backtest reports. |
| Bayesian Deep Convolutional Neural Networks for Limit Order Books, https://arxiv.org/abs/1811.10041 | Shows uncertainty estimates can inform position sizing and reduce unnecessary trades. | `model-risk-validation-lab`, `llm-market-hypothesis-auditor`, `agentic-strategy-search-lab` | Add uncertainty-aware promotion criteria for strategy candidates. |
| ABIDES market-impact experiments, https://arxiv.org/abs/1904.12066 | Demonstrates simulation as a tool for testing market-impact hypotheses. | `paper-to-alpha-reproduction-suite`, `walk-forward-auto-optimizer`, `backtest-result-warehouse` | Connect simulator output to the result warehouse and research lineage ledger. |

## FPGA, Timing, and Low-Latency Systems

| Source | Why It Matters | Evidence-bearing repositories | Next extension |
| --- | --- | --- | --- |
| High Frequency Trading Acceleration using FPGAs, https://people.ucsc.edu/~hlitz/papers/hft_fpga.pdf | Discusses FPGA acceleration for feed handling and the split between hardware-accelerated data paths and software decision logic. | `fpga-low-latency-market-data-engine`, `fpga-udp-market-data-feed-handler`, `fix-fast-decoder-benchmark`, `nasdaq-itch-parser-rtl-lab` | Build a consolidated RTL/golden-model benchmark with parser, arbitration, timestamp, and risk-gate modules. |
| Precision Time Protocol security analysis, https://arxiv.org/abs/1603.00707 | Analyzes IEEE 1588 Precision Time Protocol security assumptions and why timing systems need threat modeling. | `ptp-nanosecond-timestamp-core`, `fpga-hardware-timestamping-core`, `time-sync-attack-simulator`, `distributed-clock-sync-lab` | Add timing-integrity alerts and drift/fault injection scenarios to the hardware replay harness. |
| Breaking Precision Time, https://arxiv.org/abs/2510.06421 | Shows that host-level assumptions can undermine IEEE 1588/PTP clock synchronization even when network defenses exist. | `time-sync-attack-simulator`, `zero-trust-trading-audit-lab`, `hft-config-drift-detector` | Model host-trust assumptions in timing-sensitive market infrastructure runbooks. |

## CPSE and Operator Systems

| Source | Why It Matters | Evidence-bearing repositories | Next extension |
| --- | --- | --- | --- |
| Precision Time Protocol and distributed timing references, https://www.ntp.org/reflib/ptp/ | Explains the relationship between NTP and IEEE 1588/PTP for high-speed local synchronization. | `distributed-clock-sync-lab`, `real-time-scheduler-lab`, `sensor-fusion-risk-monitor` | Connect timing quality, scheduler misses, and operator health dashboards. |
| Control and monitoring style engineering references | CPSE systems require sensors, state, timing, control loops, and operator-visible failure states. | `cpse-engineering-labs`, `industrial-control-sim-lab`, `edge-device-health-monitor`, `operator-console-design-system` | Build one CPSE capstone that links sensor simulation, network transport, anomaly detection, and operator display. |

## How Reviewers Should Use This

Start with the three whitepapers, then use this map to inspect the repositories tied to each literature thread. The strongest portfolio signal is not any single claim. It is the pattern: paper-backed intent, small tested implementations, explicit limitations, and a roadmap that keeps implementation evidence separate from future ambition.

