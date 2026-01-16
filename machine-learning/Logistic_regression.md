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
- Linear relationship between feature and target variables
- Error is normally distributed ~(0,/sigma^2). Error is the part of the target variable that linear model cannot explain (measurement noise, unobserved variables, random fluctuations), this assumption came from Central Limit Theorem intuition
What happens if errors are NOT normal?
- Variance of the error is constant, uncertainty around the prediction is constant no matter how big or small is the features and predictions.
What happens if variance is NOT constant?
- All feature variables are not correlated, no multicollinearity
What happens if there is multicollinearity?
- All data points(observations) are independant from each other, no autocorrelation
What happens if there is autocorrelation?

## Algorithm (step-by-step)
What is the cost function?

```text
Algorithm <Name>
Input: ...
Output: ...
for i in 1..N:
    ...
return ...