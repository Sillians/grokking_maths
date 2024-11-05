# The `n x n` Identity Matrix

The identity matrix is a fundamental concept in linear algebra, playing a crucial role in matrix operations.

- It is "square" (has the same number of rows and columns),
- It has $1$'s on the diagonal and $0$s everywhere else,
- Its symbol is the capital letter $I$.

### 1. Definition of the Identity Matrix:
An **identity matrix** is a square matrix in which all the diagonal elements are $1$ and all other elements are $0$. 
It is denoted by $`I_n`$ for an $`n \times n`$ matrix.

- For a $`2 \times 2`$ identity matrix:

$`I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}`$


- For a $`3 \times 3`$ identity matrix:

$`I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}`$


### 2. Properties of the Identity Matrix:
- **Multiplicative Identity**: The identity matrix acts as the multiplicative identity for matrices, similar to the number $1$ for real numbers. For any $`n \times n`$ matrix $A$:

$`A \cdot I_n = I_n \cdot A = A`$

This property holds for both left and right multiplication.

- **Diagonal Structure**: The identity matrix is a **diagonal matrix** with all diagonal elements equal to 1.

- **Inverse Relationship**: The identity matrix is the result of multiplying a matrix by its inverse. For any invertible $`n \times n`$ matrix $A$:
$`A \cdot A^{-1} = A^{-1} \cdot A = I_n`$

- **Power of Identity Matrix**: For any integer $k$, $`I_n^k = I_n`$.


### 3. Significance in Linear Algebra:
- **Preservation of Vector Spaces**: When the identity matrix multiplies a vector, the vector remains unchanged. For a vector $`\mathbf{x}`$ in $`\mathbb{R}^n`$:
$`I_n \cdot \mathbf{x} = \mathbf{x}`$

- **Basis Representation**: The identity matrix serves as a representation of the standard basis in $`\mathbb{R}^n`$. Each column of the identity matrix is one of the standard basis vectors.


### 4. Applications of the Identity Matrix:
- **Solving Systems of Linear Equations**: The identity matrix is used in Gaussian elimination and other algorithms to simplify matrices to their reduced row echelon form.

- **Matrix Inverses**: The identity matrix helps verify whether a matrix has an inverse. If a matrix $A$ has an inverse $`A^{-1}`$, then:
$`A \cdot A^{-1} = A^{-1} \cdot A = I_n`$

- **Eigenvalues and Eigenvectors**: The identity matrix appears in the equation $`(A - \lambda I_n)\vec{x} = 0`$ for finding the eigenvalues $`\lambda`$ and eigenvectors $`\mathbf{x}`$ of a matrix $A$.


### 5. Examples and Calculations:
- **Multiplication Example**:

For a matrix $`A = \begin{bmatrix} 4 & 2 \\ 1 & 3 \end{bmatrix}`$ and the identity matrix $`I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}`$:
$`A \cdot I_2 = \begin{bmatrix} 4 & 2 \\ 1 & 3 \end{bmatrix} \cdot \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 4 & 2 \\ 1 & 3 \end{bmatrix}`$


- **Verification of Inverses**:

Given $`A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}`$ and its inverse $`A^{-1} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}`$:
$`A \cdot A^{-1} = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} \cdot \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I_2`$



### 6. Identity Matrix in Higher Dimensions:
For larger dimensions, the identity matrix maintains the same structure, with $1$s on the main diagonal and $0$s elsewhere. 
For example, a $`4 \times 4`$ identity matrix is:

$`I_4 = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}`$



### 7. The Role of the Identity Matrix in Matrix Transformations:
- **Preserving Transformations**: When performing linear transformations, multiplying by the identity matrix corresponds to no change in the vector space. 
This means it preserves the direction and magnitude of vectors.

- **Normalization**: The identity matrix is used in normalization processes where matrix properties need to be preserved or analyzed.

In summary, the identity matrix is a fundamental tool in linear algebra that serves as a building block for matrix operations, preserving matrix properties and assisting in transformations and computations.



## Reference:
- The `n × n` Identity Matrix: [The nxn Identity Matrix](https://maths.nuigalway.ie/~rquinlan/MA203/section2-2.pdf)

- Identity Matrices: [Identity Matrices](http://apps.lonestar.edu/blogs/pehorton/files/2024/05/Math-1324-Lecture-8.pdf)