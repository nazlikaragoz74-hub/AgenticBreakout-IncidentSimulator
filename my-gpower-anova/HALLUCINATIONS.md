# HALLUCINATIONS: AI Agent Error Log

## Incident 1: Standard Ceil Rounding Assumption
- **Agent Claim:** AI agent initial specification claimed that N_total is simply rounded up using standard `math.ceil(N_calculated)`.
- **How Discovered:** Differential test failed on test case 1 (Expected N=159, Agent engine produced N=157).
- **Correct Behavior:** G*Power enforces equal group allocation for ANOVA (k=3), meaning `n_per_group = math.ceil(N_calculated / 3)` and `N_total = n_per_group * 3`.
- **Catching Test:** Differential test case #1 (`f=0.25, alpha=0.05, power=0.80`).

## Incident 2: Non-Centrality Parameter Calculation Formula
- **Agent Claim:** Agent assumed ncp formula was `f * sqrt(N_total)`.
- **How Discovered:** Critical F values and power calculations deviated significantly from G*Power oracle outputs.
- **Correct Behavior:** Correct formula used in G*Power binary is `lambda = (f^2) * N_total`.
- **Catching Test:** Oracle vector comparison test.