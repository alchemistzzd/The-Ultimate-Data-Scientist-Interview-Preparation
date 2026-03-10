# Causal Inference Notes — Week 1

## 1. Key Mindset: Prediction vs Causation

- **Prediction / Association**: P(Y | X)
- **Causal effect / Intervention**: P(Y | do(X))
- Example: Ice cream sales predict drowning → correlation ≠ causation

---

## 2. Core Concepts

### Confounder
- Variable that affects both **Treatment (X)** and **Outcome (Y)**
- Example:
  - Treatment: Carrying a lighter
  - Outcome: Lung cancer
  - Confounder: Smoking
- DAG:


### Selection Bias / Reverse Causality
- Occurs when treatment assignment is **not random**
- Example:
- High-stress people more likely to start exercising → Exercise group may have higher stress initially

### Randomization
- Breaks confounder → treatment link
- Makes groups **exchangeable**
- Average difference in outcome = causal effect
- Key property: Treatment ⊥ Confounders

---

## 3. Mini Exercises / Thought Experiments

1. Smoking → Lighter → Lung cancer: Identify confounder ✅  
2. Exercise ↔ Stress: Possible confounder?  
 - Example: Routine / self-discipline

---

## 4. Key Takeaways

- Observed correlation ≠ causal effect  
- Confounders and selection bias can bias estimates  
- Randomized experiments solve confounding in expectation  
- Observational causal inference is needed when **randomization isn’t possible**



# Piece 2 — Regression Adjustment in A/B Tests

## 1. What regression adjustment is

In an experiment we estimate the treatment effect using regression:

Y = β0 + β1 * Treatment + β2 * Covariates

Where:

- Y = outcome (revenue, clicks, purchases, etc.)
- Treatment = experiment assignment (0 = control, 1 = treatment)
- Covariates = pre-treatment variables (past behavior, demographics, etc.)

The treatment effect estimate is:

β1

---

## 2. Why regression is used in randomized experiments

Randomization already guarantees the treatment effect estimate is **unbiased**.

Regression adjustment is used to:

- reduce variance
- increase statistical power
- improve precision of the treatment estimate

Key idea:

Regression is **not fixing bias** in a randomized experiment.  
It is mainly used to **reduce variance**.

---

## 3. How variance reduction works

Outcome variation comes from many sources:

- user heterogeneity
- behavioral differences
- random noise

If a covariate predicts the outcome, regression explains part of that variation.

Conceptually:

Outcome variance = explained variance + residual variance

Regression removes part of the **explained variance**, leaving smaller **residual variance**.

Smaller residual variance → smaller variance of the treatment estimate → smaller standard error.

---

## 4. Good covariates

Good covariates should be:

- measured **before treatment**
- **predictive of the outcome**

Examples:

- past purchases
- past engagement
- user tenure
- historical conversion rate

These reduce noise caused by natural differences between users.

---

## 5. Bad covariates

### Post-treatment variables (introduce bias)

Example:

Treatment → time spent → purchases

Controlling for time spent blocks part of the treatment effect.

---

### Irrelevant variables (increase variance)

Examples:

- user_id modulo value
- random hash
- unrelated demographic features

These add parameters to estimate but do not reduce residual variance.

---

## 6. Key interview explanation

A strong explanation:

"In randomized experiments the difference in means already provides an unbiased estimate of the treatment effect. Regression adjustment with pre-treatment covariates can reduce residual variance in the outcome, which decreases the standard error and improves the precision of the treatment effect estimate."

---

## 7. Key takeaway

Use regression adjustment to:

- reduce variance
- improve precision

Avoid:

- post-treatment variables (bias)
- irrelevant covariates (increase variance)