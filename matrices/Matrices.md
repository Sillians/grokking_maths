# Matrices

## Introduction

**Definition:** A $m × n$ matrix is a rectangular array of numbers having $m$ rows and $n$ columns.

$` A = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ a_{31} & a_{32} & \dots & a_{3n} \\ \vdots & \vdots & \vdots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix} `$

#### Explanation of the Matrix Notation

- $`a_{ij}`$ represents the element in the $`i`$-th row and $`j`$-th column. We sometimes denote $A$ by
- The matrix has:
  - $m$ **rows** (indicated by indices $`i = 1, 2, \dots, m`$).
  - $n$ **columns** (indicated by indices $`j = 1, 2, \dots, n`$).

This general form allows each element $`a_{ij}`$ to vary, making it applicable to any rectangular or square matrix with $m$ rows and $n$ columns.


## Matrix Operation

### 1. **Addition**

We can only add two matrices of the same dimension i.e. same number of `rows` and `columns`. We then add element-wise

`Example`:

Here's an example of **matrix addition** using two $`2 \times 2`$ matrices:

Let:

$`A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \quad \text{and} \quad B = \begin{pmatrix} 4 & 3 \\ 5 & 6 \end{pmatrix}`$

To find $`A + B`$:

1. **Add the corresponding elements** from matrices $A$ and $B$.
   - Top-left: $`2 + 4 = 6`$
   - Top-right: $`1 + 3 = 4`$
   - Bottom-left: $`1 + 5 = 6`$
   - Bottom-right: $`3 + 6 = 9`$

So,

$`A + B = \begin{pmatrix} 2 + 4 & 1 + 3 \\ 1 + 5 & 3 + 6 \end{pmatrix} = \begin{pmatrix} 6 & 4 \\ 6 & 9 \end{pmatrix}`$

Thus,

$`\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} + \begin{pmatrix} 4 & 3 \\ 5 & 6 \end{pmatrix} = \begin{pmatrix} 6 & 4 \\ 6 & 9 \end{pmatrix}`$



### 2. **Scalar Multiplication**

if $c$ is a real number and $`A = (a_{ij})_{m \times n}`$ is a matrix then $`cA = (ca_{ij})_{m \times n}`$.

`Example`:

This example demonstrates **scalar multiplication** of a matrix. When a real number $c$ multiplies each element of a matrix $A$, it is called **scalar multiplication**.

Let:
$`c = 5 \quad \text{and} \quad A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}`$

Then, $cA$ is calculated by multiplying each element of $A$ by $c$.

#### Steps
1. Multiply $`c = 5`$ with each element in $A$:
   - Top-left: $`5 \times 2 = 10`$
   - Top-right: $`5 \times 1 = 5`$
   - Bottom-left: $`5 \times 1 = 5`$
   - Bottom-right: $`5 \times 3 = 15`$

So:

$`cA = 5 \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 10 & 5 \\ 5 & 15 \end{pmatrix}`$

Thus,

$`5 \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 10 & 5 \\ 5 & 15 \end{pmatrix}`$


### 3. **Matrix Multiplication**

Given a matrix  $`A = (a_{ij})_{m \times n}`$  and a matrix $`B = (b_{ij})_{r \times s}`$, we can only multiply
them if $`n = r`$. In such a case the multiplication is defined to be the matrix $`C = (c_{ij})_{m \times s}`$ as follows:


$`c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}`$

We may view the $c_{ij}$th element as the dot product of the $`ith`$ row of the matrix $A$ and $`jth`$ column of the matrix $B$.

#### Explanation

- $`c_{ij}`$: The element in the $`i`$-th row and $`j`$-th column of matrix $C$.
- $`\sum_{k=1}^{n}`$: This is a summation over $k$, where $k$ goes from $1$ to $n$ (the common dimension of $A$ and $B$).
- $`a_{ik}`$: The element in the $`i`$-th row and $`k`$-th column of matrix $A$.
- $`b_{kj}`$: The element in the $`k`$-th row and $`j`$-th column of matrix $B$.

#### Matrix Multiplication Example

Suppose:

$`A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \quad \text{and} \quad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}`$

To find $C = AB$:

1. **Calculate** $c_{11}$:
   $`c_{11} = (1 \times 5) + (2 \times 7) = 5 + 14 = 19`$

2. **Calculate** $c_{12}$:
   $`c_{12} = (1 \times 6) + (2 \times 8) = 6 + 16 = 22`$

3. **Calculate** $c_{21}$:
   $`c_{21} = (3 \times 5) + (4 \times 7) = 15 + 28 = 43`$

4. **Calculate** $c_{22}$:
   $`c_{22} = (3 \times 6) + (4 \times 8) = 18 + 32 = 50`$

So:

$`C = AB = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}`$



## Special matrices

1. A matrix is called a **square matrix** if the number of `rows` is equal to the number of `columns`.



2. The transpose of a square matrix $`A = (a_{ij})`$ is the matrix $`A^{T} = (a_{ji})`$. The `rows` of $A$ become the `columns` of $`A^{T}`$.

The **transpose** of a matrix $A$ is obtained by flipping it over its diagonal,

Given:

$`A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 0 \\ 0 & 3 & 1 \end{pmatrix}`$

To find $`A^{T}`$, switch the rows and columns:

1. The first row of $A$ $`(1, 2, 3)`$ becomes the first column of $`A^T`$.
2. The second row of $A$ $`(2, 1, 0)`$ becomes the second column of $`A^T`$.
3. The third row of $A$ $`(0, 3, 1)`$ becomes the third column of $`A^T`$.

So:

$`A^T = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 3 \\ 3 & 0 & 1 \end{pmatrix}`$

Thus,

$`\text{If } A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 0 \\ 0 & 3 & 1 \end{pmatrix}, \text{ then } A^T = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 3 \\ 3 & 0 & 1 \end{pmatrix}`$



3. A square matrix is said to be symmetric if $`A = A^T`$, i.e. $`a_{ij} = a_{ji} \quad \forall \, i, j`$. 
A **symmetric matrix** is a square matrix that is equal to its transpose.

This means that for a matrix $A$ to be symmetric, every element in position $`(i, j)`$ must be equal to the element in position $`(j, i)`$. In other words:

$`A = A^T \quad \text{and} \quad a_{ij} = a_{ji} \quad \forall \, i, j`$

#### Example of a Symmetric Matrix

$`A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 5 & 6 \end{pmatrix}`$

#### Explanation:
In this matrix:
- $`a_{12} = a_{21} = 2`$
- $`a_{13} = a_{31} = 3`$
- $`a_{23} = a_{32} = 5`$

Since $`A = A^T`$, this matrix is symmetric.



4. A **square matrix** is said to be a **diagonal matrix**, if all the non-diagonal elements in the matrix are zero.
This means only the elements $`a_{ii}`$ (where row index $i$ equals column index $i$) can be non-zero, while all other elements $`a_{ij}`$ (where $`i \neq j`$) must be zero.

#### Example of a Diagonal Matrix

$`A = \begin{pmatrix} 3 & 0 & 0 \\ 0 & -4 & 0 \\ 0 & 0 & 1 \end{pmatrix}`$

#### Explanation:
In this matrix:
- The main diagonal elements are $3$, $-4$, and $1$.
- All non-diagonal elements are zero.

Since all non-diagonal elements are zero, $A$ is a diagonal matrix.



5. A **square matrix** is said to be the **identity matrix**, if it is a diagonal matrix and all the non-zero elements are 1.
An **identity matrix** is a special type of diagonal matrix where all the elements on the main diagonal are $1$ and all other elements are $0$.

The identity matrix is often denoted by $I$ and has the property that, for any square matrix $A$ of the same dimensions, 
multiplying $A$ by $I$ does not change $A$. In other words:

$`AI = A = IA`$

#### Example of a $3 \times 3$ Identity Matrix

$`I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}`$

#### Properties

For any square matrix $A$ of size $`n \times n`$:
- **Left Identity**: $`IA = A`$
- **Right Identity**: $`AI = A`$

The identity matrix essentially acts as a "neutral element" in matrix multiplication, similar to how multiplying a number by $1$ leaves the number unchanged in regular arithmetic.


## Determinants 
For more on Matrix determinants refer to: [Matrix Determinants](matrix_determinants.md)


## Inverses 

**Definition:** A matrix $I$ which has $`1’s`$ on the diagonal and $`0’s`$ everywhere else is called the `identity matrix`. This matrix has the property that $AI = A$.

- Example. 

A $`2 \times 2`$ identity matrix has the form $`I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}`$.

A $`3 \times 3`$ identity matrix has the form $`I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}`$

**Definition.** Let $`A = (a_{ij})`$ be a square matrix. A matrix $`B = (b_{ij})`$ is called the inverse of $A$ if $`AB = BA = I`$.

**Remark.** A matrix $A$ has an inverse if and only if $`det(A) \neq 0`$.


### Inverse of a $2 \times 2$ matrix
**Definition:** The inverse of a $`2 \times 2`$ matrix $`A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}`$ is given by;

$`A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}`$

where $`A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}`$ and $`ad - bc \neq 0`$ (since this is the determinant of $A$, it must be non-zero for the inverse to exist).

### Example
Find the inverse of the matrix 

$`A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}`$

1. **Calculate the Determinant of $A$:**
   $`\text{det}(A) = (1)(2) - (1)(1) = 2 - 1 = 1`$
  
   Since $`\text{det}(A) \neq 0`$, the inverse exists.

2. **Apply the Inverse Formula:**
   Substitute $`a = 1`$, $`b = 1`$, $`c = 1`$, and $`d = 2`$ into the formula:

   $`A^{-1} = \frac{1}{1} \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}`$

3. **Verification by Multiplying $`A^{-1} A`$:**

   $`A^{-1} A = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}`$

   Calculating each element:

   - Top-left: $`(2 \times 1) + (-1 \times 1) = 2 - 1 = 1`$
   - Top-right: $`(2 \times 1) + (-1 \times 2) = 2 - 2 = 0`$
   - Bottom-left: $`(-1 \times 1) + (1 \times 1) = -1 + 1 = 0`$
   - Bottom-right: $`(-1 \times 1) + (1 \times 2) = -1 + 2 = 1`$

   So:

   $`A^{-1} A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}`$

#### Final Result

The inverse of $`A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}`$ is:

$`A^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}`$

And as verified, $`A^{-1} A = I`$, the identity matrix.


#### Another Method for finding the Inverse, using an augmented matrix and row operations

To find the inverse of a $`2 \times 2`$ matrix $A$ using an augmented matrix and row operations, we can follow these steps:

1. Write the matrix $A$ alongside the $`2 \times 2`$ identity matrix, forming the augmented matrix $`(A | I_2)`$.
2. Use row operations to transform $A$ on the left into the identity matrix $`I_{2}`$.
3. The right side of the augmented matrix will then become $B$, which is the inverse $`A^{-1}`$.

#### Example
Let:
$`A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}`$

Start with the augmented matrix $`(A | I_{2})`$:
$`\begin{pmatrix} 1 & 1 & | & 1 & 0 \\ 1 & 2 & | & 0 & 1 \end{pmatrix}`$

**Step-by-Step Row Operations:**

1. **Row 2 Transformation**: Subtract Row 1 from Row 2 to make the first element in Row 2 zero.
   $`R_2 \to R_2 - R_1`$
   This gives:
   $`\begin{pmatrix} 1 & 1 & | & 1 & 0 \\ 0 & 1 & | & -1 & 1 \end{pmatrix}`$

2. **Row 1 Transformation**: Subtract Row 2 from Row 1 to make the second element in Row 1 zero.
   $`R_1 \to R_1 - R_2`$

   This results in:
   $`\begin{pmatrix} 1 & 0 & | & 2 & -1 \\ 0 & 1 & | & -1 & 1 \end{pmatrix}`$

At this point, the left side of the matrix is the identity matrix $`I_2`$, and the right side is the matrix $B$, which is the inverse $`A^{-1}`$.

### Result

So, we find:
$`A^{-1} = B = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}`$

This matches the previous result obtained using the formula for the inverse of a $`2 \times 2`$ matrix.

### Inverse of a $`3 \times 3`$ matrix

The method is the same as in the $`2 \times 2`$ case:

- Check determinant $A$ is non-zero.
- Rewrite as $`(A|I_3)`$.
- Use row operations to put in the form $`(I_3|A^{-1})`$.


### Example

Let:
$`A = \begin{pmatrix} 1 & -1 & 1 \\ 0 & -2 & 1 \\ -2 & -3 & 0 \end{pmatrix}`$

### Step 1: Check the Determinant

First, we need to check that the determinant of $A$ is non-zero, as this indicates that the inverse exists.

$`\text{det}(A) = 1(0 - (-3)(1)) - (-1)(0 - (-2)(1)) + 1(0 - (-2)(-2))`$

Calculating this gives:
$`= 1(0 + 3) + 1(0 + 2) + 1(0 - 4) = 3 + 2 - 4 = 1 \neq 0`$

Since the determinant is $1$, the inverse exists.

### Step 2: Rewrite as $`(A|I_3)`$

Now we rewrite the matrix $A$ alongside the $`3 \times 3`$ identity matrix:

$`(A | I_3) = \begin{pmatrix} 1 & -1 & 1 & | & 1 & 0 & 0 \\ 0 & -2 & 1 & | & 0 & 1 & 0 \\ -2 & -3 & 0 & | & 0 & 0 & 1 \end{pmatrix}`$

### Step 3: Use Row Operations

Now we perform row operations to transform the left side into the identity matrix $`I_3`$.

1. **Row 3 Transformation**: Replace Row 3 with $`R_3 + 2R_1`$ to eliminate the first element in Row 3.
   $`R_3 \to R_3 + 2R_1 \implies \begin{pmatrix} 1 & -1 & 1 & | & 1 & 0 & 0 \\ 0 & -2 & 1 & | & 0 & 1 & 0 \\ 0 & -5 & 2 & | & 2 & 0 & 1 \end{pmatrix}`$

2. **Row 2 Transformation**: Normalize Row 2 by multiplying by $`-\frac{1}{2}`$.
   $`R_2 \to -\frac{1}{2}R_2 \implies \begin{pmatrix} 1 & -1 & 1 & | & 1 & 0 & 0 \\ 0 & 1 & -\frac{1}{2} & | & 0 & -\frac{1}{2} & 0 \\ 0 & -5 & 2 & | & 2 & 0 & 1 \end{pmatrix}`$

3. **Row 3 Transformation**: Replace Row 3 with $`R_3 + 5R_2`$.
   $`R_3 \to R_3 + 5R_2 \implies \begin{pmatrix} 1 & -1 & 1 & | & 1 & 0 & 0 \\ 0 & 1 & -\frac{1}{2} & | & 0 & -\frac{1}{2} & 0 \\ 0 & 0 & -\frac{1}{2} & | & 2 & -\frac{5}{2} & 1 \end{pmatrix}`$

4. **Row 3 Normalization**: Multiply Row 3 by $`-2`$.
   $`R_3 \to -2R_3 \implies \begin{pmatrix} 1 & -1 & 1 & | & 1 & 0 & 0 \\ 0 & 1 & -\frac{1}{2} & | & 0 & -\frac{1}{2} & 0 \\ 0 & 0 & 1 & | & -4 & 5 & -2 \end{pmatrix}`$

5. **Row 2 Transformation**: Add $`\frac{1}{2}R_3`$ to Row 2.
   $`R_2 \to R_2 + \frac{1}{2}R_3 \implies \begin{pmatrix} 1 & -1 & 1 & | & 1 & 0 & 0 \\ 0 & 1 & 0 & | & -2 & 2 & -1 \\ 0 & 0 & 1 & | & -4 & 5 & -2 \end{pmatrix}`$

6. **Row 1 Transformation**: Eliminate the second element of Row 1 by adding Row 2.
   $`R_1 \to R_1 + R_2 \implies \begin{pmatrix} 1 & 0 & 0 & | & 3 & -3 & 1 \\ 0 & 1 & 0 & | & -2 & 2 & -1 \\ 0 & 0 & 1 & | & -4 & 5 & -2 \end{pmatrix}`$

### Final Result

Now that the left side of the matrix is the identity matrix, the right side gives us the inverse $`A^{-1}`$:

$`A^{-1} = \begin{pmatrix} 3 & -3 & 1 \\ -2 & 2 & -1 \\ -4 & 5 & -2 \end{pmatrix}`$

This is the inverse of the matrix $A$.


Also refer to [Matrix Determinants](Inverse_matrix.md) for a bit more details on Matrix Inverse.


## Eigenvalues and Eigenvectors and Diagonalization

**Definition:** In linear algebra, **eigenvalues** and **eigenvectors** are fundamental concepts that help us understand how linear transformations behave. 
When we apply a transformation $A$ (a square matrix) to a vector $`\vec{x}`$, if the result is a scalar multiple of $`\vec{x}`$, 
then $`\vec{x}`$ is called an **eigenvector** of $A$, and the scalar $`\lambda`$ is the corresponding **eigenvalue**.


Suppose that $A$ is an $`n \times n`$ square matrix. Suppose that $`\vec{x}`$ is a non-zero vector in $`\mathbb{R}^n`$ and that $`\lambda`$ is 
a scalar so that,

$`A \vec{x} = \lambda \vec{x}`$

We then call $`\vec{x}`$ an eigenvector of $A$ and $`\lambda`$ an eigenvalue of $A$.

Note:
- $A$ is an  $`n \times n`$ matrix,
- $`\vec{x}`$ is a non-zero vector in $`\mathbb{R}^n`$,
- $`\lambda`$ is a scalar.


The goal is to find such vectors $`\vec{x}`$ and corresponding values $`\lambda`$ for a given matrix $A$.


### Example

Let’s consider the matrix:
$`A = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}`$


1. **First Eigenvector and Eigenvalue**:
   - Take the vector $\vec{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
   - Multiply $A$ by $\vec{x}$:
     $`A \vec{x} = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 10 \\ 5 \end{pmatrix} = 5 \begin{pmatrix} 2 \\ 1 \end{pmatrix}`$
   - Since $`A \vec{x} = 5 \vec{x}`$, $`\lambda = 5`$ is an eigenvalue of $A$, and $`\vec{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}`$ is the associated eigenvector.


2. **Second Eigenvector and Eigenvalue**:
   - Now, take the vector $\vec{x} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$.
   - Multiply $A$ by $\vec{x}$:
     $`A \vec{x} = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} -2 \\ 2 \end{pmatrix} = 2 \begin{pmatrix} -1 \\ 1 \end{pmatrix}`$
   - Since $`A \vec{x} = 2 \vec{x}`$, $`\lambda = 2`$ is another eigenvalue of $A$, and $`\vec{x} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}`$ is the associated eigenvector.


###  Method to find eigenvalues and eigenvectors

We start with $`A \vec{x} = \lambda \vec{x}`$ and rewrite it as follows,

$`A \vec{x} = \lambda I \vec{x}`$

$`\lambda I \vec{x} - A \vec{x} = 0`$

$`(\lambda I - A) \vec{x} = 0`$

**THEOREM:** $`\lambda`$ is an eigenvalue of $A$ if and only if $`\lambda I - A`$ is not invertible if and only it $`det (\lambda I - A) = 0`$.

where $I$ is the identity matrix of the same dimension as $A$. Solving this equation gives the possible values for $`\lambda`$. 
Once we have $`\lambda`$, we can substitute it back into $`(A - \lambda I) \vec{x} = 0`$ to find the corresponding eigenvectors $`\vec{x}`$.



### Steps to find eigenvalues and eigenvectors:


















































# Reference

- Matrices : https://byjus.com/jee/matrices/



#### Videos

- Inverse of a 3x3 Matrix  : https://www.youtube.com/watch?v=Fg7_mv3izR0

- Inverse matrices, column space and null space | Chapter 7, Essence of linear algebra (3Blue1Brown) : https://www.youtube.com/watch?v=uQhTuRlWMxw&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab

- Eigenvalues and Eigenvectors : https://www.youtube.com/watch?v=BWvx4wUSGdA&t=493s

- 3 x 3 eigenvalues and eigenvectors : https://www.youtube.com/watch?v=qa9fI6qvUQY

- Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra : https://www.youtube.com/watch?v=PFDu9oVAE-g


---
- Gil Strang's Final 18.06 Linear Algebra Lecture (MIT OpenCourseWare)  : https://www.youtube.com/watch?v=lUUte2o2Sn8
---























































































































































