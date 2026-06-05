# Package Surfaces

This portfolio favors installable, reviewable project surfaces where a Python package is the right shape for the work. Static sites and sanitized lab portfolios use simpler structures when packaging would not add value.

| Repository | Package surface | Entry points | Verification |
| --- | --- | --- | --- |
| ARGUS | `src/argus`, `pyproject.toml` | CLI and examples | pytest, GitHub Actions |
| CIPHER | `src/cipher`, `pyproject.toml` | CLI command taxonomy, PowerShell launcher | pytest, GitHub Actions |
| ARES | `src/ares`, `pyproject.toml` | Review/demo scripts | pytest, GitHub Actions |
| ORACLE | `src/oracle`, `pyproject.toml` | Research workflow helpers | pytest, GitHub Actions |
| Aurora | `src/aurora`, `pyproject.toml` | Streamlit `app.py` | pytest, GitHub Actions |
| Eidenhall | `src/eidenhall`, `pyproject.toml` | Memo, dashboard snapshot, control-plane workflow | pytest, GitHub Actions |
| M2M Learning Systems | `src/m2m`, `pyproject.toml` | Knowledge graph helpers, review cycle examples | pytest, GitHub Actions |
| Market Data Ingestion Lab | `src/market_ingestion`, `pyproject.toml` | `market-ingest` CLI | pytest with coverage, GitHub Actions |
| Deploq | Static product site | GitHub Pages | link/static checks |
| CPSE Engineering Labs | Sanitized lab portfolio | Python/Arduino examples | structure tests |

## Standard

- `src/` layout for package code
- deterministic examples or safe sample data
- `requirements.txt` for fast reviewer setup
- `pyproject.toml` where installability matters
- tests that do not require credentials or private data
- GitHub Actions for public verification
