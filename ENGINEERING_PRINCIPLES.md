# Engineering Principles

## Risk First

Systems that touch markets, credentials, personal records, or coursework need explicit boundaries. Public repositories should show the design while keeping private data, secrets, account details, and restricted academic materials out of source control.

## Reproducible Public Surface

Every project should be reviewable without private services. Examples use deterministic sample data, local files, or clearly documented provider boundaries.

## Observable Workflows

Good tooling makes state visible. Repositories emphasize logs, reports, review gates, architecture diagrams, and clear module boundaries so a reviewer can understand what the system does and where risk enters.

## Documentation As Interface

Recruiters and engineers often inspect documentation before code. Each repository is structured so the README explains the problem, the docs explain the architecture, and examples show expected behavior.

## Conservative Claims

Public work should be credible. Roadmaps are labeled as roadmaps, finance repositories include disclaimers, and incomplete integrations are represented as interfaces or design notes rather than overstated production systems.

## Security Hygiene

`.env.example` files show variable names only. `.gitignore` excludes local environments, cache files, private data folders, databases, and notebooks checkpoints. Security files describe what must never be committed.
