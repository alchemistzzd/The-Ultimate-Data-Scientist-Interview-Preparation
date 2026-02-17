# Classification Evaluation Metrics

**Summary**:  The metrics used to evaluate classificaiton models' performances. Precision, recall(sensitivity), ROC, AUC, type 1 error, type 2 error

## Table of contents
- [When to use](#when-to-use)
- [Intuition](#intuition)


---

## When to use
- Evaluating performances of classification models

## Intuition
- Type 1 error: (over confident!) false positive
- Type 2 error: (over inconfident!) false negetive

- Recall (or Sensitivity in medicine): 

True positive rate(TPR, sensitivity)
= True positive / (True positive + False negative)
The "Safety metric", if you are wrong and miss a case, someone will get hurt. (Low recall,false negative is high, missing too much of the actual cases, too conservative)
High Sensitivity means you can trust a Negative result (because if it were positive, the test would have found it).

- Precision 

Positive preditive value(PPV)
= True positive / (True positive + False positive)
The "Annoyance metric", if you are wrong and over accused, you are just annoying. (Low precision, high false positive, you are over accusing)

- False positive rate

= False positive / (False positive + True negative)
= 1- Specificity
Probability of false alarm, how many non-targets are incorrectly classified as targets?

- True negative rate

Specificity
= True negative / (True negative + False positive)
High Specificity meaning very picky, meaning less false positive, but might miss some real positive cases since the bar is very high.
High Specificity means you can trust a Positive result (because the test is so picky, it wouldn't have flagged it unless it was really there).

- F1 score

The F1 score is the harmonic mean of Precision and Recall. It is the most popular metric for imbalanced datasets because it punishes models

$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

While F1 score treats Precision and Recall equally, we can further expand F1 to $F_\beta$

$$F_\beta = (1 + \beta^2) \cdot \frac{\text{Precision} \cdot \text{Recall}}{(\beta^2 \cdot \text{Precision}) + \text{Recall}}$$

The rule of thumb is simple: $\beta$ is the "Recall Multiplier."

$\beta = 1$: You get the F1 Score (Balanced).

$\beta > 1$ (e.g., $F_2$): You care more about Recall. You want to find all the positives, even if it means more false alarms.

$\beta < 1$ (e.g., $F_{0.5}$): You care more about Precision. You want to be very sure when you call something "Positive," even if you miss a few cases.

- Confusion Matrices

X axis: Predicted class
Y axis: Actual class

- ROC curves(Receiver Operating Characteristics curves)

The ROC graph summarizesall of the confusion matricesthat each threshold produced.
X axis: False positive rate
Y axis: True positive rate

The line x=y means: Any point on this line means the proportion of correctly classified positive samples is the same the proportion of incorrectly classified samples that are actually negative

- AUC(area under the curve)

1. Graph definition
Area under ROC curve, between 0 and 1. It measures how well the classifier separates classes.
The most optimal curve is the one hugging left top of the plot, indicating a high True positive rate and a low False positive rate.

2. Statistical definition
The AUC is the probability that a randomly chosen positive instance will be ranked higher by the model than a randomly chosen negative instance.

$$P(\text{score}(x_{pos}) > \text{score}(x_{neg}))$$

If you have $n_p$ positive samples and $n_n$ negative samples, the relationship is:

$$\text{AUC} = \frac{U}{n_p \times n_n}$$

This is why AUC is called a non-parametric metric. It doesn't care about the mean or variance of your scores; it only cares about the ordinal rank.

