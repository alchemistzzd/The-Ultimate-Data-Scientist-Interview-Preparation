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
