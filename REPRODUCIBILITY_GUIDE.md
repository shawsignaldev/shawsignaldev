# Reproducibility Guide

This guide gives reviewers exact commands for auditing the public portfolio. It is written for engineers who want to verify structure, tests, CI, and deployment evidence without relying on the README alone.

## Profile verification

Run from the profile repository:

```powershell
cd C:\Users\fiboguapcci\dev\projects\shawsignaldev
$env:POWERSHELL_TELEMETRY_OPTOUT='1'
C:\Users\fiboguapcci\.pyenv\pyenv-win\versions\3.12.7\python.exe -m unittest discover -s tests -v
git status --short
gh run list --repo shawsignaldev/shawsignaldev --limit 5 --json status,conclusion,workflowName,headSha
```

Portable form:

```powershell
python -m unittest discover -s tests -v
```

What this proves:

- The profile meta-artifacts are present and linked.
- Whitepapers, reading map, role packets, and evidence ledger are covered by tests.
- The working tree can be checked for unexpected local drift.
- Recent GitHub Actions runs can be inspected.

What this does not prove:

- It does not prove every one of the 200 repositories has equal depth.
- It does not prove private data, production trading behavior, or deployment claims.
- It does not replace opening representative repositories and reading their docs/tests.

## Site verification

Run from the portfolio site repository:

```powershell
cd C:\Users\fiboguapcci\dev\projects\shawsignaldev.github.io
$env:POWERSHELL_TELEMETRY_OPTOUT='1'
C:\Users\fiboguapcci\.pyenv\pyenv-win\versions\3.12.7\python.exe -m pytest -q -p no:cacheprovider
git status --short
gh run list --repo shawsignaldev/shawsignaldev.github.io --limit 5 --json status,conclusion,workflowName,headSha
```

Portable form:

```powershell
python -m pytest -q -p no:cacheprovider
```

What this proves:

- The live-site source includes expected navigation, project links, research papers, role packets, evidence ledger, and reproducibility guide.
- Static site checks can run without private credentials.
- Recent GitHub Pages and static-check workflows can be inspected.

What this does not prove:

- It does not prove browser rendering on every device.
- It does not prove GitHub Pages cache has updated until live readback is performed.

## Live readback

Use public URLs to confirm deployed content:

```powershell
$depth=(Invoke-WebRequest -Uri 'https://shawsignaldev.github.io/technical-depth.html?bust=manual' -UseBasicParsing -Headers @{'Cache-Control'='no-cache'}).Content
$depth.Contains('Evidence Ledger')
$depth.Contains('Reproducibility Guide')

$papers=(Invoke-WebRequest -Uri 'https://shawsignaldev.github.io/papers.html?bust=manual' -UseBasicParsing -Headers @{'Cache-Control'='no-cache'}).Content
$papers.Contains('Research Reading Map')

$guide=(Invoke-WebRequest -Uri 'https://shawsignaldev.github.io/review-guide.html?bust=manual' -UseBasicParsing -Headers @{'Cache-Control'='no-cache'}).Content
$guide.Contains('Role Packets')
```

What this proves:

- The public site exposes the intended review surfaces after deployment.
- The deployed page content matches the current portfolio thesis.

What this does not prove:

- It does not prove every linked repository has passing CI at that moment.
- It does not verify every external source link in the reading map.

## Representative repository verification

The portfolio is large, so reviewers should sample representative repositories by role:

```powershell
$repos=@(
  'fpga-low-latency-market-data-engine',
  'agentic-strategy-search-lab',
  'market-data-tickerplant-simulator',
  'llm-market-hypothesis-auditor'
)
foreach($repo in $repos){
  gh run list --repo "shawsignaldev/$repo" --limit 1 --json status,conclusion,workflowName,headSha
}
```

If those repos are cloned locally under `C:\Users\fiboguapcci\dev\projects`, inspect local state with:

```powershell
foreach($repo in $repos){
  git -C "C:\Users\fiboguapcci\dev\projects\$repo" status --short
}
```

What this proves:

- Reviewers can verify representative CI status without opening every repository manually.
- The sampled repos cover hardware, strategy research, market infrastructure, and AI research governance.

What this does not prove:

- A small sample does not certify all 200 repositories.
- CI success only proves the tests configured in that repository, not unstated production behavior.

## Public repo count

```powershell
(gh repo list shawsignaldev --limit 250 --json name | ConvertFrom-Json | Measure-Object).Count
```

What this proves:

- The public GitHub account exposes the expected portfolio scale.

What this does not prove:

- Repository count is not quality by itself. The stronger proof is the combination of green CI, docs, role packets, whitepapers, reading map, evidence ledger, and representative source review.
