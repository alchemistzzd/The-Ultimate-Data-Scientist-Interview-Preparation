## Material

https://www.bradyneal.com/causal-inference-course



## Table of contents
- [Interview keys](#interview-keys)
- [Causal Inference Notes — Week 1](#causal-inference-notes--week-1)
- [Piece 2 — Regression Adjustment in A/B Tests](#piece-2--regression-adjustment-in-ab-tests)
- [Piece 3 — Good vs Bad Covariates in Regression Adjustment](#piece-3--good-vs-bad-covariates-in-regression-adjustment)

---
# Interview keys

1. Step by step, be specific for the case, do not jump to conclusion

2. Include the causal impact, X impacts Y, X is an indicator of Y etc.

3. Do not say do not launch easily, say .. might impact result. Recommend more experiments etc.


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

Regression accounts for more **explained variance**, leaving smaller **residual variance**.

Smaller residual variance → smaller variance of the treatment estimate → smaller standard error.

$\mathrm{Var}(Y) = \mathrm{Var}(\hat{Y}) + \mathrm{Var}(\varepsilon)$


3. What happens when we add predictive covariates

If we include a covariate X that strongly predicts Y, then the regression can explain more variation:

$\mathrm{Var}(\hat{Y}) \uparrow$

Since total variance stays the same:

$\mathrm{Var}(Y) = \text{constant}$

the residual variance must decrease:

$\mathrm{Var}(\varepsilon) \downarrow$
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

# Piece 3 — Good vs Bad Covariates in Regression Adjustment

## 1. Goal of covariate selection

In randomized experiments, covariates are included in regression to:

- reduce variance
- improve precision of the treatment effect estimate

Randomization already guarantees **unbiased estimates**, so covariates are not needed to remove confounding.

---

## 2. Good covariates

Good covariates have two key properties:

1. Measured **before treatment**
2. **Predictive of the outcome**

These variables explain natural variation in the outcome, which reduces residual variance.

Examples:

- past purchases
- past engagement
- historical conversion rate
- user tenure

Effect:

Reducing unexplained outcome variation leads to a **smaller standard error of the treatment estimate**.

---

## 3. Bad covariates

### Post-treatment variables (introduce bias)

Post-treatment variables are affected by the treatment.

Example causal structure:

Treatment → Clicks → Purchases

If we control for clicks in regression:

Purchases = β0 + β1 * Treatment + β2 * Clicks

The regression attributes the increase in purchases to clicks rather than treatment.

This blocks part of the causal pathway and introduces **downward bias** in the treatment estimate.

---

### Weak or irrelevant covariates (increase variance)

Variables that are unrelated to the outcome do not reduce residual variance.

Examples:

- user_id modulo values
- random hashes
- unrelated demographic features

Including these variables forces the model to estimate additional parameters without reducing noise.

Result:

Variance of the treatment estimate may **increase**, reducing precision.

---

## 4. Mediators

A mediator is a variable on the causal pathway:

Treatment → Mediator → Outcome

Example:

Treatment → Clicks → Purchases

If we control for the mediator, we remove part of the treatment effect.

Regression then estimates only the **direct effect**, not the **total effect**.

---

## 5. Key interview rule

Safe covariates:

- pre-treatment variables
- predictive of the outcome

Avoid:

- post-treatment variables (introduce bias)
- irrelevant covariates (increase variance)

---

## 6. Key takeaway

Regression adjustment works best when covariates:

- are measured before treatment
- strongly predict the outcome

The goal is to **reduce residual variance while avoiding bias**.

# Piece 4 — Bias vs Variance Trade-off in Covariate Selection

## 1. Two potential problems when adding covariates

When including covariates in regression adjustment, two types of issues can arise:

- Bias
- Variance

Understanding the difference is critical for A/B testing and causal inference.

---

## 2. Bias

Bias occurs when the estimated treatment effect systematically deviates from the true causal effect.

A common source of bias is including **post-treatment variables**.

Example causal structure:

Treatment → Clicks → Purchases

Regression model:

Purchases = β0 + β1 * Treatment + β2 * Clicks

Because clicks are caused by the treatment, controlling for clicks blocks part of the causal pathway.

Result:

The regression estimates only the **direct effect**, not the **total effect**.

This introduces **downward bias** in the treatment estimate.

---

## 3. Variance

Variance refers to how much the estimate fluctuates due to noise.

Adding irrelevant covariates can increase variance.

Example:

Purchases = β0 + β1 * Treatment + β2 * RandomFeature

If RandomFeature does not predict the outcome:

- residual variance is not reduced
- additional parameters must be estimated

Result:

The variance of the treatment estimate increases, reducing precision.

---

## 4. The bias–variance trade-off

When choosing covariates, we want to:

- avoid introducing bias
- reduce variance when possible

Summary:

| Covariate Type | Effect |
|---|---|
Pre-treatment and predictive | reduces variance |
Pre-treatment but weak | may increase variance slightly |
Post-treatment | introduces bias |

---

## 5. Practical rule for A/B testing

Include covariates that:

- are measured before treatment
- strongly predict the outcome

Avoid covariates that:

- occur after treatment
- are unrelated to the outcome

Goal:

Reduce residual variance without introducing bias.

# Piece 5 — DAG Reasoning for Experiments

## 1. Why DAGs are useful

Directed Acyclic Graphs (DAGs) help us reason about:

- causal relationships
- which variables to control for
- which variables to avoid controlling for

The goal is to estimate the causal effect:

Treatment → Outcome

while avoiding biased estimates.

---

## 2. Confounders

Structure:

X ← Z → Y

Z influences both the treatment and the outcome.

Example:

Income → Education  
Income → Health  
Education → Health

Income is a confounder because it affects both education and health.

This creates a **backdoor path**:

Education ← Income → Health

If we do not control for the confounder, the treatment effect estimate becomes biased.

Solution:

Control for the confounder (e.g., include it in regression).

---

## 3. Mediators

Structure:

X → Z → Y

Z lies on the causal pathway from treatment to outcome.

Example:

Treatment → Clicks → Purchases

Clicks are a mediator.

If we control for a mediator, we block part of the causal effect.

Result:

The regression estimates only the **direct effect**, not the **total effect**.

Therefore, mediators should **not be controlled for** when estimating total treatment effects.

---

## 4. Colliders

Structure:

X → Z ← Y

Z is caused by both X and Y.

Example:

Talent → JobOffer ← Connections

JobOffer is a collider.

If we condition on a collider (e.g., only analyze people with job offers), we create a **spurious correlation** between Talent and Connections.

Therefore, colliders should **not be controlled for**.

---

## 5. Key rule for covariate selection

| Structure | Variable Type | Should we control? |
|---|---|---|
X ← Z → Y | Confounder | Yes |
X → Z → Y | Mediator | No |
X → Z ← Y | Collider | No |

---

## 6. Controlling for a variable

Controlling for a variable means accounting for it when estimating the treatment effect.

Common methods include:

- regression adjustment
- matching
- stratification
- weighting

Conceptually, controlling for a variable means comparing treatment and control units with **similar values of that variable**.

Example:

Purchases = β0 + β1 * Treatment + β2 * PastPurchases

This compares treatment and control users with similar past purchase levels.

---

## 7. Backdoor paths

A backdoor path is a non-causal path between treatment and outcome that introduces bias.

Example:

Treatment ← Motivation → Purchases

Motivation creates a backdoor path.

Controlling for the confounder blocks the backdoor path and removes the bias.

---

## 8. Practical takeaway for experiments

When estimating treatment effects:

Include covariates that:

- are measured before treatment
- influence both treatment and outcome (confounders)

Avoid covariates that:

- occur after treatment (mediators)
- are common effects of treatment and outcome (colliders)


# Quiz on core concepts 

## Mistakes


## Weak ones

1. What is the safest unit of randomization for most app experiments?

Correct answer:
User

Explanation:
Prevents users from experiencing inconsistent treatments across sessions.

2. Why might user-level randomization still suffer interference in ad marketplaces?

Correct answer:
Because changing supply for treated users can shift auction prices for control users

Explanation:
Experiments can affect the auction equilibrium, impacting all users.

# Core concepts

## Network Effects

- Product value increases as more users join or interact.
- More users → more interactions/content/supply → higher product value.

### Examples
- Social networks
- Marketplaces
- Multiplayer games

### Relationship to Interference

- Network effects mean users influence each other's behavior.
- In experiments, this can cause **interference (spillover)**:
  - Treatment applied to one user affects outcomes of another user.
- This violates the **independence assumption** in A/B testing.

### Why it matters

- Control group behavior may be influenced by treatment users.
- Estimated treatment effects may become **biased or diluted**.

### Mitigation

- Cluster / group randomization
- Randomize by network or region
- Monitor ecosystem-level metrics

### Interview answers

- Yes, network effects could bias the experiment.
- Recommendations based on friends' activity.
- Treated users may interact with / invite control friends.
- Control users’ engagement may increase without treatment.
- Control group becomes contaminated.
- Estimated treatment effect may be underestimated.

- Mitigation:
  - Randomize at friend-network level.
  - Put connected users in same bucket.
  - Or use cluster randomization by social community.

- If network randomization is not feasible:
  - Check for spillover evidence.
  - Analyze control outcomes by exposure to treated friends.
  - Compare control users with many treated friends vs mostly control friends.
  - Higher engagement among exposed control users → network interference likely.





## Variance Reduction
  
### Interview Answer Template

- High variance due to user heterogeneity.
- Use **predictive pre-treatment covariates** (e.g., past playtime).
- Covariate explains part of outcome variation.
- Removes noise from the metric.
- Reduces **residual variance**.
- Improves **precision of treatment effect estimate**.
- Increases **statistical power**.

## Bias vs Variance – Covariate Selection

- Use **pre-treatment variables**.
- Strong predictors of the outcome → reduce variance.

- Avoid **post-treatment variables**.
- Treatment → mediator → outcome.
- Controlling mediator blocks part of treatment effect.
- Introduces **bias / underestimates treatment effect**.

### Key Rule

- Pre-treatment covariates → **variance reduction**.
- Post-treatment covariates → **bias**.



# Mock with William:
1. Pros and cons between simple and stratifying randomnization

2. What specific covariates would you use for a case?

3. Explain p-value

4. Explain power

5. What if we cannot do AB test, what to use? Quasi

6. Metric goes up at first, then goes down, why? Novelty effect

7. A metric moves differently for subgroups under a big metric

8. Guardrails they use mostly are one each level at funnel