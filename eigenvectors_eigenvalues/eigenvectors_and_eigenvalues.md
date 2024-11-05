# Eigenvectors and Eigenvalues

**Definition:** In linear algebra, **eigenvalues** and **eigenvectors** are fundamental concepts that help us understand how linear transformations behave. 
When we apply a transformation $A$ (a square matrix) to a vector $`\vec{x}`$, if the result is a scalar multiple of $`\vec{x}`$, 
then $`\vec{x}`$ is called an **eigenvector** of $A$, and the scalar $`\lambda`$ is the corresponding **eigenvalue**.


### 1. **Eigenvector and Eigenvalue Relationship**:
If $`\vec{x}`$ is an eigenvector of matrix $A$ with eigenvalue $`\lambda`$, then:

$`A\vec{x} = \lambda \vec{x}`$

This means that when matrix $A$ is applied to the vector $`\vec{x}`$, the output $`A\vec{x}`$ is a scalar multiple $`( \lambda )`$ of the original vector $`\vec{x}`$. 
This property shows that $`\vec{x}`$ does not change direction under the transformation represented by $A$, only its magnitude is scaled by $`\lambda`$.

### 2. **Implications for Powers and Shifts of Matrices**:
- If $`A\vec{x} = \lambda \vec{x}`$, then applying $A$ multiple times yields:

$`A^2 x = A(Ax) = A(\lambda x) = \lambda (Ax) = \lambda^2 x`$

So, raising $A$ to the power $n$ gives:
$`A^n x = \lambda^n x`$

- For the inverse matrix, if $`\lambda \neq 0`$:
$`A^{-1} x = \lambda^{-1} x`$

- Adding a scalar multiple of the identity matrix $`cI`$ to $A$ results in:
$`(A + cI)x = Ax + cIx = \lambda x + cx = (\lambda + c)x`$

This operation shifts the eigenvalues by $c$ but keeps the eigenvectors unchanged.

### 3. **Singularity and Determinant Condition**:
If $`A\vec{x} = \lambda \vec{x}`$, then rearranging gives:

$`(A - \lambda I)x = 0`$

This implies that $`A - \lambda I`$ must be singular (non-invertible) for non-zero $`\vec{x}`$. Therefore:

$`\det(A - \lambda I) = 0`$

This determinant equation is called the **characteristic polynomial**, and solving it gives the eigenvalues $`\lambda`$.

### 4. **Properties and Checks for Eigenvalues**:
- The **product of the eigenvalues** of a matrix $A$ equals the **determinant** of $A$:

$`\det(A) = \lambda_1 \lambda_2 \dots \lambda_n`$

- The **sum of the eigenvalues** equals the **trace** of the matrix (the sum of its diagonal elements):

$`\text{trace}(A) = a_{11} + a_{22} + \dots + a_{nn} = \lambda_1 + \lambda_2 + \dots + \lambda_n`$

### 5. **Special Cases of Eigenvalues**:
- **Projections**: Matrices that represent projection transformations have eigenvalues $`\lambda = 1`$ and $`\lambda = 0`$. 
The eigenvalue `1` corresponds to vectors that lie on the line of projection (unchanged), and `0` corresponds to vectors that are orthogonal to it (projected to zero).

- **Reflections**: Matrices representing reflections typically have eigenvalues $`\lambda = 1`$ (vectors along the line of reflection) and $`\lambda = -1`$ (vectors orthogonal to the line of reflection).

- **Rotations**: In the complex plane, rotation matrices have complex eigenvalues of the form $`e^{i\theta}`$ and $`e^{-i\theta}`$, 
representing a rotation by an angle $`\theta`$. For real matrices representing 2D rotation, there are generally no real eigenvalues 
unless the rotation angle is $`0^\circ`$ or $`180^\circ`$.

These properties and checks form the backbone of understanding eigenvalues and eigenvectors in linear transformations and their applications in various fields, 
including physics, computer graphics, and data science.


## Solving eigenvalue problem for an $n$ by $n$ matrix
To solve the eigenvalue problem for an $n$ by $n$ matrix, follow these steps:

### 1. Compute the Determinant of $A - \lambda I$:
Given a matrix $A$, subtract $\lambda$ from the diagonal elements to form the matrix  $`A - \lambda I`$. Then compute its determinant. 
This determinant will be a polynomial in $`\lambda`$, known as the **characteristic polynomial**.

- For a **2 × 2 matrix** $`A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}`$, the characteristic polynomial is:
$`\det(A - \lambda I) = \det \begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix} = (a - \lambda)(d - \lambda) - bc`$

This is a quadratic polynomial $`\lambda^2 - (a + d)\lambda + (ad - bc)`$.

- For a **3 × 3 matrix** $`A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix}`$, 
the determinant $`\det(A - \lambda I)`$ expands to a cubic polynomial in $`\lambda`$.


### 2. Find the Roots of the Characteristic Polynomial:
Solve the equation $`\det(A - \lambda I) = 0`$ for $`\lambda`$. The roots of this polynomial are the **eigenvalues** of $`A`$. 
These are the values of $`\lambda`$ that make $`A - \lambda I`$ a **singular** matrix (i.e., a matrix with zero determinant).


### 3. Solve $`(A - \lambda I)\vec{x} = 0`$ for Each Eigenvalue:
For each eigenvalue $`\lambda`$, substitute it into the equation $`(A - \lambda I)\vec{x} = 0`$ to find the corresponding **eigenvector** $\vec{x}$. 
This equation forms a system of linear equations.

- For a **2 × 2 matrix**, the rows of $`A - \lambda I`$ will be proportional (indicating the matrix is singular). 
The solution vector $`x`$ can be found by choosing any non-trivial vector $`(b, -a)`$, where $`(a, b)`$ are coefficients from one of the proportional rows.


### Example with a 2 × 2 Matrix:
Suppose $`A = \begin{bmatrix} 4 & 2 \\ 1 & 3 \end{bmatrix}`$.

1. **Find the Characteristic Polynomial**:
$`\det(A - \lambda I) = \det \begin{bmatrix} 4 - \lambda & 2 \\ 1 & 3 - \lambda \end{bmatrix} = (4 - \lambda)(3 - \lambda) - 2 \cdot 1 = \lambda^2 - 7\lambda + 10`$


2. **Find the Eigenvalues**:
Solve $`\lambda^2 - 7\lambda + 10 = 0`$:

$`(\lambda - 5)(\lambda - 2) = 0`$

Eigenvalues are $`\lambda_1 = 5`$ and $`\lambda_2 = 2`$.


3. **Find the Eigenvectors**:
- **For $`\lambda = 5`$**:
$`(A - 5I)x = \begin{bmatrix} -1 & 2 \\ 1 & -2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}`$

Solving this system, we get $`x_1 = 2x_2`$. An eigenvector is $`x = \begin{bmatrix} 2 \\ 1 \end{bmatrix}`$.

- **For $`\lambda = 2`$**:
$`(A - 2I)x = \begin{bmatrix} 2 & 2 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}`$

Solving this system, we get $`x_1 = -x_2`$. An eigenvector is $`x = \begin{bmatrix} -1 \\ 1 \end{bmatrix}`$.

- The eigenvalues of $A$ are $`\lambda_1 = 5`$ and $`\lambda_2 = 2`$.
- Eigenvectors can be any non-zero multiples of $`\begin{bmatrix} 2 \\ 1 \end{bmatrix}`$ for $`\lambda_1 = 5`$ and $`\begin{bmatrix} -1 \\ 1 \end{bmatrix}`$ 
for $`\lambda_2 = 2`$.

  

### REVIEW OF THE KEY IDEAS
1. $`A \vec{x} = \lambda \vec{x}`$ says that eigenvectors $`\vec{x}`$ keep the same direction when multiplied by $A$.
2. $`A \vec{x} = \lambda \vec{x}`$ also says that $`\det(A - \lambda I) = 0`$. This determines $n$ eigenvalues.
3. The eigenvalues of $`A^2`$ and $`A^{-1}`$ are $`\lambda^{2}`$ and $`\lambda^{-1}`$, with the same eigenvectors.
4. The sum of the $`\lambda`$'s equals the sum down the main diagonal of $A$ (the trace). The product of the $`\lambda`$'s equals the determinant of $A$.
5. Special properties of a matrix lead to special eigenvalues and eigenvectors.




## Applications of Eigenvalues and Eigenvectors in Machine Learning

Eigenvalues and eigenvectors have a wide array of applications across many machine learning, data science, and computational fields. 
Some primary contexts where they are especially useful include:

### 1. **Principal Component Analysis (PCA)**
   - **Context**: Dimensionality reduction and data compression.
   - **Application**: PCA finds the principal components of the data by identifying the directions (principal axes) that maximize the variance. These principal axes are the eigenvectors of the data’s covariance matrix, with eigenvalues indicating the amount of variance explained by each component. PCA is widely used for visualization, feature reduction, and noise reduction in high-dimensional datasets.

### 2. **Graph Theory and Network Analysis**
   - **Context**: Analyzing and simplifying graphs and social networks.
   - **Application**: Eigenvectors and eigenvalues of matrices like the **adjacency matrix** or **Laplacian matrix** (which represents relationships or edges in a network) can identify influential nodes, cluster nodes, and reveal graph connectivity. They are crucial in community detection, page ranking, and analyzing connectivity within large networks.

### 3. **Singular Value Decomposition (SVD)**
   - **Context**: Matrix factorization in collaborative filtering and text mining.
   - **Application**: In recommendation systems (e.g., collaborative filtering), SVD is used to decompose user-item interaction matrices, extracting latent features of users and items. The decomposition relies on eigenvectors of derived matrices. This allows recommendation systems to fill in missing ratings, even for large-scale sparse matrices.

### 4. **Quantum Computing and Quantum Mechanics**
   - **Context**: Quantum state analysis and measurement.
   - **Application**: Eigenvalues and eigenvectors describe the possible outcomes of a quantum measurement. In a quantum system, they define energy levels and are central to solving Schrödinger's equation. Quantum computing algorithms (like Shor's algorithm) also leverage eigenvalues in factoring and other computational problems.

### 5. **Image Compression and Face Recognition**
   - **Context**: Image processing.
   - **Application**: Eigenvalues and eigenvectors are key in techniques like **Eigenfaces** for face recognition. In Eigenfaces, PCA is applied to a set of face images, and the principal components (eigenfaces) are used to represent and compare faces, compressing image data while preserving essential characteristics for identification.

### 6. **Stability Analysis in Control Systems**
   - **Context**: Robotics, autonomous systems, and engineering.
   - **Application**: Eigenvalues of the system matrix in linear control systems indicate system stability. If all eigenvalues have negative real parts, the system is stable. Engineers use this information to design feedback mechanisms that maintain system stability in automated systems like drones, vehicles, and industrial machinery.

### 7. **Natural Language Processing (NLP) and Word Embeddings**
   - **Context**: Text data representation.
   - **Application**: Eigen decomposition techniques, like SVD, are used in methods such as **Latent Semantic Analysis (LSA)** for topic modeling. Eigenvectors reveal the underlying topics or themes within a document-term matrix, helping in tasks such as information retrieval and semantic similarity.

### 8. **Dynamics and Time-Series Forecasting**
   - **Context**: Financial and scientific modeling.
   - **Application**: Eigenvalues in **Autoregressive Moving Average (ARMA)** models or related state-space models determine the stability of time series and are used to forecast future states, e.g., stock prices, weather patterns, and economic indicators.

Eigenvalues and eigenvectors, in summary, enable meaningful decompositions, transformations, and insights across many machine learning and scientific computing applications. They reveal structures within data, improve computational efficiency, and are essential for many matrix-based algorithms foundational to machine learning and AI.




### Reference

- Eigenvalues and Eigenvectors (Chapter 6): [Eigenvalues and Eigenvectors](https://math.mit.edu/~gs/linearalgebra/ila5/linearalgebra5_6-1.pdf)
- Lecture Notes: Eigenvalues and Eigenvectors (Chinese University of Hong Kong): [Lecture Notes: Eigenvalues and Eigenvectors](https://www.math.purdue.edu/~liu1957/MA262_files/eigen.pdf)
- 18.03 LA.5: Eigenvalues and Eigenvectors: [Eigenvectors and Eigenvalues](https://math.mit.edu/~jorloff/suppnotes/suppnotes03/la5.pdf)
- Eigenvalues, Eigenvectors, and Applications: [Eigenvalues, Eigenvectors, and Applications](https://web.ma.utexas.edu/users/sl55444/Archive/Eigenvalues.pdf)
- Eigenvalues and Eigenvectors (Interactive Linear Algebra): [Eigenvalues and Eigenvectors](https://textbooks.math.gatech.edu/ila/eigenvectors.html)
- Eigenvector and Eigenvalue (MathsisFun): [Eigenvector and Eigenvalue](https://www.mathsisfun.com/algebra/eigenvalue.html)


### Videos

[![IMAGE ALT TEXT](http://img.youtube.com/vi/BWvx4wUSGdA/0.jpg)](http://www.youtube.com/watch?v=BWvx4wUSGdA "Eigenvalues and Eigenvectors")


[![IMAGE ALT TEXT](http://img.youtube.com/vi/qa9fI6qvUQY/0.jpg)](http://www.youtube.com/watch?v=qa9fI6qvUQY "3 x 3 eigenvalues and eigenvectors")


[![IMAGE ALT TEXT](http://img.youtube.com/vi/PFDu9oVAE-g/0.jpg)](http://www.youtube.com/watch?v=PFDu9oVAE-g "Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra")



































































