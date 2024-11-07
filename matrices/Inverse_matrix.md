# Inverse Matrices

For an $n \times n$ square matrix $A$, the inverse $A^{-1}$ exists if and only if the matrix is *non-singular*, 
meaning its determinant is non-zero, i.e., $`det(A) \neq 0`$. The general formula for computing the inverse of a matrix $A$ involves:

### 1. **The Adjugate Method**

For a matrix $A = [a_{ij}]$, the inverse $A^{-1}$ can be computed using the formula:

$`A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)`$

where:
- $`det(A)`$ is the determinant of $A$.
- $`\text{adj}(A)`$ is the adjugate (or adjoint) of $A$, which is the transpose of the cofactor matrix of $A$.
- (Refer to [Adjugate Matrix](adjugate_matrix.md) for more on Adjugate matrix)

### 2. **Steps to Compute the Inverse Using the Adjugate Method**

1. **Calculate the Determinant** of $A$:
   - For a $2 \times 2$ matrix:
     $`A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}`$,  $`\det(A) = ad - bc`$
   
   - For a $`3 \times 3`$ matrix, the determinant is calculated using cofactor expansion, and so on for larger matrices.

2. **Find the Matrix of Minors**:
   - The minor of an element $`a_{ij}`$ is the determinant of the submatrix formed by removing the $`i`$-th row and $`j`$-th column.

3. **Create the Cofactor Matrix**:
   - Apply a checkerboard pattern of signs $`(+/-)`$ to the matrix of minors to obtain the cofactor matrix.

4. **Transpose the Cofactor Matrix** to get the Adjugate (Adjoint) Matrix.

5. **Divide by the Determinant**:
   - Multiply each element of the adjugate matrix by $`\frac{1}{\det(A)}`$.

### Example: Inverse of a 2x2 Matrix
For a $2 \times 2$ matrix: 

$`A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}`$

If $`\det(A) = ad - bc \neq 0`$, 

then: 

$`A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}`$

For the matrix 

$`A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}`$

The inverse is calculated as; 

$`A^{-1} = \frac{1}{1 \times 2 - 1 \times 1} \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}`$

$`A^{-1} = \frac{1}{1} \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}  = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}`$



### Example: Inverse of a 3x3 Matrix
For a $`3 \times 3`$ matrix: 

$`A = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix}`$

1. Compute $`\det(A)`$ using cofactor expansion.
2. Find the cofactor matrix and its transpose (adjugate).
3. Multiply the adjugate by $`\frac{1}{\det(A)}`$ to get $`A^{-1}`$.



**For Example** 

Let matrix,  

$`A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 0 & 1 \\ -1 & 1 & 2 \end{pmatrix}`$

1. **Computing the matrix of `minors` and `cofactors` as thus**;

- $`M_{11} = (-1)^{1+1} \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix} = -1`$
- $`M_{12} = (1)^{1+2} \begin{pmatrix} 2 & 1 \\ -1 & 2 \end{pmatrix} = -5`$
- $`M_{13} = (-1)^{1+3} \begin{pmatrix} 2 & 0 \\ -1 & 1 \end{pmatrix} = 2`$
- $`M_{21} = (-1)^{2+1} \begin{pmatrix} 2 & 3 \\ 1 & 2 \end{pmatrix} = -1`$
- $`M_{22} = (-1)^{2+2} \begin{pmatrix} 1 & 3 \\ -1 & 2 \end{pmatrix} = 5`$
- $`M_{23} = (-1)^{2+3} \begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix} = -3`$
- $`M_{31} = (-1)^{3+1} \begin{pmatrix} 2 & 3 \\ 0 & 1 \end{pmatrix} = 2`$
- $`M_{32} = (-1)^{3+2} \begin{pmatrix} 1 & 3 \\ 2 & 1 \end{pmatrix} = 5`$
- $`M_{33} = (-1)^{3+3} \begin{pmatrix} 1 & 2 \\ 2 & 0 \end{pmatrix} = -4`$


2. **Construct the Cofactor Matrix**:
The `matrix` of cofactors is  

$`\begin{pmatrix} -1 & -5 & 2 \\ -1 & 5 & -3 \\ 2 & 5 & -4 \end{pmatrix}`$

3. **Transpose the Cofactor Matrix** to get the adjugate:

The `adjugate` is the transpose of the matrix of cofactors

$`\begin{pmatrix} -1 & -1 & 2 \\ -5 & 5 & 5 \\ 2 & -3 & -4 \end{pmatrix}`$


**THEOREM** A square matrix $A$ is invertible if and only if $`det(A) \neq 0`$. If $`det(A) \neq 0`$ then the inverse of $A$ is given by

$`A^{-1} = \frac{1}{\det(A)} \text{adj}(A)`$

**EXAMPLE**

For the $`3 \times 3`$ case example matrix; 

$`A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 0 & 1 \\ -1 & 1 & 2 \end{pmatrix}`$ has $`det(A) = -5`$. (Refer to [Matrix Determinants](matrix_determinants.md) for more on matrix determinant)

The inverse of $A$ therefore exists and is equal to 

$`A^{-1} = -\frac{1}{5} \begin{pmatrix} -1 & -1 & 2 \\ -5 & 5 & 5 \\ 2 & -3 & -4 \end{pmatrix}`$

Can also be written as; 

$`A^{-1} =  \begin{pmatrix} \frac{1}{5} & \frac{1}{5} & -\frac{2}{5} \\ 1 & -1 & -1 \\ -\frac{2}{5} & \frac{3}{5} & \frac{4}{5} \end{pmatrix}`$


This method scales for larger matrices but becomes computationally expensive, so algorithmic or numerical approaches are typically used for matrices larger than $`3 \times 3`$.



### Reference

- Inverse Matrix : [Inverse Matrix](http://www.thphys.nuim.ie/Notes/EE112/09_Inverse_Matrix.pdf)

- The Engineering Maths First Aid Kit (The inverse of a matrix) : [The inverse of a matrix](https://lcn.people.uic.edu/classes/che205s17/docs/che205s17_reading_05a.pdf)

- The adjugate matrix and the inverse matrix [The adjugate matrix and the inverse matrix](https://www.macs.hw.ac.uk/~markl/teaching/Inverses.pdf)

- Lesson Name: Adjoint of a Matrix and Inverse of a Matrix [Adjoint and Inverse of a Matrix](https://cdn1.byjus.com/wp-content/uploads/2019/04/Adjoint-and-Inverse-of-a-Matrix.pdf)

- The inverse of a 2 × 2 matrix : [The inverse of a 2 × 2 matrix](https://www.mathcentre.ac.uk/resources/uploaded/sigma-matrices7-2009-1.pdf)

- Introduction to Linear Algebra, 5th Edition : [Inverse Matrices](https://math.mit.edu/~gs/linearalgebra/ila5/linearalgebra5_2-5.pdf)


### Videos

Lec 3: Matrices; inverse matrices | MIT 18.02 Multivariable Calculus, Fall 2007 : https://www.youtube.com/watch?v=bHdzkFrgRcA

20. Cramer's Rule, Inverse Matrix, and Volume : https://www.youtube.com/watch?v=QNpj-gOXW9M

Inverse matrices, column space and null space | Chapter 7, Essence of linear algebra : https://www.youtube.com/watch?v=uQhTuRlWMxw&t=1s

### Code implementation from Scratch (using python)

- [Matrix Inverse from scratch python](../code_implementation/matrix_inverse.py)
