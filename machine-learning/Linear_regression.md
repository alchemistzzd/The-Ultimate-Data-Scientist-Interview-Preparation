# Linear Regression

**Type**:  Supervised | Regression | Classification | Non-parametric

**Summary**:  The basic idea is to find the ‘k’ closest data points in the training set to a given test data point and use the labels of those closest points to make a prediction for the test point.

## Table of contents
- [When to use](#when-to-use)
- [Intuition](#intuition)
- [Formal definition / math](#formal-definition--math)
- [Algorithm (step-by-step)](#algorithm-step-by-step)
- [Interview questions](#interviewquestions)


---

## When to use
- When to model linear relationships

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
What is the metric for evaluation?
- Mean squared error (MSE)
- Mean absolute error(MAE)
- R2,coefficient of determination: Proportion of the response variable variation explained by the model
- Adjusted R2: since R2 increases with more predictor variables regardless of relevance, Adjusted R-squared modifies this value, penalizing the model for adding irrelevant variables. Use  to compare models with different numbers of predictors, as it only increases if new variables improve the model. Adjusted R2 is always <= R2
- Explained variance ?

```text
Algorithm <Name>
Input: ...
Output: ...
for i in 1..N:
    ...
return ...

## Interview questions