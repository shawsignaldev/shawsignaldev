# Strategy Robustness Whitepaper

## Thesis

A trading strategy is not credible because it has one attractive backtest. It becomes credible when the research process explains where the edge comes from, how it fails, how it survives changing regimes, and how promotion decisions are gated. The portfolio treats strategy research as a robustness problem: generate ideas, estimate expectancy, penalize drawdown, test across time, detect overfitting, preserve code, and produce reports that a human can reject.

The public work is intentionally approval-gated. The objective is not to publish a secret trading strategy or promise returns. The objective is to build the tooling a serious quant researcher would want before trusting any signal. A good strategy research system should make bad ideas cheaper to reject, good ideas easier to inspect, and every promotion decision traceable.

## Research Loop

The research loop begins with a hypothesis. A hypothesis can come from microstructure, session behavior, volatility, factor exposure, event catalysts, order flow, options structure, or machine learning. The loop then turns the hypothesis into a testable candidate with explicit inputs, outputs, entry logic, exit logic, transaction-cost assumptions, and risk controls. The candidate is run through historical windows, scored, compared to alternatives, and written into a report.

The repositories map this loop into small tools. `agentic-strategy-search-lab` ranks candidate strategies with promotion gates. `walk-forward-auto-optimizer` constructs train/test windows and parameter choices. `strategy-survivorship-analyzer` measures persistence and window-level expectancy. `realistic-fill-backtester` models partial fills and participation caps. `spread-impact-slippage-estimator` decomposes transaction costs. `backtest-result-warehouse` stores strategy results and symbol summaries. `research-lineage-ledger` records evidence and parent-child research lineage.

The portfolio also includes research primitives for specific strategy families: opening auction imbalance, queue position, volatility surface checks, options liquidity, Hawkes order flow, contextual bandits, cointegration, state-space models, and regime classification. The important point is not that every candidate is a finished strategy. The important point is that each candidate can be scored through a consistent evidence process.

## Objective Function

The ranking objective should reflect the actual decision problem. A strategy that has high average return but extreme drawdown is not automatically useful. A strategy that wins often but has poor payoff asymmetry may collapse under costs. A strategy that only works in one market regime may be valuable, but only if the regime detector is honest.

The starting score in this portfolio favors positive expectancy, lower maximum drawdown, higher profit factor, and stronger risk-adjusted return. Those metrics can be extended with turnover, exposure time, tail loss, recovery time, parameter sensitivity, symbol breadth, regime stability, and sample-size penalties. This is a search problem, not a finished theorem. A serious platform should never imply that one scalar score proves truth. The score is a triage tool that points the researcher toward candidates worth inspecting.

## Walk-Forward Discipline

Walk-forward validation is the main guardrail against overfitting. Parameters selected on one window must be evaluated on later windows. The system should track not only aggregate results but also per-window behavior: when did it work, when did it fail, which symbols were most fragile, and whether the apparent edge survived costs. A candidate that performs well only in the most favorable interval should not be promoted without a regime explanation.

The portfolio models this through train/test splits, recent-window weighting, persistence scoring, and explicit promote/watch/reject decisions. The human remains in the loop. The system can recommend a candidate, but it should also produce the evidence that would let a skeptical reviewer reject it. That is the difference between strategy automation and strategy governance.

## Options and Intraday Reality

Intraday options strategies add additional uncertainty. Same-day and nearest-weekly contracts depend on underlying movement, volatility, spread, execution quality, and contract selection. Public repositories can estimate option payoff using simplified greeks and contract assumptions, but they should not pretend that approximate historical option PnL is the same as filled live option execution.

The useful research workflow is to separate the underlying signal from the options expression. First evaluate whether the stock signal has directional edge under realistic timing and costs. Then evaluate whether contract selection, delta, premium, spread, and expiry choice preserve or destroy that edge. The system should record assumptions explicitly so later live or paper-trading evidence can replace estimates.

## Evidence Map

The evidence for this whitepaper includes:

- `agentic-strategy-search-lab` for candidate ranking and promotion gates.
- `walk-forward-auto-optimizer` for train/test windows and parameter selection.
- `strategy-survivorship-analyzer` for persistence and window-level expectancy.
- `realistic-fill-backtester` for partial fills and missed trades.
- `spread-impact-slippage-estimator` for cost decomposition.
- `backtest-result-warehouse` for result storage and symbol summaries.
- `research-lineage-ledger` for experiment lineage and missing-evidence checks.
- `options-ev-estimator` and `zero-dte-options-backtester` for options research framing.
- `llm-market-hypothesis-auditor` for evidence-gated hypothesis review.

## Limits and Honest Boundaries

The public portfolio does not prove a universal profitable strategy. No public backtest can prove that. The repositories are educational and research infrastructure. They do not include live brokerage execution, private fills, paid options history, or production risk approval. They provide a disciplined framework for testing ideas and rejecting weak claims.

There are still hard unsolved problems: regime shifts, non-stationarity, market impact, option spread behavior, data quality, look-ahead leakage, and selection bias. The correct professional stance is to make those problems visible. A platform that admits its uncertainty is more credible than one that hides it behind a high score.

## Recruiter Signal

For quant roles, this paper shows that the portfolio emphasizes research process, not isolated indicators. For software roles, it shows data models, testable workflows, report generation, and auditability. For market infrastructure roles, it shows understanding that execution, costs, and operational controls are part of the strategy, not afterthoughts. For AI-related roles, it shows how agentic tooling can help generate and audit hypotheses without replacing human approval.

The strongest signal is maturity. The work does not say, "this strategy always wins." It says, "here is how I would build the system that makes strategy claims harder to fake and easier to verify."

