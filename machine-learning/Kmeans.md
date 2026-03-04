# Kmeans

**Type:** Unsupervised | Clustering | Parametric

**Summary:**

---

## Table of contents

- [When to use](#when-to-use)
- [Intuition](#intuition)
- [Assumptions](#assumptions)
- [Algorithm (step-by-step)](#algorithm-step-by-step)
- [Tradeoff](#tradeoff)
- [Hyperparameters](#hyperparameters)
- [Implementation (python)](#implementation-python)
- [Practical tips & gotchas](#practical-tips--gotchas)
- [Experiments / example](#experiments--example)
- [References & further reading](#references--further-reading)
- [Exercises / extension ideas](#exercises--extension-ideas)
- [Changelog](#changelog)

---

## When to use

- When need to group data into different clusters

---

## Intuition

- It is a unsupervised learning algorithm because the training data don't have labels

---

## Assumptions

1. **Kmeans algorithm assumes the clusters are Gaussians centered at the mean**
   - Points in a cluster are concentrated near the center
   - Density decreases smoothly as you move away
   - The shape is blob-like
   - assumes spherical clusters

2. **Each cluster has identical covariance matrices**
   - All clusters have the same size and shape
   - Only their centers differ

3. **All features are independent**  
   Since K-Means uses Euclidean distance, it assumes features are uncorrelated and equally scaled. This corresponds to a spherical covariance matrix where off-diagonal covariance terms are zero.

---

## Algorithm (step-by-step)

1. Step 1 — Select k
2. Step 2 — Randomly initiate k mean values
3. Step 3 — Calculate distance between each observation and means. Assign all observations to the nearest mean
4. Step 4 — Update the mean to be the centroid of the labeled data
5. Step 5 — Repeat step 3 and 4 until convergence (no means need to be updated)

---

## Tradeoff

### 1. How to choose k?

- **Elbow method** (Using a line chart where: x is different k, y is sum of squared errors)  
  Run k-means for various k; Choose the value of k at the "elbow" of the curve; Increasing k will improve the fit, but at the cost of potentially overfitting the data
- **Other approaches:** silhouette (graphical approach to evaluating cluster fit), Akaike information criterion (AIC) and Bayesian information criterion (BIC) measure relative quality of models and factors in the number of parameters

### 2. Benefits over other clustering methods

1) Converges very quickly  
2) Excels with clusters with equal varirance (?)

### 3. When it struggles

1) Nonliear boundaries between clusters  
2) When there are variations in cluster variance (?)  
3) When there are correlation between features (?)
