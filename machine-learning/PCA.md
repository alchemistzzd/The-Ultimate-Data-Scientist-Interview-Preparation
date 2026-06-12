# Principle Component Analysis

## Reason
PCA is a dimension reduction technique to solve the problems of Curse of Dimensionality

## Steps
1. Calculate covariance matrix (Pearson correlation)
2. Decompose the covariance matrix and find eigenvalues and corresponding eigenvectors by

    $$covariance matrix * eigenvector = eigenvalue * eigenvector$$

3. Each eigenvalue corresponds to a principle component, rank them from highest to lowest

## Assumptions
1. variables should all have linear relationship, since Pearson correlation captures linear correlation relationship
2. data samples are well representitive for PCA to work effectively

## Limitations
(Think from the conditions PCA have, like linear, orthogonal, then it is not good at not those)
1. not good at variables with non linear relationships
2. if the data we have is better presented with non-orthogonal principle components
3. PCA removes low variances components and treat all of them as noise but sometimes they are useful

## Implementation caveats
1. Standardization
Necessary if variables are not on the same scale. Since covariance matrix is sensitive to scale. (if one variable is 10x scale, the correlation value will be 10x too)

2. Evaluation
