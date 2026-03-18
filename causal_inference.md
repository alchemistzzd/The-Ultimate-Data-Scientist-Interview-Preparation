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

4. Start by listing steps for AB testing, and ask interview which part do they want to dive into?


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

Quasi experimental methods:
Instrumental Variables (IV)
Definition: A method that uses a third variable (the "instrument") that is correlated with the treatment but does not have a direct effect on the outcome, nor is it correlated with the error term (confounders). This isolates the causal effect of the treatment.
Example: To study the effect of education on earnings, researchers might use the distance a student lives from a college as an instrument. Distance affects the likelihood of attending college but is generally unrelated to an individual's innate earning potential.

Matching
Definition: A technique where treated units are paired with untreated (control) units that have similar observable characteristics (covariates). The goal is to create a control group that looks as much like the treatment group as possible.
Example: Comparing the health outcomes of two groups of patients who have the same age, weight, and medical history, where one group received a new drug and the other did not.

Propensity Score
Definition: This method estimates the probability (propensity) of a unit receiving treatment based on observed characteristics. Researchers then match, stratify, or weight units based on these scores to balance the treatment and control groups.
Example: If wealthier people are more likely to join a voluntary job training program, a propensity score would calculate the likelihood of joining based on income. Outcomes are then compared between people with the same "propensity" to join, regardless of whether they actually did.

Difference-in-Differences (DiD)
Definition: This method compares the change in outcomes over time between a treatment group and a control group. It assumes that, without the treatment, the two groups would have followed the same "trend" over time.
Example: Comparing the change in employment rates in a city that implemented a minimum wage increase versus a neighboring city that did not, both before and after the policy change.

Synthetic Control
Definition: Used primarily for case studies with a single treated unit (like a state or country). It involves creating a weighted combination of multiple control units (a "synthetic" version) that closely matches the treated unit's pre-treatment characteristics.
Example: Estimating the economic impact of a tobacco control law in California by creating a "Synthetic California" composed of a weighted average of other states that did not pass the law.

Regression Discontinuity Design (RDD)
Definition: This method exploits a specific cutoff or threshold that determines who receives treatment. Units just above the threshold are compared to those just below it, as they are assumed to be nearly identical except for the treatment.
Example: Evaluating the effect of a scholarship awarded only to students who score above 90 on an exam. Students who scored 89 (control) are compared to those who scored 91 (treated).

Fixed Effects (Panel Data)
Definition: A method used with data collected over multiple time periods for the same units. It controls for unobserved characteristics of those units that do not change over time (e.g., a person's personality or a city's geography).
Example: Analyzing the effect of local traffic laws on accident rates across different cities by looking only at changes within each city over several years, which controls for permanent differences between the cities.



# Ads on Homepage A/B Testing — Mock Interview Notes

## Q: How would you evaluate the impact? What metrics would you track?
A: I would assume the goal is to increase ad revenue while maintaining user experience. The primary metric would be revenue per user or revenue per session. Supporting metrics would include ad impressions and click-through rate to understand user interaction with ads. Guardrail metrics would include retention, engagement metrics like session frequency or bounce rate, and system metrics like latency or crash rate to ensure we are not degrading user experience.

---

## Q: How would you determine sample size and experiment duration?
A: Sample size depends on significance level (alpha), power, minimum detectable effect (MDE), and variance of the metric. Once the required sample size is determined, experiment duration depends on traffic allocation. The experiment should run until enough samples are collected and should cover natural temporal patterns such as weekday versus weekend behavior.

---

## Q: If the experiment ran for only 3 days and shows significant positive results, what could be wrong?
A: This could be due to peeking or early stopping, which inflates the false positive rate. The sample size may not be sufficient, making results unstable. Temporal effects like weekday versus weekend differences may not be captured. There may also be novelty effects where users initially react differently. Additionally, short duration may fail to capture long-term effects such as retention or user fatigue.

---

## Q: What else should we be careful about in this ads experiment?
A: We should check for data quality issues such as heavy-tailed distributions, outliers, bots, and sample ratio mismatch. From a product perspective, ads may negatively impact user experience, so engagement and retention should be monitored. We should consider exposure bias since not all users may see the ads depending on placement. It is also important to analyze heterogeneous treatment effects across user segments. Logging accuracy for impressions and clicks should be validated. Finally, long-term effects such as ad fatigue or retention drops should be considered.

---

## Q: How does regression adjustment help in A/B testing?
A: Regression adjustment reduces variance by controlling for pre-treatment covariates that explain user behavior differences. This improves statistical power without introducing bias, since randomization already ensures unbiased estimates.

---

## Q: How does regression adjustment improve power?
A: It reduces the variance of the outcome, which lowers the standard error of the treatment effect estimate. This makes it easier to detect statistically significant effects without increasing sample size.

---

## Q: What is the difference between regression adjustment and regression in observational studies?
A: Regression adjustment in A/B testing is used to reduce variance since randomization already ensures unbiased estimates. In observational studies, regression is used to control for confounding and obtain unbiased estimates, assuming no unobserved confounders.

---

## Q: If you cannot run an A/B test, what methods would you use?
A: I would use quasi-experimental methods such as difference-in-differences if I have before-and-after data with a control group, matching or regression to control for observed confounders if treatment is self-selected, or instrumental variables if there is unobserved confounding and a valid instrument is available.

---

## Q: How do instrumental variables isolate causal effect?
A: Instrumental variables use an external factor that influences treatment but is independent of confounders and affects the outcome only through treatment. This isolates the variation in treatment that is as good as random, allowing causal estimation.

---

## Q: How do DiD, regression/matching, and IV compare?
A: Difference-in-differences uses time-based changes between treatment and control groups. Regression or matching controls for observed confounders by comparing similar users. Instrumental variables use external variation to handle unobserved confounding, but rely on strong assumptions.


Homepage ranking / recommendations:
time spent, game join rate, sessions per user, retention (D1/D7), CTR on recommendations

Search ranking / discovery:
search CTR, game join rate, success rate (search → play), time to first play

Game recommendation system (“For You”):
engagement time, diversity of games played, retention, repeat visits

UI / UX changes (homepage, navigation):
bounce rate, session length, clicks to key actions, retention

Ads placement / ads section:
revenue per user (ARPU), impressions, CTR, ad conversion, retention (guardrail), session time

Notifications (push / in-app):
open rate, CTR, re-engagement rate, sessions per user, retention

Social features (friends, chat, invites):
messages sent, invites sent, co-play rate, sessions with friends, retention

In-game economy / monetization (Robux, bundles):
revenue per user, payer conversion rate, average spend, purchase frequency

Creator tools / marketplace changes:
creator revenue, number of active creators, content uploads, player engagement in new games

Performance improvements (latency, load time):
session start success rate, time to load, crash rate, session length, retention

Safety / moderation features:
report rate, moderation actions, user retention, user satisfaction signals 