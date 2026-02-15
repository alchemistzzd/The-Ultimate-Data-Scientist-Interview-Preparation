# Logistic Regression

**Type**:  Supervised | Regression | Classification | Non-parametric

**Summary**:  Moving from linear regression to classification, if you put a sigmoid function over the linear regression model, you get logistic regression. It models the probability that features belong to a class.

## Table of contents
- [When to use](#when-to-use)
- [Intuition](#intuition)
- [Formal definition / math](#formal-definition--math)
- [Algorithm (step-by-step)](#algorithm-step-by-step)
- [Complexity](#complexity)
- [Hyperparameters](#hyperparameters)
- [Implementation (python)](#implementation-python)
- [Practical tips & gotchas](#practical-tips--gotchas)
- [Experiments / example](#experiments--example)
- [References & further reading](#references--further-reading)
- [Exercises / extension ideas](#exercises--extension-ideas)
- [Changelog](#changelog)

---

## When to use
- When need to classify data in to different groups

## Intuition
- Linear models are linear in the parameters, not in input features
- How to model non linear relationships? Transform the features, and make linear models on the transformed features

## Assumptions
-Linearity of the Log-Odds: Logistic Regression assumes a linear relationship between the log-odds of the dependent variable and the independent variables. Deviations from linearity can impact the model’s accuracy.
Independence of Observations: Each observation should be independent of others. In scenarios like time-series data, where observations may be correlated, violating this assumption can affect the model’s reliability.
-Absence of Multicollinearity: The assumption of no multicollinearity suggests that predictor variables should not be highly correlated. High multicollinearity can make it challenging to assess the individual impact of each variable.
-No Outliers: Outliers can disproportionately influence the model, affecting coefficients and potentially leading to erroneous conclusions. Robust techniques or data transformations may be necessary to mitigate their impact.
-Binary or Ordinal Dependent Variable: Logistic Regression is designed for binary or ordinal outcomes. Attempting to apply it to non-binary problems can yield inaccurate results.

## Algorithm (step-by-step)
What is the cost function?
Mean Square Error vs Cross Entropy
**Mean Square Error**
Using maximum likelihood, Goal is to find the value of p that maximizes the likelihood of our data.
𝑃(𝑋 = 1)= 𝑝
𝑃(𝑋 = 0)= 1 − 𝑝
𝐿(𝑥𝑖)= 𝑃 (𝑥𝑖 |𝑝) = 𝑝^𝑥𝑖 * (1 − 𝑝)^1−𝑥𝑖

Log transformation -> derivative

This results in our estimate being the mean of our observations.

**Cross Entropy**
Think of logistic regression as modeling probability that features belong to a class




Algorithm <Name>
Input: ...
Output: ...
for i in 1..N:
    ...
return ...