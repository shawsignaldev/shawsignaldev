# Portfolio Reality Audit

## Purpose

This audit exists because the GitHub profile is only useful if GitHub displays real code, runnable examples, tests, documentation, and clear evidence. A repository that is empty, README-only, tiny, or full of process-residue language weakens the whole portfolio, even if the top-level profile looks organized.

The standard is direct: every employer-facing project should contain real implementation code, a README that explains what the project does, public-safe fixtures or examples, a verification path, and enough structure that a reviewer can click through the repository and see engineering work rather than a shell.

## Current Evidence

The first repository inventory was taken with:

```powershell
gh repo list shawsignaldev --limit 300 --json name,isPrivate,description,updatedAt,diskUsage,primaryLanguage,url
```

The scan showed a large portfolio with many repositories in the 2 KB to 8 KB range and one empty repository. A tiny repository is not automatically bad, but it must be inspected before it is promoted.

| Risk class | Evidence | Required action |
| --- | --- | --- |
| Empty repository | `QuantPortfolio` originally reported `0 KB` and no primary language. | Repaired on 2026-08-02 with a Python package, risk analytics, optimizer, backtest module, CLI, tests, sample data, docs, and CI. |
| Tiny repository | Many repositories reported only `2 KB` to `4 KB`. | Inspect each one for real source files, tests, docs, and examples before treating it as employer-facing. |
| README-only risk | Small disk usage often means the repo may contain mostly README text. | Add source modules, deterministic examples, test files, reports, and CI, or remove it from promoted materials. |
| process-residue language | Profile scan checks for public text that reads like scaffolding, tool output, or unfinished project setup. | Remove process residue and rewrite docs as direct engineering prose. |

## Evidence Gate

A project is not complete until a reviewer can open it on GitHub and verify:

- Real code exists in the repository, not just references to future work.
- The README explains the problem, the design, the proof, and the limits.
- Tests or deterministic verification commands are present.
- Public-safe inputs, examples, fixtures, or synthetic data are included when the project claims analysis behavior.
- CI exists for code projects unless the repository is intentionally documentation-only.
- process-residue language is absent from public-facing prose and source comments.
- The repository is either promoted with evidence or left out of the employer-facing review path.

## Repair Queue

The immediate repair queue starts with the highest-risk public presentation issues:

1. Repositories with `2 KB` disk usage: inspect for README-only shells and rebuild the most visible ones first.
2. Repositories with `3 KB` to `4 KB` disk usage: verify they contain implementation code, tests, and examples.
3. Repositories currently promoted in `README.md`, `PROJECTS.md`, `ROLE_PACKETS.md`, and `FLAGSHIP_SYSTEMS_MAP.md`: apply the strictest evidence gate first because those are most likely to be clicked by employers.
4. New repositories created during this goal: no promotion until tests pass, CI is present, docs are complete, and the public language is clean.

## Repaired Repositories

| Repository | Previous issue | Current public evidence |
| --- | --- | --- |
| `QuantPortfolio` | Two-line README and no primary language in GitHub metadata. | `src/quantportfolio/`, `tests/`, `examples/sample_returns.csv`, `docs/architecture.md`, `pyproject.toml`, `.github/workflows/ci.yml`, and green CI on commit `ee38203`. |

## Operating Rule

From this point forward, the portfolio is not complete until the audit has been run, the repair queue has been worked down, and the promoted repositories have public evidence. This keeps the portfolio aligned with the actual goal: GitHub displays polished, real code across quant research, CPSE, FPGA, trading systems, and AI infrastructure rather than blank projects or empty claims.
