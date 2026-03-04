# Overfitting

**Summary:** How to deal with overfitting

---

## Table of contents

- [Variance subset selection](#variance-subset-selection)
- [Regularization](#regularization)
- [Dimentionality reduction](#dimentionality-reduction)

---

## Variance subset selection

**Benefits:**

1. Computationally cheaper and faster with less dimentions. Espesically for some algorithm that scales badly with dimentional increase
2. Generalization performance increase. Redundant and irrelevant features can confuse algorithms
3. Training data need descrease. Usually less features means less training data needed

**Methods**

1. **Wrapper methods:** search for subsets of features that perform well
   - **Forward selection:** start with no feature, include one feature at a time that improves performance the most, stop when a desired number of features is reached;
   - **Backward selection:** start with all features, exclude one feature at a time that reduces performance the least, stop when a desired number of features is reached
   - **Downside:** requires retraining the model so can be computationally expensive

2. **Embedded methods:** reduce the variance by simplifying the model during training

---

## Regularization (aka Shrinkage)

Adjust the cost/loss function to penalize larger parameters by adding a penalty term, so instead of minimizing Error of cost function we are minimizing Error+Penalty. Regularization reduces variance. L1 or LASSO performs variable selection.

Regularization forces "Boring" models: By penalizing large weights, you prevent the model from over-reacting to outliers or noise.

Stability: Because the weights are kept small, the model becomes more stable. It focuses on the broad "signal" that exists across all data points rather than the "noise" unique to a few.

### 1. Ridge regularization (L2)

**The "Fair" Manager:**

- **The Policy:** "Everyone can stay, but everyone must be quiet."
- **How it works:** It penalizes the square of the weights. This makes it very expensive to have huge weights, but very cheap to have tiny ones.
- **The Vibe:** It keeps all your variables in the model but shrinks their influence. It's great when you think every feature has a little bit of value.

L2's penalty is quadratic, meaning the pressure effectively vanishes as the weight gets smaller, so it shrinks weights but keeps all features in the model to maintain stability.

**Benefits:** handles multicollinearity well

### 2. LASSO regularization (L1)

**The Policy:** "If you aren't providing massive value, you're fired."

- **How it works:** It penalizes the absolute value of the weights. Mathematically, this "tax" is constant even as the weight gets small, eventually pushing it all the way to zero.
- **The Vibe:** It performs Feature Selection. It leaves you with a simple, clean model that only uses the most impactful variables.

L1 uses a constant gradient, so the pressure to simplify the model stays strong all the way to the origin, which results in feature selection

**Benefits:** reduces number of predictors and yields sparse models

### 3. Elastic net

\(a \cdot L1 + b \cdot L2\)

It uses the \(L_2\) part to keep the correlated variables together (the "grouping effect") and the \(L_1\) part to zero out the truly useless noise.

- **The \(L_2\) Tax:** Ensures that if variables are correlated, their weights are shrunk together rather than one being destroyed.
- **The \(L_1\) Tax:** Ensures that if a variable (or a group of variables) adds no value at all, it eventually gets set to zero.

---

## Dimentionality reduction

### PCA (Principle Components Analysis)

**Intuition:** Transform the data from a high dimensional space to a lower dimensional subspace, while minimizing the projection error. Selecting the principle components that maximizes variances of the data when projecting the data to those components.

**Steps:**

1. Normalize each feature to mean zero and a standard deviation of 1 (Why? By normalizing (Standardization), you put both features on a level playing field. You give them a mean of \(0\) and a standard deviation of \(1\), regardless of magnitude of the units)
2. Determine the principal components. Calculate the eigenvectors and eigenvalues of the data covariance matrix. Eigenvectors in descending order of their eigenvalues are the principal components
3. Project the data features on the principal components
4. Keep the top X principal components to reduce into a lower dimension

**Benefits:**

- Dimensionality reduction
- Feature extraction
- Data visualization
- Lossy data compression

### Others

- Kernel PCA
- Random projections
- Multidimensional scaling
- Locality sensitive hashing
- Autoencoders
- Isomap
