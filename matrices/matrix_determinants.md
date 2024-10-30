## Matrix Determinants

### Definition

A determinant is a scalar value associated with a square matrix. It has profound significance in various fields of mathematics and engineering,
notably in linear algebra, calculus, and differential equations. 

### What is the Determinant?

The determinant of a matrix $A$, denoted $det(A)$ or $|A|$, provides important information about the matrix and the linear transformation it represents.
In geometric terms, the absolute value of the determinant of a `2D` matrix represents the area scaling factor for the transformation, while in `3D`, it 
represents the volume scaling factor.


### Determinants in Matrices
Let's look at the general case to see how we compute the determinant;

Let $A$ be an $NxN$ matrix: 
    
$det(A) = \sum_{j=1}^{N} (-1)^{i+j} A_{i,j}M_{i,j}$

where
- `M` is the determinant of the sub-matrix constructed by removing the $ith$ row and $jth$ column of $A$.

or

Given an `NxN` matrix $A$ = $[a_{ij}]$. The determinant of $A$, denoted $det(A)$ or $|A|$, can be computed by expanding
along the first row (or any other row or column):

$\det(A) = \sum_{j=1}^{N} (-1)^{1+j} a_{1j} \cdot \det(A_{1j})$

where:
- $a_{1j}$ is the element in the first row and $j-th$ column.
- $(-1)^{1+j}$ is the sign factor, which alternates based on the position of $a_{1j}$.
- $A_{1j}$ is the $(N-1) \times (N-1)$ submatrix formed by removing the first row and $j-th$ column from $A$.


This expression is referred to as the `Laplace Expansion`. There is a quite a bit to unpack here, but it's rather simple
once you get passed the symbolic representation. It basically says to divide the matrix $A$ into smaller and smaller
sub-matrices until you can compute the determinant with relative ease. We also add a "weight" to each subsequent sub-matrix
via the `ith` and `jth` column of $A$. This generalization is quite easier to understand in the `3x3` case. 

However, let's first discuss the simplest computation: 
1. **2x2 Matrix**: 

Let $A$ be a `2x2` matrix 

```math
A = \begin{bmatrix} a & b \\
                    c & d
                    \end{bmatrix}
```


We compute the determinant of a `2x2` matrix by finding the difference of the main diagonal and the counter diagonal.

```math
det(A) = det(\begin{bmatrix} a & b \\  c & d  \end{bmatrix}) =  ad - bc
```

The sub-matrices in the Laplace expansion can be reduced to the `2x2` case. This can be visualized as the area of a parallelogram spanned by two vectors (formed by the rows and columns).


2. **3x3 Matrix**:

Let $A$ be a `3x3` matrix

```math
A = \begin{bmatrix} a & b & c \\ d & e & f \\  g & h & i  \end{bmatrix}
```

```math
det(A) = det(\begin{bmatrix} a & b & c \\ d & e & f \\  g & h & i  \end{bmatrix}) = a * det (\begin{bmatrix} e & f \\  h & i  \end{bmatrix}) - 
b * det (\begin{bmatrix} d & f \\  g & i  \end{bmatrix}) + c * det (\begin{bmatrix} d & e \\  g & h  \end{bmatrix})
```

```math
det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
```

Notice that the `3x3` case is a direct application of the Laplace expansion. We hold the top row fixed (but it could be any row or column), which act as
the multipliers, and reduce the primary matrix down into `2x2` sub-matrices. Since we can easily compute the determinant of a `2x2` sub-matrix, the computation
becomes much simpler. it is also important to notice the alternating plus and minus signs. This comes from the `-1` term in the Laplace expansion.
We alternate signs as we create sub-matrices. 

This determinant represents the volume of a parallelepiped in three dimensions. Determinants of larger matrices are computed through recursive expansion
or other methods (LU decomposition or row reduction).


### Geometric Interpretation
The algebraic interpretation of a determinant is great at providing a basis for computing a determinant. it does not, however, provide an intuitive 
understanding of determinants. it makes it seem like the determinant is merely a product of numbers. 

![2x2 Geographic interpretation](/assests/Untitled-2024-09-14-1236.png)

The `2x2` depiction of matrix $A$ is seen above. The above parallelogram is constructed by recognizing that the matrix $A$ forms two linear maps:
- one that maps the standard basis vectors to the rows of $A$ and
- one that maps the standard basis vectors to the columns of $A$. 
Put another way, we can plot the elements of $A$ as seen in the diagram. This makes the determinant the area of the parallelogram! The area, then, represents
the scale by which $A$ transforms other areas. 

#### What of Negative Determinants? How can there be negative area?
When we apply the sign to the area, we have an oriented area. The only difference between an oriented area and the area is the sign: a negative
oriented area implies the angle from the first and second vectors turns in a clockwise direction rather than a counterclockwise direction. However, the
magnitude of the area is the same between the two. It is analogous vectors having a magnitude and direction. A vector does not have a negative magnitude;
it simply has a direction associated with the magnitude. 

The sign of the determinant reflects orientation:
- A positive determinant indicates that the orientation is preserved.
- A negative determinant indicates that the transformation reverses orientation (like flipping).

#### What about a 3x3 or NxN case?
The same concept is applied here! The only thing that changes is the shape. In the `3x3` case, it forms a `parallelepiped` and in the `NxN` case, it forms
a `parallelotope`. That means, the `3x3` case calculates the `volume`, the `4x4` case calculates a `hypervolume`, etc. It becomes a lot more abstract above 
three dimensions, but the fundamentals remain the same; we are calculating the scale at which $A$ transforms other objects.


### Properties of Determinants 
Determinants have several fundamental properties
- `Multiplicative`: For square matrices $A$ and $B$, $det(AB) = det(A) \times det(B)$.
- `Transpose`: $det(A) = det(A^{T})$. The transpose of $A$ has the same determinant as $A$.
- `Inverse`: For an invertible matrix $A$, $det(A^{-1}) = 1/det(A)$.
- `Row Operations`:
  - Swapping two rows or columns changes the sign of the determinant.
  - Multiplying a row by a scalar $k$ scales the determinant by $k$.
  - Adding a multiple of one row to another row does not change the determinant. 
  - If two rows are equal, the determinant is zero.
  - if a matrix is singular, the determinant is zero.


### Computing the Determinant for Larger Matrices
For Larger matrices, determinants are computed using methods like:
- `Row Reduction`: Transforming the matrix to an upper triangular form using row operations, where the determinant is the product of the diagonal elements.
- `Laplace Expansion`: Expanding along rows or columns using minors and cofactors, though this is computationally expensive for large matrices.
- `LU Decomposition`: This method is efficient for computation. It decomposes $A$ into lower and upper triangular matrices, $A = LU$, and then 
$det(A) = det(L) \times det(U)$, with $det(L)$ typically being `1` for matrices transformed into a standard form. 


### Application of Determinants
Determinants are essential in various fields:
- `Solving Linear Systems`: In Cramer's rule, determinants are used to find solutions to systems of linear equations.
- `Eigenvalues and Eigenvectors`: The characteristic polynomial of a matrix, which is used to find eigenvalues, is derived from the determinant of 
$A - \lambda I$, where $\lambda$ is a scalar.
- `Matrix Inverse`: A square matrix $A$ is invertible if and only if $det(A) \neq 0$.
- `Volume and Area Transformations`: Determinants measure how a transformation scales areas and volumes. For example, if $T$ is a linear transformation represented
by matrix $A$, the volume of any region transformed by $T$ is scaled by $| det(A)|$.


### Example Calculation
Consider a `3x3` matrix:

```math
A = \begin{bmatrix}
2 & 3 & 1 \\ 
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix},
```

using cofactor expansion along the first row;

```math
\det(A) = 2 \begin{vmatrix} 5 & 6 \\ 8 & 9 \end{vmatrix} - 3 \begin{vmatrix} 4 & 6 \\ 7 & 9 \end{vmatrix} + 1 \begin{vmatrix} 4 & 5 \\ 7 & 8 \end{vmatrix}
```

Calculating each minor determinant:
```math
= 2(5 \cdot 9 - 6 \cdot 8) - 3(4 \cdot 9 - 6 \cdot 7) + 1(4 \cdot 8 - 5 \cdot 7)
```

```math
= 2(-3) - 3(-6) + 1(-3)
```

```math
= -6 + 18 - 3 = 9
```

Thus, the determinant of \( A \) is:
```math
\det(A) = 9
```


### Summary
Determinants are powerful tools in matrix algebra, with broad applications from solving equations to analyzing transformations. Their properties and
efficient calculation methods allow for understanding linear transformations and their impact on space. 


### Reference:

- Laplace expansion (Wikipedia): [Laplace expansion](https://en.wikipedia.org/wiki/Laplace_expansion)


- The determinant | Chapter 6, Essence of linear algebra (3Blue1Brown)

[![IMAGE ALT TEXT](http://img.youtube.com/vi/Ip3X9LOh2dk/0.jpg)](http://www.youtube.com/watch?v=Ip3X9LOh2dk "The determinant | Chapter 6, Essence of linear algebra")





