# Classification Evaluation Metrics

> **Summary:** The metrics used to evaluate classification models' performances. Precision, recall (sensitivity), ROC, AUC, Type I error, Type II error.

---

## Table of Contents

- [When to Use](#when-to-use)
- [Intuition](#intuition)
- [Interview Questions](#interview-questions)

---

## When to Use

- Evaluating performances of classification models

---

## Intuition

### Error Types

| Error | Meaning | Intuition |
|-------|--------|-----------|
| **Type I** | False positive | (Over confident!) false positive |
| **Type II** | False negative | (Over inconfident!) false negative |

---

### Recall (Sensitivity)

**True Positive Rate (TPR)**

$$\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$

- The **"Safety metric"**: if you are wrong and miss a case, someone will get hurt.
- (Low recall, false negative is high, missing too much of the actual cases, too conservative.)
- High Sensitivity means you can **trust a Negative result** (because if it were positive, the test would have found it).

---

### Precision (Positive Predictive Value, PPV)

$$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$

- The **"Annoyance metric"**: if you are wrong and over accuse, you are just annoying.
- (Low precision, high false positive, you are over accusing.)

---

### False Positive Rate

$$\text{FPR} = \frac{\text{False Positives}}{\text{False Positives} + \text{True Negatives}} = 1 - \text{Specificity}$$

- Probability of **false alarm**: how many non-targets are incorrectly classified as targets?

---

### True Negative Rate (Specificity)

$$\text{Specificity} = \frac{\text{True Negatives}}{\text{True Negatives} + \text{False Positives}}$$

- High Specificity meaning very picky, meaning less false positive, but might miss some real positive cases since the bar is very high.
- High Specificity means you can **trust a Positive result** (because the test is so picky, it wouldn't have flagged it unless it was really there).

---

### F1 Score

The F1 score is the **harmonic mean of Precision and Recall**. It is the most popular metric for imbalanced datasets because it punishes models (e.g. extreme imbalance).

$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

**Generalized: Fβ score**

$$F_\beta = (1 + \beta^2) \cdot \frac{\text{Precision} \cdot \text{Recall}}{(\beta^2 \cdot \text{Precision}) + \text{Recall}}$$

The rule of thumb is simple: \(\beta\) is the **"Recall Multiplier."**

| β | Interpretation |
|---|----------------|
| **β = 1** | You get the F1 Score (Balanced). |
| **β > 1** (e.g. \(F_2\)) | You care more about Recall. You want to find all the positives, even if it means more false alarms. |
| **β < 1** (e.g. \(F_{0.5}\)) | You care more about Precision. You want to be very sure when you call something "Positive," even if you miss a few cases. |

**Multiclass F1:**

- **Micro-average:** Calculate metrics globally by counting the total true positives, false negatives, and false positives.
- **Macro-average:** Use the average precision and recall for each class label.

---

### Confusion Matrix

- **X-axis:** Predicted class  
- **Y-axis:** Actual class  

```
                Predicted
                Neg    Pos
Actual  Neg   [ TN     FP ]
        Pos   [ FN     TP ]
```

---

### ROC Curve (Receiver Operating Characteristic)

The ROC graph summarizes **all of the confusion matrices that each threshold produced**.

- **X-axis:** False Positive Rate  
- **Y-axis:** True Positive Rate  

**Line *x* = *y*:** Any point on this line means the proportion of correctly classified positive samples is the same as the proportion of incorrectly classified samples that are actually negative.

---

### AUC (Area Under the Curve)

**1. Graph definition**

- Area under ROC curve, between 0 and 1. It measures how well the classifier separates classes.
- The most optimal curve is the one hugging left top of the plot, indicating a high True positive rate and a low False positive rate.

**2. Statistical definition**

- The AUC is the probability that a randomly chosen positive instance will be ranked higher by the model than a randomly chosen negative instance:

$$P\bigl(\text{score}(x_{\text{pos}}) > \text{score}(x_{\text{neg}})\bigr)$$

- If you have \(n_p\) positive samples and \(n_n\) negative samples, the relationship is:

$$\text{AUC} = \frac{U}{n_p \times n_n}$$

- This is why AUC is called a **non-parametric** metric. It doesn't care about the mean or variance of your scores; it only cares about the ordinal rank.

---

## Interview Questions

### 1. "Explain the difference between Precision and Recall to a non-technical stakeholder."

> **The Answer:** Precision is about **quality** (out of everyone we flagged as "high risk," how many actually were?).  
> Recall is about **quantity** (out of everyone who actually was "high risk," how many did we successfully find?).

---

### 2. "Why can't we just use Accuracy for imbalanced datasets?"

> **The Answer:** If 99% of your data is "Not Fraud," a model that predicts "Not Fraud" for every single case will have 99% accuracy but 0% recall for the fraud class. It is completely useless for the actual task. Precision and recall force the model to account for the minority class.

---

### 3. "Mathematically, what happens to Precision and Recall if I lower the classification threshold from 0.5 to 0.1?"

*(The threshold here is not the threshold on ROC curve, but the model threshold.)*

> **The Answer:** Lowering the threshold makes the model "laxer."  
> - **Recall increases:** You catch more true positives because the net is wider.  
> - **Precision decreases:** You also catch more "noise" (false positives), polluting your results.

---

### 4. "Is it possible to have 100% Precision and 100% Recall simultaneously?"

> **The Answer:** In theory, yes, for a perfect model that makes zero errors (\(FP = 0\) and \(FN = 0\)). In reality, almost never. Improving one typically incurs a cost to the other because decision boundaries in real-world data are rarely perfectly separable.

---

### 5. "Describe the Precision-Recall (PR) Curve. What does the Area Under the Curve (AUC-PR) tell us?"

> **The Answer:** The PR curve plots precision (\(y\)-axis) vs. recall (\(x\)-axis) for every possible threshold. The AUC-PR summarizes the overall performance across all thresholds. It is often preferred over the ROC curve when the positive class is extremely rare, as it doesn't get inflated by a large number of True Negatives.

---

### 6. Concrete case scenario

**"You are building a cancer screening model. Which metric do you prioritize?"**  
**"You are building a 'Spam' filter for Gmail. Which metric is more important?"**

> **The Answer:**  
> - If missing a positive case in this scenario is **fatal** (e.g. a missed diagnosis), we have to keep False negative low, which means we need to make sure **Recall is high**.  
> - If a **False positive** will be more of a concern (e.g. an important email gets classified as spam), we want to keep the False positive low, which means we need to make sure **Precision is high**.  
> - If we want a **balance** between the two and need a single number to compare different models: use **F1**. Since it is the harmonic mean, it severely punishes extreme values. If your precision is 1.0 but recall is 0.01, your F1-score will be near zero.

| Scenario | Priority |
|----------|----------|
| Cancer screening (missing positive = fatal) | **Recall** |
| Spam filter (false positive = important email as spam) | **Precision** |
| Balance, single number | **F1** (harmonic mean punishes extremes) |

---

### 7. "If your model has high Recall but very low Precision, how do you 'fix' it without retraining?"

> **The Answer:** You increase the classification threshold. By requiring the model to be more "confident" before it predicts a positive label, you filter out the low-probability false positives, which raises precision (though it will inevitably drop some true positives, lowering recall).
