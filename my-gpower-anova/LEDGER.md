# LEDGER: Evidence Registry

| ID | Claim / Behavior | Evidence Source | Tag | Confidence | Verification / Notes |
|:---|:---|:---|:---|:---|:---|
| EV-01 | One-Way ANOVA pay serbestlik derecesi formülü: df_num = k - 1 | G*Power Manual & Formula | [DOK] | High | k = 3 için df_num = 2 sabittir. |
| EV-02 | Total Sample Size (N) her zaman k (3) sayısının tam katına yukarı yuvarlanır. | G*Power Binary Execution & Differential Tests | [REA] | High | N_raw = 157.1 çıksa dahi grup başına n=53 yapacak şekilde N=159'a ceil() uygulanır. |
| EV-03 | Denominator serbestlik derecesi formülü: df_den = N_total - k | G*Power Output Inspection | [DOK] | High | N=159 ve k=3 iken df_den = 156 olur. |
| EV-04 | Non-centrality parameter (ncp / lambda) = f^2 * N_total | Binary Output Mapping | [REA] | High | f=0.25, N=159 için ncp = 0.0625 * 159 = 9.9375 birebir doğrulanmıştır. |
| EV-05 | Bisection / Iteration durma kriteri: Calculated Power >= Target Power | Differential Test Set (30/30 match) | [REA] | High | İterasyon power değerini ilk karşılayan n_per_group adımında durur. |
| EV-06 | Floating point tolerance in power convergence check | Differential Test Iteration | [REA] | High | Power aramasında SciPy ile G*Power numeric float hassasiyeti arasında mikro farklar bulunur. |