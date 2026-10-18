# SPECIFICATION: One-Way ANOVA Power Engine (G*Power Teardown)

## Feature: One-Way ANOVA Sample Size and Power Calculation
  As a clinical researcher or AI Agent
  I want to calculate the required sample size and actual statistical power for One-Way ANOVA with 3 groups
  So that clinical trials are properly powered without wasting resources.

  Background:
    Given the target test family is "anova-oneway"
    And the statistical model assumes 3 fixed, equal-sized treatment groups (k = 3)

  Scenario: Calculate required sample size (A Priori Mode)
    When I request sample size with:
      | parameter   | value        |
      | test        | anova-oneway |
      | mode        | a-priori     |
      | f           | 0.25         |
      | alpha       | 0.05         |
      | power       | 0.80         |
      | groups      | 3            |
    Then the total sample size "n_total" MUST be 159
    And "df_num" MUST be 2
    And "df_den" MUST be 156
    And "critical" MUST be 3.0543
    And "ncp" MUST be 9.9375
    And "actual_power" MUST be greater than or equal to 0.80

  Scenario: Group Multiplicity Constraint Rule
    When the unrounded continuous total sample size N_calculated is obtained
    Then the final N_total MUST be rounded UP to the nearest multiple of group count (k = 3)
    Because each group must contain an equal integer number of participants (n_per_group = N_total / 3).