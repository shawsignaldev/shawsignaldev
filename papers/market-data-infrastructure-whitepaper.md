# Market Data Infrastructure Whitepaper

## Thesis

Market-data infrastructure is the first place where a trading or research system either earns trust or becomes impossible to reason about. A useful market system is not just a model that consumes prices. It is a sequence of contracts: receive the feed, normalize the message, preserve order, detect gaps, timestamp the observation, project state, expose telemetry, and make downstream research aware of uncertainty. This portfolio treats market data as an engineered system instead of a loose collection of API calls.

The core design idea is a deterministic market-data path with visible failure modes. Every feed event should have a source, sequence, timestamp, schema, validation result, and replay path. A downstream researcher should be able to ask why a signal changed and get a reproducible answer. A hardware reviewer should be able to see which parts map naturally to an FPGA or SmartNIC data path. A software reviewer should be able to inspect the same path as Python reference models, tests, and documentation.

## Architecture

The public repositories form a layered reference architecture. `market-data-ingestion-lab` starts with OHLCV validation and quality reports. `market-data-schema-contracts` defines required fields, type checks, positive price and size rules, and sequence-gap detection. `event-sourced-market-feed-pipeline` models sequence-aware replay and top-of-book projection. `market-data-tickerplant-simulator` builds a tickerplant view from quote updates. `market-data-reconciliation-engine` compares provider outputs under tolerance rules. `synthetic-market-data-generator` creates deterministic fixtures so tests do not depend on restricted feeds.

The low-latency layer extends the same idea into hardware-facing systems. `fpga-low-latency-market-data-engine`, `fpga-udp-market-data-feed-handler`, `nasdaq-itch-parser-rtl-lab`, `multicast-feed-arbitration-fpga`, `fix-fast-decoder-benchmark`, and `ptp-nanosecond-timestamp-core` make the feed path reviewable from packet parsing through arbitration and timestamp math. The repositories avoid pretending to be production exchange infrastructure. They are reference models and testable design slices. The important signal is that the boundaries are explicit: parser, sequencer, arbiter, tickerplant, replay harness, and alert path.

## Data Contract

The canonical event contract is intentionally small. A useful public event needs a symbol, event time, receive time, source, sequence number, event type, price, size, side, and validation verdict. In a production system there would be venue-specific extensions, order identifiers, channel IDs, and recovery metadata. In this portfolio the smaller public contract keeps the examples inspectable while preserving the engineering shape of a real system.

The contract rejects ambiguous inputs early. Price and size must be positive when present. Sequence numbers must be monotonic within a channel unless a reset is explicitly modeled. A quote update should be able to update top-of-book state without mutating unrelated historical records. Replay should rebuild the same state from the same ordered event list. These are simple invariants, but they are the invariants that make later modeling credible.

## Low-Latency Design

Latency work is treated as a budget and bottleneck problem, not a marketing number. The path is decomposed into decode, validation, sequence check, state update, risk check, routing, and telemetry stages. Each stage has its own measurable or simulated contribution. The point is not to claim a final hardware timing result from a public Python model. The point is to show that the design has boundaries that can be instrumented, verified, and moved into faster execution environments.

The hardware-facing repositories emphasize fixed data paths, deterministic control flow, bounded state, and self-checking tests. A feed handler should reject malformed messages without corrupting state. A multicast arbiter should prefer the earliest valid sequence and flag gaps rather than silently accepting inconsistent feeds. A timestamp core should preserve monotonicity and explain offset calculations. These details matter because financial infrastructure fails through edge cases more often than through the happy path.

## Validation Strategy

The validation plan is layered. Unit tests check parser and schema behavior. Replay tests check deterministic reconstruction. Contract tests check required fields and boundary cases. Reconciliation tests compare multiple provider-like inputs. Hardware-facing tests check golden-model agreement and state transitions. Documentation tests force the public repos to carry system design, validation evidence, and operating-boundary notes instead of leaving the reader to infer intent.

This is not a substitute for production certification, exchange conformance, hardware timing closure, or live market certification. It is a public evidence layer that proves the candidate can reason about the system in a disciplined way. The strongest signal is the consistency across repos: data contracts, deterministic examples, tests, CI, security boundaries, and explicit limitations.

## Evidence Map

The evidence for this paper is spread across the portfolio:

- `market-data-ingestion-lab` shows schema validation, cleaning, and data-quality reporting.
- `market-data-schema-contracts` focuses on field contracts and sequence gaps.
- `event-sourced-market-feed-pipeline` demonstrates event replay and top-of-book projection.
- `market-data-tickerplant-simulator` models tickerplant state from normalized updates.
- `market-data-reconciliation-engine` checks provider mismatch and tolerance behavior.
- `fpga-udp-market-data-feed-handler` models packet/session filtering and sequence telemetry.
- `nasdaq-itch-parser-rtl-lab` demonstrates ITCH-style parser boundaries.
- `multicast-feed-arbitration-fpga` models A/B feed arbitration and gap reporting.
- `ptp-nanosecond-timestamp-core` isolates timestamp offset and delay calculations.

## Limits and Honest Boundaries

The public repositories do not contain private exchange data, account access material, paid data feeds, or production market access. They do not claim exchange-certified feed handling. They do not claim board-level timing results from public examples. They are intentionally sanitized and deterministic. This makes them weaker as production artifacts but stronger as employer-review artifacts, because an engineer can run them without special access and inspect the design boundaries directly.

The next stage would be a unified exchange-in-a-box simulator, a shared event schema package, more realistic recovery paths, and benchmark reports that compare latency, loss handling, and replay correctness across implementations. That would turn the current portfolio from many strong slices into one integrated reference platform.

## Recruiter Signal

For a market infrastructure role, this paper shows that the portfolio is not just quantitative notebooks. It shows data engineering, packet thinking, deterministic systems, hardware/software boundaries, test design, and operational awareness. For an FPGA or CPSE role, it shows that market data can be framed as a real-time cyber-physical workflow: noisy external events enter a bounded system, state is updated under timing constraints, and operators need visibility when assumptions break. For a software role, it shows clean decomposition and a bias toward reproducible systems.
