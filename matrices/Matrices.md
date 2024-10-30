# Matrices

## Introduction

**Definition:** A $m × n$ matrix is a rectangular array of numbers having $m$ rows and $n$ columns.

$
A = \begin{pmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
a_{31} & a_{32} & \dots & a_{3n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{pmatrix}
$

#### Explanation of the Matrix Notation

- $a_{ij}$ represents the element in the $i-th$ row and $j-th$ column. We sometimes denote $A$ by
- The matrix has:
  - $m$ **rows** (indicated by indices $i = 1, 2, \dots, m$).
  - $n$ **columns** (indicated by indices $j = 1, 2, \dots, n$).

This general form allows each element $a_{ij}$ to vary, making it applicable to any rectangular or square matrix with $m$ rows and $n$ columns.


## Matrix Operation

### 1. **Addition**

We can only add two matrices of the same dimension i.e. same number of `rows` and `columns`. We then add element-wise

`Example`:

Here's an example of **matrix addition** using two $2 \times 2$ matrices:

Let:

$
A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \quad \text{and} \quad B = \begin{pmatrix} 4 & 3 \\ 5 & 6 \end{pmatrix}
$

To find $A + B$:

1. **Add the corresponding elements** from matrices $A$ and $B$.
   - Top-left: $2 + 4 = 6$
   - Top-right: $1 + 3 = 4$
   - Bottom-left: $1 + 5 = 6$
   - Bottom-right: $3 + 6 = 9$

So,

$
A + B = \begin{pmatrix} 2 + 4 & 1 + 3 \\ 1 + 5 & 3 + 6 \end{pmatrix} = \begin{pmatrix} 6 & 4 \\ 6 & 9 \end{pmatrix}
$

Thus,

$
\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} + \begin{pmatrix} 4 & 3 \\ 5 & 6 \end{pmatrix} = \begin{pmatrix} 6 & 4 \\ 6 & 9 \end{pmatrix}
$



### 2. **Scalar Multiplication**

if $c$ is a real number and $A = (a_{ij})_{m \times n}$ is a matrix then $cA = (ca_{ij})_{m \times n}$.

`Example`:

This example demonstrates **scalar multiplication** of a matrix. When a real number $c$ multiplies each element of a matrix $A$, it is called **scalar multiplication**.

Let:
$
c = 5 \quad \text{and} \quad A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}
$

Then, $cA$ is calculated by multiplying each element of $A$ by $c$.

#### Steps
1. Multiply $c = 5$ with each element in $A$:
   - Top-left: $5 \times 2 = 10$
   - Top-right: $5 \times 1 = 5$
   - Bottom-left: $5 \times 1 = 5$
   - Bottom-right: $5 \times 3 = 15$

So:

$
cA = 5 \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 10 & 5 \\ 5 & 15 \end{pmatrix}
$

Thus,

$
5 \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 10 & 5 \\ 5 & 15 \end{pmatrix}
$


### 3. **Matrix Multiplication**

Given a matrix  $A = (a_{ij})_{m \times n}$  and a matrix $B = (b_{ij})_{r \times s}$, we can only multiply
them if $n = r$. In such a case the multiplication is defined to be the matrix $C = (c_{ij})_{m \times s}$ as follows:


$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
$

We may view the $c_{ij}$th element as the dot product of the $ith$ row of the matrix $A$ and $jth$ column of the matrix $B$.

#### Explanation

- $c_{ij}$: The element in the $i$-th row and $j$-th column of matrix $C$.
- $\sum_{k=1}^{n}$: This is a summation over $k$, where $k$ goes from $1$ to $n$ (the common dimension of $A$ and $B$).
- $a_{ik}$: The element in the $i$-th row and $k$-th column of matrix $A$.
- $b_{kj}$: The element in the $k$-th row and $j$-th column of matrix $B$.

#### Matrix Multiplication Example

Suppose:

$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \quad \text{and} \quad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}
$

To find $C = AB$:

1. **Calculate** $c_{11}$:
   $
   c_{11} = (1 \times 5) + (2 \times 7) = 5 + 14 = 19
   $

2. **Calculate** $c_{12}$:
   $
   c_{12} = (1 \times 6) + (2 \times 8) = 6 + 16 = 22
   $

3. **Calculate** $c_{21}$:
   $
   c_{21} = (3 \times 5) + (4 \times 7) = 15 + 28 = 43
   $

4. **Calculate** $c_{22}$:
   $
   c_{22} = (3 \times 6) + (4 \times 8) = 18 + 32 = 50
   $

So:

$
C = AB = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}
$



## Special matrices

1. A matrix is called a **square matrix** if the number of `rows` is equal to the number of `columns`.



2. The transpose of a square matrix $A = (a_{ij})$ is the matrix $A^{T} = (a_{ji})$. The `rows` of $A$ become the `columns` of $A^{T}$.

The **transpose** of a matrix $A$ is obtained by flipping it over its diagonal,

Given:

$
A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 0 \\ 0 & 3 & 1 \end{pmatrix}
$

To find $A^{T}$, switch the rows and columns:

1. The first row of $A$ $(1, 2, 3)$ becomes the first column of $A^T$.
2. The second row of $A$ $(2, 1, 0)$ becomes the second column of $A^T$.
3. The third row of $A$ $(0, 3, 1)$ becomes the third column of $A^T$.

So:

$
A^T = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 3 \\ 3 & 0 & 1 \end{pmatrix}
$

Thus,

$
\text{If } A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 0 \\ 0 & 3 & 1 \end{pmatrix}, \text{ then } A^T = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 3 \\ 3 & 0 & 1 \end{pmatrix}
$



3. A square matrix is said to be symmetric if $A = A^T$, i.e. $a_{ij} = a_{ji} \quad \forall \, i, j$. 
A **symmetric matrix** is a square matrix that is equal to its transpose.

This means that for a matrix $A$ to be symmetric, every element in position $(i, j)$ must be equal to the element in position $(j, i)$. In other words:

$
A = A^T \quad \text{and} \quad a_{ij} = a_{ji} \quad \forall \, i, j
$

#### Example of a Symmetric Matrix

$
A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 5 & 6 \end{pmatrix}
$

#### Explanation:
In this matrix:
- $a_{12} = a_{21} = 2$
- $a_{13} = a_{31} = 3$
- $a_{23} = a_{32} = 5$

Since $A = A^T$, this matrix is symmetric.



4. A **square matrix** is said to be a **diagonal matrix**, if all the non-diagonal elements in the matrix are zero.
This means only the elements $a_{ii}$ (where row index $i$ equals column index $i$) can be non-zero, while all other elements $a_{ij}$ (where $i \neq j$) must be zero.

#### Example of a Diagonal Matrix

$
A = \begin{pmatrix} 3 & 0 & 0 \\ 0 & -4 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$

#### Explanation:
In this matrix:
- The main diagonal elements are $3$, $-4$, and $1$.
- All non-diagonal elements are zero.

Since all non-diagonal elements are zero, $A$ is a diagonal matrix.



5. A **square matrix** is said to be the **identity matrix**, if it is a diagonal matrix and all the non-zero elements are 1.
An **identity matrix** is a special type of diagonal matrix where all the elements on the main diagonal are $1$ and all other elements are $0$.

The identity matrix is often denoted by $I$ and has the property that, for any square matrix $A$ of the same dimensions, 
multiplying $A$ by $I$ does not change $A$. In other words:

$
AI = A = IA
$

#### Example of a $3 \times 3$ Identity Matrix

$
I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$

#### Properties

For any square matrix $A$ of size $n \times n$:
- **Left Identity**: $IA = A$
- **Right Identity**: $AI = A$

The identity matrix essentially acts as a "neutral element" in matrix multiplication, similar to how multiplying a number by $1$ leaves the number unchanged in regular arithmetic.


## Determinants 
Refer to this [Matrix Determinants](matrices/matrix_determinants.md)

[//]: # (matrices/matrix_determinants.md)

































































































































