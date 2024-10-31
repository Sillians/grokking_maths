# Inverse Matrices

**Definition:** A matrix $I$ which has $1’s$ on the diagonal and $0’s$ everywhere else is called the `identity matrix`. This matrix has the property that $AI = A$.

- Example. 

A $2 \times 2$ identity matrix has the form $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.

A $3 \times 3$ identity matrix has the form $I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$

**Definition.** Let $A = (a_{ij})$ be a square matrix. A matrix $B = (b_{ij})$ is called the inverse of $A$ if $AB = BA = I$.

**Remark.** A matrix $A$ has an inverse if and only if $det(A) \neq 0$.


### Inverse of a $2 \times 2$ matrix
**Definition:** The inverse of a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is given by;

$
A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$

where $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ and $ad - bc \neq 0$ (since this is the determinant of $A$, it must be non-zero for the inverse to exist).

### Example
Find the inverse of the matrix 

$
A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}
$

1. **Calculate the Determinant of $A$:**
   $
   \text{det}(A) = (1)(2) - (1)(1) = 2 - 1 = 1
   $
   Since $\text{det}(A) \neq 0$, the inverse exists.

2. **Apply the Inverse Formula:**
   Substitute $a = 1$, $b = 1$, $c = 1$, and $d = 2$ into the formula:

   $
   A^{-1} = \frac{1}{1} \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}
   $

3. **Verification by Multiplying $A^{-1} A$:**

   $
   A^{-1} A = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}
   $

   Calculating each element:

   - Top-left: $(2 \times 1) + (-1 \times 1) = 2 - 1 = 1$
   - Top-right: $(2 \times 1) + (-1 \times 2) = 2 - 2 = 0$
   - Bottom-left: $(-1 \times 1) + (1 \times 1) = -1 + 1 = 0$
   - Bottom-right: $(-1 \times 1) + (1 \times 2) = -1 + 2 = 1$

   So:

   $
   A^{-1} A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
   $

#### Final Result

The inverse of $A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ is:

$
A^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}
$

And as verified, $A^{-1} A = I$, the identity matrix.





