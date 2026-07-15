# FPGA Trading Architecture Whitepaper

## Thesis

FPGA trading architecture is valuable because some market-infrastructure tasks are naturally streaming, bounded, and latency-sensitive. Packet parsing, sequence validation, top-of-book updates, timestamping, throttles, and simple risk gates can be expressed as deterministic data paths. The portfolio uses public, testable reference models to show how those boundaries work without claiming access to proprietary exchange systems or measured production hardware results.

The central idea is hardware/software co-design. Python reference models explain behavior. Verilog or RTL-style boundaries show how the behavior could be mapped into hardware. Tests compare expected state transitions and failure behavior. Documentation states what is implemented, what is simulated, and what would require real synthesis, timing analysis, and board validation.

## System Boundary

The candidate architecture has six stages. First, a packet intake stage receives frames, filters sessions, and extracts payloads. Second, a parser stage validates message type and required fields. Third, a sequencer detects gaps, duplicates, and resets. Fourth, a state stage reconstructs top-of-book or order-book state. Fifth, a risk stage rejects unsafe order intent based on limits, kill switches, and market-state faults. Sixth, an output stage emits normalized events, telemetry, or approved order intent.

The repositories correspond to these stages. `fpga-udp-market-data-feed-handler` covers packet intake and session filtering. `fpga-fix-protocol-parser` and `nasdaq-itch-parser-rtl-lab` cover protocol parsing boundaries. `multicast-feed-arbitration-fpga` covers feed arbitration and gap logic. `fpga-lob-reconstruction-engine` and `market-data-tickerplant-simulator` cover state reconstruction. `fpga-nanosecond-orderbook-risk-gate`, `risk-gate-co-simulation-lab`, and `symbiyosys-formal-risk-gates` cover risk controls. `market-replay-hardware-harness` provides a replay-style test path.

## Hardware/Software Co-Design

The portfolio uses Python for the golden model because Python is readable and easy to test. It uses RTL-style modules or hardware-oriented models where the boundary matters. This is not a shortcut around hardware. It is the normal engineering pattern: define behavior in an executable reference model, create deterministic fixtures, implement the hardware boundary, and compare outputs. When a test fails, the golden model and RTL boundary make the mismatch inspectable.

The co-design repos also show fixed-point thinking. `fixed-point-finance-lab` demonstrates basis-point and EMA-style calculations without relying on floating-point behavior. `hls-vs-rtl-latency-lab` compares methodological tradeoffs. `fpga-fifo-depth-planner`, `pcie-throughput-budget-lab`, `dma-burst-coalescer-simulator`, and `pcie-descriptor-ring-simulator` show that data movement, buffering, and backpressure are as important as arithmetic.

## Operating Model

The operating model separates research iteration from safety-critical execution boundaries. Strategy research can change often, but parser contracts, sequence checks, timestamp behavior, and final risk gates should change slowly and with stronger review. That separation is important in any trading system because the fastest component is not the most valuable component if it can move bad state forward. A hardware-oriented path should therefore expose telemetry for rejected messages, gap events, stale state, throttle decisions, and kill-switch activation. Operators and researchers need to know not only what was accepted but also what was refused.

This model also gives software and hardware teams a shared language. Software owns the richer research loop, configuration management, replay tooling, and reports. Hardware owns the bounded data path, deterministic state transitions, and low-latency safety checks. The interface between them is a compact event or order-intent contract. That contract is where tests, documentation, and review should concentrate.

## Verification Model

The verification strategy combines deterministic examples, golden-model comparison, coverage-style checks, and operating-boundary documentation. Public tests should prove basic invariants: malformed messages are rejected, sequence gaps are flagged, state updates are deterministic, limits prevent unsafe output, and replay produces consistent results. More advanced hardware verification would require formal properties, constrained-random testbenches, synthesis checks, timing reports, and board-level validation. The public portfolio does not claim those steps unless a repo actually contains them.

The purpose of the public layer is to show verification habits. `uvm-lite-verification-harness` models scoreboard and mismatch reporting. `formal-liveness-monitor-lab` and `hardware-formal-coverage-lab` model formal coverage thinking. `rtl-lint-rule-engine` and `hardware-timing-constraint-checker` show quality gates. `clock-domain-reset-sequencer-lab` and `fpga-cdc-metastability-lab` show awareness of reset and clock-domain issues. These are the details that distinguish hardware engineering from writing a simple parser.

## Risk Gate Philosophy

Risk gates are central because speed without safety is not infrastructure. A hardware risk gate should be simple enough to trust: exposure limits, quantity limits, kill switch, stale-market flag, crossed-market flag, and sequence-fault flag. Complex strategy logic can stay in software, but final permission checks should be deterministic and auditable. This separation also makes the system easier to review: research can evolve quickly while the risk gate remains stable and verified.

The portfolio frames order intent carefully. Public code should not be a broker integration. It should model the decision boundary: candidate signal in, risk checks applied, approved or rejected intent out. That boundary is valuable to employers because it shows judgment about safety, not just interest in speed.

## Evidence Map

The evidence for this paper includes:

- `fpga-low-latency-market-data-engine` for the flagship market-data pipeline.
- `fpga-udp-market-data-feed-handler` for packet parsing and sequence telemetry.
- `fpga-nanosecond-orderbook-risk-gate` for order-book safety gating.
- `fpga-latency-arbitration-crossbar` for stream arbitration and backpressure.
- `fpga-pcie-market-data-dma-engine` for descriptor validation and DMA-style movement.
- `fpga-fix-protocol-parser` for hardware-oriented connectivity parsing.
- `fpga-lob-reconstruction-engine` for add, modify, cancel, and trade transitions.
- `fpga-hardware-timestamping-core` and `ptp-nanosecond-timestamp-core` for timing discipline.
- `risk-gate-co-simulation-lab` and `symbiyosys-formal-risk-gates` for risk verification framing.

## Limits and Honest Boundaries

The public repositories are not exchange-certified trading systems. They do not include proprietary feeds, live broker connectivity, hardware board deployment claims, or final timing closure. Some are Python reference models with RTL boundaries; some are Verilog-style educational implementations; some are documentation-backed design slices. That boundary is intentional. The work is meant to be safe, public, and reviewable.

The next professional step would be to unify the hardware repos into a single FPGA trading reference architecture with shared fixtures, a common packet/event schema, CI simulation, formal checks where feasible, and benchmark reports that separate cycle estimates from measured toolchain outputs. That would turn the current evidence into a deeper capstone.

## Recruiter Signal

For hardware roles, this paper shows understanding of datapaths, backpressure, reset/CDC concerns, verification, and golden-model comparison. For market infrastructure roles, it shows that low latency is treated as a systems property, not a slogan. For CPSE roles, it shows cyber-physical thinking: external events, timing constraints, state estimation, safety gates, and operator telemetry. For software roles, it shows decomposition, testing, and documentation discipline across a large public portfolio.

The most important signal is honesty. The portfolio makes a strong case without overstating what public examples prove. That is the kind of engineering judgment employers can trust.
