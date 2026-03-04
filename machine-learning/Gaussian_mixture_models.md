# Gaussian Mixture Models (GMM)

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
- Density estimation

---

## Intuition

- It is a unsupervised learning algorithm because the training data don't have labels

---

## Assumptions

- GMM algorithm assumes a weighted average of density functions
- For clustering, GMM assumes the clusters are Gaussians centered at the mean, but with differernt covarance matrics (clusters can have different shapes)
- For clustering, GMM does not assume all features are independent (While GMMs can be configured with diagonal covariance (assuming independence) to reduce computation or prevent overfitting on small datasets, the general GMM framework uses full covariance to capture feature relationships.)

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
