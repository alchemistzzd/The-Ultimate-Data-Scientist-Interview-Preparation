# Bias vs Variance vs Noise

## Bias

- **Impact:** Cosistently incorrect predictions, high bias results in underfit
- **Cause:** Error from poor model assumptions

---

## Variance

- **Impact:** Inconsistently predictions, high vairance results in overfit
- **Cause:** Error from over complex models that are too sensitive to training data

---

## Noise

- **Impact:** Noise sets lower bound in genelization error  
  (*Genelization error: error that a model makes on unseen data)
- **Cause:** Irreducible error inherent to the problem. Eg. you cannot predict the outcome of a flip of a fair coin any more than 50% of the time.

---

## Solutions for high bias

1. Add more data for training

---

## Solutions for high variance

1. Constrain model flexibility through regularization

---

# Likelihood vs Probabilities

[Bayes for Beginners: Probability and Likelihood](../References/2015-APS-Bayes-for-Beginners-1-Probability-and-Likelihood---Association-for-Psychological-Science.pdf)

## Probability

- **Forward-looking,** model -> data, attach to results; probabilities that attach to the possible results sum to 1. Probability treats parameters as fixed and data as random.
- **Input:** model parameters  
- **Variable:** data  
- **Output:** a distribution over data given parameters  
- \(P(\text{data}|\text{parameters})\)

## Likelihood

- **Backward-looking,** data -> model, attach to hypotheses on the model; the hypotheses to which likelihoods attach are often not mutually exclusive or exhaustive, eg. two hypothese could be overlapping. Likelihood treats data as fixed and parameters as variable.
- **Input:** data result  
- **Variable:** model parameters  
- **Output:** a function over parameters given fixed data  
- \(L(\text{parameters}|\text{data}) = P(\text{data}|\text{parameters})\)

---

# Maximum Likelihood Estimation (MLE) vs Bayesian Estimation

[2015-APS-Bayes-for-Beginners-1-Probability-and-Likelihood---Association-for-Psychological-Science](../References/2015-APS-Bayes-for-Beginners-1-Probability-and-Likelihood---Association-for-Psychological-Science.pdf)

## MLE

When you know the likelihood function, find the model parameters that yield the maximum of the likelihood function given the data observed. Then using the found model parameter to make predictions. Model parameter is treated as fixed, and uncertainty is ignored.

## Bayesian Estimation

Taking both likelihood and prior into consideration, and make predictions by estimating the posterior probability and the prior. Model parameter is treated as a variable, uncertainty is considered. Final prediciton is a weighted average of all predictions.

**When to use which?**

1. **How much data do you have?**  
   MLE solely depends on the observed data, when dataset is small it becomes easily biased. In this case, BE is better

2. **How reliable is the knowledge for the prior?**  
   If prior is not reliable or you are unsure, MLE is better, especially if you have a sufficient amount of data.

3. **How much computational resources you have?**  
   Bayesian computations are more complex then MLE. If you are restrained by resources, MLE is better.

---

# Decision boundary

A decision boundary in machine learning is the line, curve, or surface that separates different classes or outcomes in a feature space, showing where a model changes its prediction from one category to another

## Why in KNN, k = 1 has a lower bias than k = 100?

Bias = error from overly simple assumptions. High bias means the model can't represent the true pattern.

Think of it from a decision boundary perspective, k = 1 has a more jagged and flexible decision boundary because it only cares the 1 neighbor near it, hence lower bias; while k = 100 has a much more smooth decision boundary because it averages over a lot of neighbors, hence higher bias and lower variance.

## Data snooping

If a test data set has affected **any** step in thelearning process, its ability to assess the outcomehas been compromised

## Difference between using training data to learn model parameters and using validation data to learn model hyperparameters

**Training Data: Learning Parameters**

Parameters are the variables the model learns automatically during the training process. Eg. The weights (\(w\)) and biases (\(b\)) in a neural network, or the coefficients in a linear regression.

**Validation Data: Learning Hyperparameters**

Hyperparameters are the settings you (the Data Scientist) choose before training begins. The model cannot learn these on its own. Eg. The learning rate, the number of layers in a neural network, the "depth" of a decision tree, or the \(k\) in K-Nearest Neighbors.

## Bootstrap sampling

Sampling with replacement. Often used to estimate standard errors and confidence intervals. Integral part of model ensembles (i.e. bagging in random forests)

**Why can't we use Training Data for both?**

If you use training data to pick hyperparameters, you will always pick the most complex model possible. For example, a Decision Tree with "infinite depth" will have 100% accuracy on the training data because it can just create a unique rule for every single row. However, it will fail miserably in the real world. The Validation Data acts as a "reality check"—it tells you if your hyperparameter choices are actually helping the model generalize or if they are just helping it memorize.

## Generative model vs Discrimitive model

**Discriminative Models: \(P(y|x)\)**

- **Core Focus:** Finding the Decision Boundary. It only cares about the line that separates "Class A" from "Class B."
- **Data Efficiency:** Usually requires less data because it only needs to learn the differences, not the whole distribution.
- **Outliers:** Can be sensitive to outliers if they happen to sit right on the decision boundary.
- **Primary Use:** Standard Classification (e.g., Logistic Regression), Sentiment Analysis, and Neural Networks.

**Generative Models: \(P(x|y)\)**

- **Core Focus:** Modeling Data Distributions. It learns the "profile" or "essence" of each class.
- **Data Efficiency:** Often needs more data to accurately model the "shape" of how the data was generated.
- **Outliers:** Robust at detecting outliers because it knows what a "normal" data point should look like for that class.
- **Primary Use:** Generating new data (e.g., GANs, LLMs), handling missing data, and Naive Bayes.

---

# EM steps (Expectation Maximization)

- **E-step**
- **M-step**

---

# AIC vs BIC

---

# Probability Density



---

# SHAP

Unlike simpler methods that look at a feature in isolation, SHAP calculates the Shapley Value by evaluating a feature across all possible coalitions (subsets) of features.

It measures how much the prediction changes when Feature A is added to a group versus when it is absent.

By averaging these marginal contributions over every possible combination, we account for feature interactions and dependencies that global importance metrics (like Gini importance in Random Forests) often miss.

---
# Superhuman

## 🧠 1. Core ML Models & Foundations

- What is Logistic Regression?
   Logistic regression is a linear model used for binary classification that models the log-odds of the outcome as a linear function of the input features. The linear combination is passed through a sigmoid function to produce a probability between 0 and 1. A threshold (commonly 0.5) is then applied to convert the probability into a class label.

   why using log odds?
   ln(p/1-p) = beta0 + beta1*x1 + beta2*x2
   Logistic regression models the log-odds because probabilities are bounded between 0 and 1, while a linear model outputs unbounded values. By modeling log-odds, we map an unbounded linear combination to a valid probability via the sigmoid function, while also preserving a linear relationship in the transformed space.

- What’s the loss function?
   Logistic regression uses log loss (cross-entropy), and is trained by minimizing it using gradient descent or variants like SGD.

- How to train it?
- How do you choose the hyper parameter?
   Key hyperparameters are regularization strength (λ or C) and type (L1/L2). These are typically selected via cross-validation.

- How would you explain the difference between linear and logistic regression to a novice?
- What are the dissimilarities between SVM and Random Forest?
- Can you explain the underlying assumptions of linear regression, and the importance of taking them into account when interpreting model outcomes?
- How do bias and variance factor into decision trees? Plus, which one is more problematic - high bias or high variance - and how do you justify that?

## 📊 2. Model Evaluation & Diagnostics

- How do you calculate both precision and recall in a data-driven analysis?
- Could you elucidate the concept of an ROC curve and the significance of AUC?
   ROC curve plots True Positive Rate vs False Positive Rate across different thresholds, showing the trade-off between sensitivity and specificity.
   AUC (Area Under Curve):
	•	Measures overall ranking ability
	•	Interpretation: Probability that a random positive is ranked higher than a random negative: AUC = 1.0 → perfect ranking, AUC = 0.5 → random guessing, AUC < 0.5 → worse than random
	•	Pros: threshold independent, can be used to compare models

- Walk me through the process of differentiating between high variance and high bias in a machine learning model.
   High bias is indicated when both training and test performance are poor, suggesting the model is too simple and underfitting. High variance occurs when training performance is strong but test performance is poor, indicating overfitting and poor generalization.

- Could you give me some examples of when overfitting and underfitting might occur in real-world scenarios? How do these impact the accuracy and performance of the model?

## ⚙️ 3. Training, Optimization & Regularization

- How to prevent overfitting?
   Common ways to prevent overfitting include regularization (L1/L2) to control model complexity
   reducing feature space via feature selection or dimensionality reduction like PCA
   using proper validation techniques such as cross-validation to ensure generalization
   Additionally, techniques like early stopping or collecting more data can also help.

- Some people prefer to use grid search CV for hyperparameter tuning, while others prefer random search CV. What are the advantages and disadvantages of each method?
   Grid Search
	•	Idea: Try all combinations of predefined hyperparameter values
	•	Example: learning_rate = [0.01, 0.1], depth = [3, 5] → tries all 4 combos
   pros:
   • Exhaustive → guaranteed to test every option
	• Good for small search spaces
   cons:
   • Expensive (combinatorial explosion)
	• Wastes time on unimportant parameters

   Random Search
	•	Idea: Sample random combinations from the parameter space

   pros:
   • More efficient for large/high-dimensional spaces
	•	Finds good results faster
   cons:
   • Not exhaustive
	•	Might miss exact optimal combo



- What steps do you take to deal with gradient problems in deep learning, and how do you evaluate their effectiveness?
   Gradient problems like vanishing and exploding gradients can be addressed using techniques such as proper weight initialization (e.g., Xavier or He), using activation functions like ReLU, applying gradient clipping to control large updates, and using architectures like LSTM or residual connections to improve gradient flow. Batch normalization can also help stabilize training. To evaluate effectiveness, I would monitor training stability, loss convergence, and gradient norms over time, ensuring gradients are neither vanishing nor exploding and that the model trains efficiently.

- What are the roles of batch normalization and dropout in training deep neural networks?
   Batch normalization stabilizes and accelerates training by normalizing activations within a mini-batch, which helps reduce internal covariate shift and allows for higher learning rates. Dropout, on the other hand, is a regularization technique that randomly deactivates neurons during training to prevent overfitting by reducing reliance on specific features. Together, batch normalization improves training efficiency, while dropout improves generalization.

- Explain L1/L2
   L1 regularization adds a penalty proportional to the absolute value of weights, which encourages some coefficients to shrink exactly to zero. This effectively performs feature selection by removing less important features.
   Why L2 does not drive parameters to zero?
   L2 uses a squared penalty, which shrinks weights smoothly toward zero but doesn’t create sharp corners like L1. Because of this, the optimization rarely drives weights exactly to zero—just very close.

## 🧹 4. Data, Features & Preprocessing

- What constitutes the practice of outlier detection in the field of analytics?
   Outliers can be handled by detecting them using statistical methods like z-scores or IQR and either removing them or transforming features, depending on whether they represent noise or real signals.
- What techniques are available for correcting covariate imbalance in machine learning, and in what ways do they bolster the models?
   Covariate imbalance refers to differences in feature distributions across groups, which can bias models; it can be addressed through reweighting, matching, or stratified sampling.
- In your opinion, what makes feature selection so significant in the context of machine learning?
   Feature selection is important because it reduces overfitting, improves interpretability, and speeds up training; common methods include regularization (L1), tree-based importance, or statistical tests.
- How would you explain the curse of dimensionality and propose a strategy to overcome it?
   The curse of dimensionality refers to the phenomenon where, as the number of features increases, data becomes sparse and distance metrics become less meaningful, which degrades model performance and increases overfitting risk. To address this, I would use dimensionality reduction techniques like PCA or feature selection to reduce irrelevant or redundant features, improving both model generalization and efficiency.

## 🧭 5. ML Paradigms & Concepts

- Can you articulate the distinctions between supervised, unsupervised, and reinforcement learning paradigms?
- In your opinion, what is the most crucial aspect of detecting an anomaly in a system or data set?

## 🤖 6. Algorithms & Methods

- Can you please elaborate on how K-means and the Expectation-Maximization (EM) algorithm differ?
   🔵 K-means
      •	Type: Hard clustering
      •	Assumption: Clusters are spherical, equal variance
      •	Assignment: Each point belongs to one cluster only
      •	Objective: Minimize within-cluster squared distance

   Steps:
      1.	Assign points to nearest centroid
      2.	Update centroids (mean of assigned points)

   ⸻

   🟣 EM (Gaussian Mixture Models)
      •	Type: Soft clustering (probabilistic)
      •	Assumption: Data comes from a mixture of Gaussians
      •	Assignment: Each point has probability for each cluster
      •	Objective: Maximize likelihood of data

   Steps:
      1.	E-step: Compute probabilities (responsibilities)
      2.	M-step: Update parameters (mean, covariance, weights)

   K-means performs hard clustering where each data point is assigned to a single cluster based on distance to centroids. EM, typically used with Gaussian Mixture Models, performs soft clustering by assigning probabilities of belonging to each cluster. Additionally, K-means is distance-based, while EM is a probabilistic generative model that maximizes likelihood.

- Could you give an overview of how collaborative filtering is used in ML applications?
   Collaborative filtering is used in recommendation systems to predict a user’s preferences based on the behavior of similar users or items. It assumes that users who behaved similarly in the past will have similar preferences in the future. There are two main approaches: user-based filtering, which finds similar users, and item-based filtering, which finds similar items. More advanced methods use matrix factorization to learn latent features representing users and items.
- Please tell me about the role of CNNs and where they are typically applied.
   Convolutional Neural Networks (CNNs) are designed to process grid-like data by using convolutional filters to automatically learn spatial hierarchies of features, such as edges, textures, and shapes. They are efficient because they use parameter sharing and local connectivity, which reduces the number of parameters compared to fully connected networks. CNNs are primarily applied in computer vision tasks like image classification, object detection, and segmentation, but are also used in areas like video analysis and even NLP for capturing local patterns in text.

## ⏳ 7. Time Series

- Could you discuss some common methods used in Time Series Forecasting?
- In time series analysis, what other models could be used in place of ARIMA?

## 🧠 8. Deep Learning (Attention)

- Can you break down the notion of an attention model?
- Could you expand on the concept of attention mechanisms in neural networks?

## 📝 9. NLP

- What is word embedding?
- Tell me some broadly used word embedding algorithm
- Can you introduce them a bit?
- How to train a word2vec model?

## 💻 10. Coding / Practical

- Is there a technique you use to extract all English words from a string of characters? If so, please share
- How would you go about programming a function that models a normal distribution and plots it?