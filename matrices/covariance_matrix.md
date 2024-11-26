# Covariance Matrix

A **covariance matrix** is a square matrix that captures the covariance (a measure of the linear relationship) 
between multiple variables in a dataset. It plays a critical role in statistics, machine learning, and data analysis, 
particularly in `multivariate analysis`, `principal component analysis (PCA)`, and `Gaussian distributions`.


### Covariance Definition
The covariance between two variables $X$ and $Y$ is defined as:

$`\text{Cov}(X, Y) = \frac{1}{n} \sum_{i=1}^{n} (X_i - \mu_X)(Y_i - \mu_Y)`$

where:
- $X_i, Y_i$: Data points for variables $X$ and $Y$.
- $`\mu_X, \mu_Y`$: Means of $X$ and $Y$.
- $n$: Number of data points.

### Covariance Matrix Structure
For a dataset with $d$ variables, the covariance matrix is a $`d \times d`$ symmetric matrix:

$`\mathbf{\Sigma} = \begin{bmatrix} \text{Var}(X_1) & \text{Cov}(X_1, X_2) & \dots & \text{Cov}(X_1, X_d) \\ \text{Cov}(X_2, X_1) & \text{Var}(X_2) & \dots & \text{Cov}(X_2, X_d) \\ \vdots & \vdots & \ddots & \vdots \\ \text{Cov}(X_d, X_1) & \text{Cov}(X_d, X_2) & \dots & \text{Var}(X_d) \end{bmatrix}`$

- The diagonal elements represent the variance of each variable $`(\text{Var}(X_i))`$.
- The off-diagonal elements represent the covariance between pairs of variables $`(\text{Cov}(X_i, X_j))`$.


### Properties
1. **Symmetric**: $`\text{Cov}(X_i, X_j) = \text{Cov}(X_j, X_i)`$.
2. **Positive Semi-Definite**: For any vector $`\mathbf{v}`$, $`\mathbf{v}^T \mathbf{\Sigma} \mathbf{v} \geq 0`$.
3. **Dimension**: The covariance matrix has dimensions $d \times d$, where $d$ is the number of variables.

---

### Computing the Covariance Matrix
For a dataset $\mathbf{X}$ with $n$ samples and $d$ features $`(n \times d \ matrix)`$:
1. Center the data:
   
   $`\mathbf{X}_{\text{centered}} = \mathbf{X} - \mu`$

   where $\mu$ is the mean of each column (feature).

2. Compute:
   $`\mathbf{\Sigma} = \frac{1}{n-1} \mathbf{X}_{\text{centered}}^T \mathbf{X}_{\text{centered}}`$

### Applications
1. **Principal Component Analysis (PCA)**: 
   Eigenvalues and eigenvectors of the covariance matrix are used to identify the principal components.

2. **Multivariate Gaussian Distribution**: 
   The covariance matrix is used to describe the spread and correlation of the data in multivariate Gaussian models.

3. **Portfolio Optimization**:
   Covariance matrices help in modeling and minimizing risk by understanding correlations between financial assets.

---

### Example
Given the dataset:
$`\mathbf{X} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6  \end{bmatrix}`$

1. Compute column means:
   
   $`\mu = [3, 4]`$

2. Center the data:
   
   $`\mathbf{X}_{\text{centered}} = \begin{bmatrix} -2 & -2 \\ 0 & 0 \\ 2 & 2  \end{bmatrix}`$

3. Covariance matrix:
   
   $`\mathbf{\Sigma} = \frac{1}{n-1} \mathbf{X}_{\text{centered}}^T \mathbf{X}_{\text{centered}} = \begin{bmatrix} 4 & 4 \\ 4 & 4  \end{bmatrix}`$

This result indicates strong positive linear relationships between the features.



### Reference

- Variance / Covariance Matrices [Variance/Covariance Matrices](https://www.biostat.jhsph.edu/~fdominic/teaching/bio655/extras/matrixnotes2.pdf)
- Random Vectors and the Variance–Covariance Matrix [Random Vectors and the Variance–Covariance Matrix](https://www.math.kent.edu/~reichel/courses/monte.carlo/alt4.7d.pdf)
- Linear Algebra (Refer to 2.3.1 Covariance matrices) [Linear Algebra](https://www.fil.ion.ucl.ac.uk/~wpenny/course/matrices.pdf)
- Covariance Matrices and Joint Probabilities [Covariance Matrices and Joint Probabilities](https://math.mit.edu/~gs/linearalgebra/ila5/linearalgebra5_12-2.pdf)