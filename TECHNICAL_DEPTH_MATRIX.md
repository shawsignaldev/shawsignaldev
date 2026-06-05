# Technical Depth Matrix

| Skill Area | Evidence | Repository |
| --- | --- | --- |
| Python packaging | `src/` layout, `pyproject.toml`, tests, CLI entry points | ARGUS, CIPHER, ARES, ORACLE, Aurora, Eidenhall, M2M, Market Data Ingestion Lab |
| Market-data quality | Provider boundary, OHLCV validation, clean frame output, quality report | Market Data Ingestion Lab |
| Quant/risk tooling | Drawdown, volatility, stability margins, rolling windows | ARGUS |
| State estimation | Scalar Kalman-style smoothing over sample observations | ARGUS |
| Command-line systems | Command taxonomy and terminal report rendering | CIPHER, ARGUS |
| Data visualization | Correlation matrix, graph metrics, Streamlit dashboard | Aurora |
| Product architecture | Static product system, operator controls, audit model | Deploq |
| Schemas and exports | Typed trade records, CSV load, JSON export | ARES |
| Operations tooling | Daily memo generation, dashboard status, runbook | Eidenhall |
| Control-plane modeling | Dashboard snapshot, review gate, stale-input tracking, operations topology | Eidenhall |
| Embedded/networking | ESP32, DHT22, TCP/UDP scripts, sensor workflows | CPSE Engineering Labs |
| Knowledge graphs | Concepts, prerequisite edges, graph integrity checks, sanitized graph sample | M2M Learning Systems |
| Learning systems | Review queue, cycle scheduling, mock-exam workflow | M2M Learning Systems |

## Gaps To Keep Improving

- Add more public historical-data studies once data-source boundaries are finalized.
- Add richer dashboard screenshots after every visual surface has been reviewed for safe publication.
- Add additional edge-case tests as modules mature.
- Keep private trading data, credentials, coursework, and account records out of public repositories.
