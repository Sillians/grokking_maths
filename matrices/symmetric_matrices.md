# Symmetric Matrices

## Diagonalization of Symmetric Matrices

A symmetric matrix is a matrix $A$ such that $`A^T = A`$. Such a matrix is necessarily square. Its main diagonal entries are arbitrary, but its other entries
occur in pairs, on opposite sides of the main diagonal.

Note: Symmetric matrices are necessarily square.

### Example 1:

$`\begin{pmatrix} 1 & -2 \\ -2 & 3  \end{pmatrix}`$

is symmetric but

$`\begin{pmatrix} 1 & -2 \\ 5 & 3  \end{pmatrix}`$

is not. The transpose is

$`\begin{pmatrix} 1 & 5 \\ -2 & 3  \end{pmatrix}`$


### Theorem 1: 
If $A$ is symmetric, then any two eigenvectors from different eigenspaces are orthogonal. If $A$ is a **symmetric matrix**, 
then **any two eigenvectors corresponding to distinct eigenvalues are orthogonal**.

In other words, if $v_1$ and $v_2$ are eigenvectors associated with eigenvalues $\lambda_1$ and $\lambda_2$ 
of a symmetric matrix $A$, and $`\lambda_1 \neq \lambda_2`$, then $`v_1 \cdot v_2 = 0`$ (i.e., $v_1$ and $v_2$ are orthogonal).

#### Proof
1. **Assume**:
   - Let $v_1$ and $v_2$ be eigenvectors of $A$ corresponding to distinct eigenvalues, say $\lambda_1$ and $\lambda_2$.
   
2. **Goal**:
   - Show that $`v_1 \cdot v_2 = 0`$ (i.e., $v_1$ and $v_2$ are orthogonal).

3. **Computation**:
   - Start with the product $`\lambda_1 v_1 \cdot v_2`$:
   
     $`\lambda_1 v_1 \cdot v_2 = (\lambda_1 v_1)^T v_2`$
   
   - Since $v_1$ is an eigenvector of $A$, we can substitute $`\lambda_1 v_1 = A v_1`$: $`= (A v_1)^T v_2`$
   
   - Use the transpose property $`(A v_1)^T = v_1^T A^T`$ (since $A$ is symmetric,  $`A = A^T`$): $`= v_1^T A v_2`$
     
   - Substitute $`A v_2 = \lambda_2 v_2`$ (since $v_2$ is an eigenvector with eigenvalue $\lambda_2$): $`= v_1^T (\lambda_2 v_2)`$
     
   - Rewrite this as: $` = \lambda_2 v_1 \cdot v_2`$

4. **Conclusion**:
   - We now have $`\lambda_1 v_1 \cdot v_2 = \lambda_2 v_1 \cdot v_2`$.
   - This implies $`(\lambda_1 - \lambda_2) v_1 \cdot v_2 = 0`$.
   - Since $`\lambda_1 - \lambda_2 \neq 0`$, it follows that $`v_1 \cdot v_2 = 0`$, proving that $v_1$ and $v_2$ are orthogonal.


#### Orthogonal Diagonalizability of a Matrix $A$

An $`n \times n`$ matrix $A$ is said to be **orthogonally diagonalizable** if there exists an **orthogonal matrix** $P$ (with $`P^{-1} = P^T`$) 
and a **diagonal matrix** $D$ such that:

$`A = P D P^T = P D P^{-1}`$

For this decomposition to exist, $A$ must have $n$ linearly independent, **orthonormal eigenvectors**.


#### When is Orthogonal Diagonalization Possible?

1. **If $A$ is orthogonally diagonalizable**, then:

   $`A^T = (P D P^T)^T = P^{TT} D^T P^T = P D P^T = A`$

   This calculation shows that $`A = A^T`$, so **$A$ must be symmetric**.

2. **Conversely, if $A$ is symmetric**, then it is guaranteed to have a complete set of orthonormal eigenvectors and can be orthogonally diagonalized. 
This is a fundamental result in linear algebra and ensures that all symmetric matrices are orthogonally diagonalizable. 



### Theorem 2:
An $`n \times n`$ matrix $A$ is orthogonally diagonalizable if and only if $A$ is a symmetric matrix. The set of eigenvalues of a matrix $A$ is sometimes
called the spectrum of $A$.


### Theorem 3: (The Spectral Theorem for Symmetric Matrices).
An $`n \times n`$ symmetric matrix A has the following properties:

1. $A$ has $n$ real eigenvalues, counting multiplicities.
2. The dimension of the eigenspace for each eigenvalue $\lambda$ equals the multiplicity of $\lambda$ as a root of the characteristic equation.
3.  The eigenspaces are mutually orthogonal, in the sense that eigenvectors corresponding to different eigenvalues are orthogonal.
4. $A$ is orthogonally diagonalizable.


## Spectral Decomposition

### Definition
Given an $`n \times n`$ matrix $A$, if $`A = P D P^{-1}`$ where $P$ is an orthogonal matrix (i.e., $`P^{-1} = P^T`$), then we have:
$`A = P D P^T`$

where:
- $`P = [u_1, u_2, \dots, u_n]`$ is a matrix with orthonormal eigenvectors $u_i$ as columns.
- $`D = \text{diag}(\lambda_1, \dots, \lambda_n)`$ is a diagonal matrix containing the eigenvalues of $A$.

### Spectral Decomposition Representation

Using the column-row expansion, we can rewrite $A$ as:
$`A = \lambda_1 u_1 u_1^T + \lambda_2 u_2 u_2^T + \cdots + \lambda_n u_n u_n^T`$

Each term $`\lambda_i u_i u_i^T`$ is an $`n \times n`$ matrix of rank 1. This representation is known as the **spectral decomposition** of $A$
because it expresses $A$ in terms of its eigenvalues (the "spectrum") and eigenvectors.

#### Properties
Each matrix $`u_j u_j^T`$ is a **projection matrix** that projects vectors onto the subspace spanned by $u_j$.

---

### Example 2: Spectral Decomposition Using a Rank-1 Matrix

Let $u$ be a unit vector in $`\mathbb{R}^n`$, and let $`B = uu^T`$.

#### (a) Given any $`x \in \mathbb{R}^n`$, compute $Bx$ and show that $Bx$ is the orthogonal projection of $x$ onto $u$.
To see this, we compute:

$`B x = (u u^T) x = u (u^T x)`$

The term $`u^T x`$ is a scalar representing the component of $x$ in the direction of $u$. Thus, $`B x`$ is a scalar multiple of $u$, 
which makes it the orthogonal projection of $x$ onto $u$.

#### (b) Show that $B$ is symmetric and that $`B^2 = B`$.
Since $`B = u u^T`$:
1. **Symmetric**: $`B^T = (u u^T)^T = u u^T = B`$.
2. **Idempotent**: $`B^2 = (u u^T)(u u^T) = u (u^T u) u^T = u \cdot 1 \cdot u^T = u u^T = B`$. Therefore, $B$ is idempotent, meaning $`B^2 = B`$.

#### (c) Show that \( u \) is an eigenvector of \( B \) and determine the corresponding eigenvalue.
Since $`B = u u^T`$:
$`B u = (u u^T) u = u (u^T u) = u \cdot 1 = u`$

This shows that $u$ is an eigenvector of $B$ with eigenvalue $`\lambda = 1`$.

---

### Example 3: Finding the Inverse of each Orthogonal Matrices

An orthogonal matrix $Q$ satisfies $`Q^T = Q^{-1}`$, so the inverse of an orthogonal matrix is simply its transpose.

#### (a)
For matrix
$`Q = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}`$

its transpose is:
$`Q^T = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}`$

Thus, $`Q^{-1} = Q^T = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}`$.

#### (b)
For the matrix
$`Q = \begin{bmatrix} 0.5 & 0.5 & -0.5 & -0.5 \\ 0.5 & 0.5 & 0.5 & 0.5 \\ 0.5 & -0.5 & -0.5 & 0.5 \\ 0.5 & -0.5 & 0.5 & -0.5 \end{bmatrix}`$

its inverse is its transpose:
$`Q^{-1} = Q^T = \begin{bmatrix} 0.5 & 0.5 & 0.5 & 0.5 \\ 0.5 & 0.5 & -0.5 & -0.5 \\ -0.5 & 0.5 & -0.5 & 0.5 \\ -0.5 & 0.5 & 0.5 & -0.5 \end{bmatrix}`$

---

### Example 4: Orthogonal Diagonalization of a Symmetric Matrix

Given:
$`A = \begin{bmatrix} 1 & -6 & 4 \\ -6 & 2 & -2 \\ 4 & -2 & -3 \end{bmatrix}`$

with eigenvalues $`-3, -6, and  9`$.

#### Steps for Orthogonal Diagonalization
1. **Find Eigenvectors**: Compute eigenvectors for each eigenvalue.
2. **Construct Matrix $P$**: Form $P$ using the normalized eigenvectors as columns.
3. **Construct Diagonal Matrix $D$**: Place each eigenvalue in $D$ along the diagonal.

For a detailed orthogonal diagonalization, you would find:
1. The eigenvectors for each eigenvalue of $A$.
2. Normalize these eigenvectors to ensure orthonormality.
3. Construct $P$ and $D$ from these eigenvectors and eigenvalues, respectively, yielding $`A = P D P^T`$.

---


Let's walk through this diagonalization of the symmetric matrix $`A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}`$, 
finding its eigenvalues, eigenvectors, and verifying that the diagonalization $`A = P D P^T`$ holds.

### Step 1: Find the Eigenvalues
We look for the eigenvalues. If $`A \vec{v} = \lambda \vec{v}`$

then $\vec{v}$ is an eigenvector and $\lambda$ is an eigenvalue. We rewrite this equation as 

$`A \vec{v} = \lambda I_2 \vec{v}`$ so that $`(A = \lambda I_2) \vec{v} = 0`$

For a matrix $A$, eigenvalues $\lambda$ satisfy the characteristic equation:
$`\det(A - \lambda I_2) = 0`$ so that 

Substitute $A$ and $\lambda I_2$, thus the null space of:

$`A - \lambda I_2 = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix} - \begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix} = \begin{bmatrix} 3 - \lambda & 1 \\ 1 & 3 - \lambda \end{bmatrix}`$

Then, calculate the determinant:

$`\left| \begin{matrix} 3 - \lambda & 1 \\ 1 & 3 - \lambda \end{matrix} \right| = 0`$

$`\det(A - \lambda I_2) = (3 - \lambda)(3 - \lambda) - (1)(1) = \lambda^2 - 6\lambda + 8 = (\lambda - 2)(\lambda - 4)`$

Thus, the eigenvalues are $`\lambda = 2`$ and $`\lambda = 4`$.


### Step 2: Find the Eigenvectors

#### Eigenvector for $`\lambda = 2`$
To find the eigenvectors corresponding to $`\lambda = 2`$, solve:

$`(A - 2I_2)v = 0 \quad \Rightarrow \quad \begin{bmatrix} 3 - 2 & 1 \\ 1 & 3 - 2 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}`$

Using Gaussian elimination:
$`\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}`$

This gives $`x + y = 0`$, so $`x = -y`$. One solution is $`v_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}`$.


#### Eigenvector for $`\lambda = 4`$
Similarly, for $`\lambda = 4`$ , solve:

$`(A - 4I_2)v = 0 \quad \Rightarrow \quad \begin{bmatrix} 3 - 4 & 1 \\ 1 & 3 - 4 \end{bmatrix} = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}`$

Using Gaussian elimination:
$`\begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & -1 \\ 0 & 0 \end{bmatrix}`$

This gives $`x - y = 0`$, so $`x = y`$. One solution is $`v_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}`$.


### Step 3: Normalize the Eigenvectors
We normalize $v_1$ and $v_2$ to obtain an orthonormal basis:

$`u_1 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ -1 \end{bmatrix}, \quad u_2 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix}`$

### Step 4: Construct $P$ and $D$
Form matrix $P$ with columns $u_1$ and $u_2$, and matrix $D$ with eigenvalues along the diagonal:

$`P = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}, \quad D = \begin{bmatrix} 2 & 0 \\ 0 & 4 \end{bmatrix}`$


Sure, let’s go through how to find the transpose of \( P \) and complete the verification step in more detail.


### Step 5: Verify $`A = P D P^T`$
To compute $`P D P^T`$, let’s find $P^T$ (the transpose of $P$) and then carry out the multiplication.

1. **Transpose of $P$:**

   The transpose of a matrix is found by swapping its rows and columns. Given:
   $`P = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}`$

   The transpose $`P^T`$ is:
   $`P^T = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}`$

2. **Compute $`P D`$:**

   Now, multiply $P$ and $D$:
   $`P D = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 2 & 0 \\ 0 & 4 \end{bmatrix}`$

   Performing the multiplication:
   $`P D = \frac{1}{\sqrt{2}} \begin{bmatrix} (1)(2) + (1)(0) & (1)(0) + (1)(4) \\ (-1)(2) + (1)(0) & (-1)(0) + (1)(4) \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 2 & 4 \\ -2 & 4 \end{bmatrix}`$


3. **Compute $`P D P^T`$:**

   Next, multiply $P D$ by $`P^T`$:
   $`P D P^T = \frac{1}{\sqrt{2}} \begin{bmatrix} 2 & 4 \\ -2 & 4 \end{bmatrix} \cdot \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}`$

   Simplifying the scalar multiplication:
   $`P D P^T = \frac{1}{2} \begin{bmatrix} 2 & 4 \\ -2 & 4 \end{bmatrix} \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}`$

   Now, carry out the matrix multiplication:
   $`P D P^T = \frac{1}{2} \begin{bmatrix} (2)(1) + (4)(1) & (2)(-1) + (4)(1) \\ (-2)(1) + (4)(1) & (-2)(-1) + (4)(1) \end{bmatrix} = \frac{1}{2} \begin{bmatrix} 6 & 2 \\ 2 & 6 \end{bmatrix}`$

   Simplifying further:
   $`P D P^T = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}`$

Thus, we confirm that:

$`A = P D P^T = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}`$

Thus, $`A = P D P^T`$, confirming the diagonalization, which matches our original matrix $A$.















### Summary
- Symmetric matrices have orthogonal eigenvectors corresponding to distinct eigenvalues.
- Symmetric matrices can always be orthogonally diagonalized.





