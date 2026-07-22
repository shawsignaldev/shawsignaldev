# Recruiter Packet

## Candidate Snapshot

Ephraim Shaw is a Cyber-Physical Systems Engineering student at the University of Maryland building software across quantitative research tooling, market infrastructure, operations workflows, dashboards, and embedded/networked systems.

## Strongest Review Path

| Role Target | Start Here | What It Shows |
| --- | --- | --- |
| Quantitative developer intern | ARGUS, CIPHER, Aurora, Market Data Ingestion Lab | Risk diagnostics, market-data workflows, CLI tooling, correlation networks, data-quality gates |
| Software engineering intern | CIPHER, ARES, Eidenhall, M2M, Market Data Ingestion Lab | Packaging, tests, command surfaces, schemas, automation, graph models, documentation |
| Fintech / market infrastructure intern | ARGUS, ARES, Deploq, Market Data Ingestion Lab | Risk-first design, process controls, auditability, privacy boundaries |
| Cyber-physical systems intern | CPSE Engineering Labs, ARGUS | Sensors, TCP/UDP, embedded systems, state-estimation framing |
| Data/dashboard intern | Aurora, Eidenhall | Streamlit dashboard design, graph metrics, reporting systems |

## Project Evidence

| Repository | Technical Signal | Best Files To Inspect |
| --- | --- | --- |
| ARGUS | State estimation, rolling risk diagnostics, CLI reporting, control-loop framing | `src/argus/filters.py`, `src/argus/risk.py`, `src/argus/cli.py`, `docs/technical_case_study.md` |
| CIPHER | Command taxonomy, research terminal structure, provider/config boundary | `src/cipher/cli.py`, `docs/operator_manual.md`, `docs/reliability_model.md` |
| ARES | Trade-review schema, process metrics, CSV loading, JSON export | `src/ares/schema.py`, `src/ares/metrics.py`, `tests/` |
| ORACLE | Source-note workflow, research templates, human-review boundary | `src/oracle/research.py`, `templates/`, `docs/research_protocol.md` |
| Deploq | Product architecture, static Pages site, link-tested product surfaces | `index.html`, `assets/operator-console.svg`, `docs/operating_model.md` |
| Aurora | Correlation matrix, thresholded graph edges, node metrics, dashboard export | `src/aurora/graph.py`, `src/aurora/metrics.py`, `app.py` |
| Market Data Ingestion Lab | Provider boundary, OHLCV schema validation, cleaning, CLI report, local coverage | `src/market_ingestion/loader.py`, `src/market_ingestion/quality.py`, `tests/` |
| CPSE Labs | Embedded/networking breadth with academic-integrity boundaries | `dht22-tcp-sensor/`, `network-analysis/`, `docs/lab_index.md` |
| Eidenhall | Daily memo workflow, dashboard snapshot, control-plane diagram, operations runbook | `src/eidenhall/dashboard.py`, `src/eidenhall/memo.py`, `docs/system_design.md` |
| M2M Learning Systems | Knowledge graph helpers, sanitized graph sample, review queue, scheduling workflow | `src/m2m/graph.py`, `examples/sample_knowledge_graph.json`, `docs/knowledge_graph_spec.md` |

## Research Papers

| Paper | Review Signal | Best Use |
| --- | --- | --- |
| [Market Data Infrastructure Whitepaper](papers/market-data-infrastructure-whitepaper.md) | Explains low-latency market data contracts, tickerplant design, replay, validation, and hardware-facing boundaries | Market infrastructure and data engineering screen |
| [Strategy Robustness Whitepaper](papers/strategy-robustness-whitepaper.md) | Explains walk-forward validation, objective scoring, options assumptions, promotion gates, and honest limitations | Quant developer and AI research tooling screen |
| [FPGA Trading Architecture Whitepaper](papers/fpga-trading-architecture-whitepaper.md) | Explains hardware/software trading datapaths, parser/sequencer/risk boundaries, golden models, and verification habits | Hardware engineer, FPGA, and CPSE screen |

The [Research Reading Map](RESEARCH_READING_MAP.md) connects those papers to DeepLOB, ABIDES, LOBFrame, FPGA HFT acceleration, Precision Time Protocol references, and the specific repositories that demonstrate implementation evidence.

## Role Packets

[ROLE_PACKETS.md](ROLE_PACKETS.md) gives direct review paths for Hardware / FPGA Engineer, Quant Developer, Market Infrastructure Engineer, Cyber-Physical Systems Engineer, and AI / Software Engineer screens. Use it when the reviewer needs a focused subset of the 200-repository portfolio.

## Evidence Ledger

[PORTFOLIO_EVIDENCE_LEDGER.md](PORTFOLIO_EVIDENCE_LEDGER.md) maps each major capability to public proof artifacts, validation method, and honest boundary. Use it when a reviewer wants to audit what is actually demonstrated.

## Flagship Systems Map

[FLAGSHIP_SYSTEMS_MAP.md](FLAGSHIP_SYSTEMS_MAP.md) turns the 200-repository portfolio into five coherent research programs so reviewers can inspect depth, paper-backed foundations, proof artifacts, and next research upgrades instead of reading unrelated repositories one by one.

## Reproducibility Guide

[REPRODUCIBILITY_GUIDE.md](REPRODUCIBILITY_GUIDE.md) gives exact commands for profile verification, site verification, representative repository verification, GitHub Actions checks, and live readback.

## Interview Talking Points

- Risk-first systems: why controls, caps, and review gates matter before speed.
- State estimation: how noisy observations can be smoothed and monitored.
- Market-network structure: how correlation thresholds change graph density and clusters.
- Data-quality boundaries: how provider inputs are normalized and validated before analytics.
- Knowledge graphs: how concepts, prerequisites, weak points, and review cycles become a system.
- Workflow tooling: how repeatable command surfaces reduce operational friction.
- Privacy and security: how credentials, account data, and restricted coursework are excluded.

## Current Portfolio Standard

- Public repositories use deterministic examples or sanitized templates.
- Finance-related repositories include educational and research disclaimers.
- Major Python repositories run tests and GitHub Actions.
- Public docs distinguish implemented v0.1 functionality from roadmap items.
- The GitHub profile points reviewers to the strongest repos first.
