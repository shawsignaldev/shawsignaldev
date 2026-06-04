# GitHub Action Items

The local repository files are prepared in this workspace. GitHub-side actions still need authenticated GitHub access.

## Security Note

Do not paste GitHub tokens, passwords, broker credentials, or API keys into chat, commits, screenshots, or docs. If a token or password is exposed, revoke or rotate it before publishing.

## Create or Update Repositories

- `shawsignaldev`
- `argus`
- `cipher`
- `ares`
- `oracle`
- `deploq`
- `aurora-market-network-explorer`
- `cpse-engineering-labs`

## Publish Commands After GitHub CLI Is Available

```powershell
gh repo create shawsignaldev/shawsignaldev --public --source C:\Users\fiboguapcci\dev\projects\shawsignaldev --remote origin --push
gh repo create shawsignaldev/deploq --public --source C:\Users\fiboguapcci\dev\projects\deploq --remote origin --push
gh repo create shawsignaldev/aurora-market-network-explorer --public --source C:\Users\fiboguapcci\dev\projects\aurora-market-network-explorer --remote origin --push
gh repo create shawsignaldev/cpse-engineering-labs --public --source C:\Users\fiboguapcci\dev\projects\cpse-engineering-labs --remote origin --push
```

Existing repositories:

```powershell
git -C C:\Users\fiboguapcci\dev\projects\argus add .
git -C C:\Users\fiboguapcci\dev\projects\argus commit -m "Professionalize ARGUS portfolio repo"
git -C C:\Users\fiboguapcci\dev\projects\argus push origin dev

git -C C:\Users\fiboguapcci\dev\projects\cipher add .
git -C C:\Users\fiboguapcci\dev\projects\cipher commit -m "Professionalize CIPHER portfolio repo"
git -C C:\Users\fiboguapcci\dev\projects\cipher push origin dev

git -C C:\Users\fiboguapcci\dev\projects\ares add .
git -C C:\Users\fiboguapcci\dev\projects\ares commit -m "Professionalize ARES portfolio repo"
git -C C:\Users\fiboguapcci\dev\projects\ares push origin dev

git -C C:\Users\fiboguapcci\dev\projects\oracle add .
git -C C:\Users\fiboguapcci\dev\projects\oracle commit -m "Professionalize ORACLE portfolio repo"
git -C C:\Users\fiboguapcci\dev\projects\oracle push origin dev
```

## Pin Order

1. `argus`
2. `cipher`
3. `ares`
4. `oracle`
5. `deploq`
6. `aurora-market-network-explorer`

## Topics

ARGUS: `python`, `quantitative-finance`, `risk-management`, `kalman-filter`, `control-theory`, `market-data`, `trading-systems`, `portfolio-risk`

CIPHER: `python`, `powershell`, `trading-terminal`, `market-data`, `quant-research`, `alpaca`, `automation`, `risk-tools`

ARES: `trading-journal`, `post-trade-analysis`, `risk-review`, `behavioral-finance`, `python`, `analytics`, `trade-review`

ORACLE: `ai`, `llm`, `research-assistant`, `market-intelligence`, `decision-support`, `python`, `agentic-workflows`

Deploq: `ai-agents`, `fintech`, `agentic-trading`, `templates`, `risk-management`, `frontend`, `marketplace`, `education`

Aurora: `streamlit`, `market-data`, `correlation-network`, `graph-analysis`, `finance`, `data-visualization`, `python`

CPSE Engineering Labs: `cyber-physical-systems`, `esp32`, `arduino`, `tcp`, `udp`, `sensors`, `embedded-systems`, `python`
