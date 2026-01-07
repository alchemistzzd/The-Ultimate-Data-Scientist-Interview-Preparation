# Bias vs Variance vs Noise
## Bias
Impact: Cosistently incorrect predictions, high bias results in underfit
Cause: Error from poor model assumptions

## Variance
Impact: Inconsistently predictions, high vairance results in overfit
Cause: Error from over complex models that are too sensitive to training data

## Noise
Impact: Noise sets lower bound in genelization error
(*Genelization error: error that a model makes on unseen data)
Cause: Irreducible error inherent to the problem. Eg. you cannot predict the outcome of a flip of a
fair coin any more than 50% of the time.

## Solutions for high bias
1. Add more data for training

## Solutions for high variance
1. Constrain model flexibility through regularization


# Likelihood vs Probabilities
[Bayes for Beginners: Probability and Likelihood](../References/2015-APS-Bayes-for-Beginners-1-Probability-and-Likelihood---Association-for-Psychological-Science.pdf)
## Probability
Forward-looking, model -> data, attach to results; probabilities that attach to the possible results sum to 1. Probability treats parameters as fixed and data as random.
Input: model parameters
Variable: data
Output: a distribution over data given parameters
P(data|parameters) 

## Likelihood
Backward-looking, data -> model, attach to hypotheses on the model; the hypotheses to which likelihoods attach are often not mutually exclusive or exhaustive, eg. two hypothese could be overlapping. Likelihood treats data as fixed and parameters as variable.
Input: data result
Variable: model parameters
Output: a function over parameters given fixed data
L(parameters|data) = P(data|parameters) 

# Maximum Likelihood Estimation (MLE) vs Bayesian Estimation
[2015-APS-Bayes-for-Beginners-1-Probability-and-Likelihood---Association-for-Psychological-Science](../References/2015-APS-Bayes-for-Beginners-1-Probability-and-Likelihood---Association-for-Psychological-Science.pdf)
## MLE
When you know the likelihood function, find the model parameters that yield the maximum of the likelihood function given the data observed. Then using the found model parameter to make predictions. Model parameter is treated as fixed, and uncertainty is ignored.

## Bayesian Estimation
Taking both likelihood and prior into consideration, and make predictions by estimating the posterior probability and the prior. Model parameter is treated as a variable, uncertainty is considered. Final prediciton is a weighted average of all predictions.

When to use which?
1. How much data do you have?
MLE solely depends on the observed data, when dataset is small it becomes easily biased. In this case, BE is better

2. How reliable is the knowledge for the prior?
If prior is not reliable or you are unsure, MLE is better, especially if you have a sufficient amount of data.

3. How much computational resources you have?
Bayesian computations are more complex then MLE. If you are restrained by resources, MLE is better.

# Generative vs Discriminative models


# Decision boundary
A decision boundary in machine learning is the line, curve, or surface that separates different classes or outcomes in a feature space, showing where a model changes its prediction from one category to another

## Why in KNN, k = 1 has a lower bias than k = 100?
Bias = error from overly simple assumptions. High bias means the model can’t represent the true pattern.
Think of it from a decision boundary perspective, k = 1 has a more jagged and flexible decision boundary because it only cares the 1 neighbor near it, hence lower bias; while k = 100 has a much more smooth decision boundary because it averages over a lot of neighbors, hence higher bias and lower variance.