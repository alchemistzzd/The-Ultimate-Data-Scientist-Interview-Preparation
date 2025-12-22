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
$$
P(\text{data} \mid \text{parameters})
$$

## Likelihood
Backward-looking, data -> model, attach to hypotheses on the model; the hypotheses to which likelihoods attach are often not mutually exclusive or exhaustive, eg. two hypothese could be overlapping. Likelihood treats data as fixed and parameters as variable.
Input: data result
Variable: model parameters
Output: a function over parameters given fixed data
$$
L(\text{parameters} \mid \text{data}) = P(\text{data} \mid \text{parameters})
$$