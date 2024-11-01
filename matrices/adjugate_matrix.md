## Adjugate (Adjoint) of a Matrix

The adjoint of a matrix (also called the adjugate of a matrix) is defined as the transpose of the cofactor matrix of that particular matrix.
For a matrix $A$, the adjoint is denoted as $adj(A)$. The **adjugate matrix** is an essential tool in matrix algebra, particularly in finding the inverse of a matrix.

The adjugate matrix is created by following a series of steps involving cofactors and transposition.

### Definition of the Adjugate Matrix

For an $n \times n$ matrix $A = [a_{ij}]$, the **adjugate** (or **adjoint**) matrix, denoted as $\text{adj}(A)$, is the **transpose of the cofactor matrix** of $A$.

The formula for finding the inverse of a matrix $A$, if $A$ is invertible (i.e., $\det(A) \neq 0$), involves the adjugate:
```math
A^{-1} = \frac{1}{\det(A)} \text{adj}(A)
```

---

## Steps to Find the Adjugate Matrix

### The $2 \times 2$ matrix case:
Let 
```math
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
```

We construct the adjugate as follows;

- Replace each entry $a_{ij}$ of $A$ by the element remaining when the $ith$ row and $jth$ column are crossed
```math
\begin{pmatrix} d & c \\ b & a \end{pmatrix}.
```

- Use the following matrix of signs
```math
\begin{pmatrix} + & - \\ - & + \end{pmatrix},
```

where the entry in row $i$ and column $j$ is the sign of $(-1)^{i+j}$, to get 
```math
\begin{pmatrix} d & -c \\ -b & a \end{pmatrix}.
```

- Take the transpose of this matrix to get the adjugate of $A$
```math
adj(A) = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}.
```

- Observe that

$A adj(A) = det(A)I = adj(A)A$.

**Example** Let 
```math
A = \begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix}.
```

- $M_{11} = 1$
- $M_{12} = -3$
- $M_{21} = -2$
- $M_{22} = 1$

This becomes; 
```math
A = \begin{pmatrix} 1 & -3 \\ -2 & 1 \end{pmatrix}.
```


Then, taking the `Transpose`, we get

```math
adj(A) = \begin{pmatrix} 1 & -2 \\ -3 & 1 \end{pmatrix}.
```




### The $3 \times 3$ matrix case:

1. **Calculate the Minor of Each Element**:
- The **minor** $M_{ij}$ of an element $a_{ij}$ is the determinant of the `submatrix` that remains after removing the $i$-th row and $j$-th column from $A$.

- For example, if $A$ is a $3 \times 3$ matrix:
```math
A = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix}
```
   
then the minor $M_{11}$ of element $a_{11} = a$ is:
```math
M_{11} = \det\begin{pmatrix} e & f \\ h & i \end{pmatrix} = ei - fh
```

2. **Apply Cofactor Signs**:
- Each minor $M_{ij}$ is assigned a **cofactor sign** $(-1)^{i+j}$ based on its position in the matrix. The cofactor $C_{ij}$ for each element $a_{ij}$ is:
  ```math
  C_{ij} = (-1)^{i+j} M_{ij}
  ```

- For example, for the $3 \times 3$ matrix above:
  - The cofactor of $a_{11}$ is $C_{11} = M_{11}$,
  - The cofactor of $a_{12}$ is $C_{12} = -M_{12}$, and so on.

- Applying these signs creates the **cofactor matrix** $C$.


3. **Construct the Cofactor Matrix**:
- Organize all calculated cofactors $C_{ij}$ into a matrix with the same dimensions as $A$:
  ```math
  C = \begin{pmatrix} C_{11} & C_{12} & \dots & C_{1n} \\ C_{21} & C_{22} & \dots & C_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ C_{n1} & C_{n2} & \dots & C_{nn} \end{pmatrix}
  ```


4. **Transpose the Cofactor Matrix**:
- Finally, the adjugate matrix $\text{adj}(A)$ is the transpose of the cofactor matrix $C$:
  ```math
  \text{adj}(A) = C^{T}
  ```
- This means we swap rows and columns of $C$ to obtain $\text{adj}(A)$.

---


#### Can also be stated as;

Let $A$ be an $n \times n$ matrix with entries $a_{ij}$. We define its adjugate as the result of the following sequence of operations.

- Choose an entry $a_{ij}$, in the matrix $A$.
- Crossing out the entries in row $i$ and column $j$, an $(n - 1) \times (n - 1)$ matrix is constructed, denoted by $M(A)_{ij}$, and called a **submatrix**.
- The determinant $det(M(A)_{ij})$ is called the **minor** of the element $a_{ij}$.
- If $det(M(A)_{ij})$ is multiplied by the corresponding sign, we get the `cofactor` $c_{ij} = (-1)^{i+j} det(M(A)_{ij})$ of the element $a_{ij}$.
- Replace each element $a_{ij}$ by its cofactor to obtain the matrix $C(A)$ of cofactors of $A$.
- The transpose of the matrix of cofactors $C(A)$ is the adjugate.

---


**Example** 

Let 

$
A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 0 & 1 \\ -1 & 1 & 2 \end{pmatrix}
$

1. **Computing the matrix of `minors` and `cofactors` as thus**;

- ```mathM_{11} = (-1)^{1+1} \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix} = -1```
- ```mathM_{12} = (1)^{1+2} \begin{pmatrix} 2 & 1 \\ -1 & 2 \end{pmatrix} = -5$
- $M_{13} = (-1)^{1+3} \begin{pmatrix} 2 & 0 \\ -1 & 1 \end{pmatrix} = 2$
- $M_{21} = (-1)^{2+1} \begin{pmatrix} 2 & 3 \\ 1 & 2 \end{pmatrix} = -1$
- $M_{22} = (-1)^{2+2} \begin{pmatrix} 1 & 3 \\ -1 & 2 \end{pmatrix} = 5$
- $M_{23} = (-1)^{2+3} \begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix} = -3$
- $M_{31} = (-1)^{3+1} \begin{pmatrix} 2 & 3 \\ 0 & 1 \end{pmatrix} = 2$
- $M_{32} = (-1)^{3+2} \begin{pmatrix} 1 & 3 \\ 2 & 1 \end{pmatrix} = 5$
- $M_{33} = (-1)^{3+3} \begin{pmatrix} 1 & 2 \\ 2 & 0 \end{pmatrix} = -4$


2. **Construct the Cofactor Matrix**:
The `matrix` of cofactors is 

```math
\begin{pmatrix} -1 & -5 & 2 \\ -1 & 5 & -3 \\ 2 & 5 & -4 \end{pmatrix}
```

3. **Transpose the Cofactor Matrix** to get the adjugate:
The `adjugate` is the transpose of the matrix of cofactors

```math
\begin{pmatrix} -1 & -1 & 2 \\ -5 & 5 & 5 \\ 2 & -3 & -4 \end{pmatrix}
```


**THEOREM** A square matrix $A$ is invertible if and only if $det(A) /neq 0$. If $det(A) /neq 0$ then the inverse of $A$ is given by

```math
A^{-1} = \frac{1}{\det(A)} \text{adj}(A)
```

**EXAMPLE**

For the $3 \times 3$ case example matrix; $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 0 & 1 \\ -1 & 1 & 2 \end{pmatrix}$ has $det(A) = -5$. (Refer to [Matrix Determinants](matrix_determinants.md) for more on matrix determinant)

The inverse of $A$ therefore exists and is equal to 

```math
A^{-1} = -\frac{1}{5} \begin{pmatrix} -1 & -1 & 2 \\ -5 & 5 & 5 \\ 2 & -3 & -4 \end{pmatrix}
```

Can also be written as;

```math
A^{-1} =  \begin{pmatrix} \frac{1}{5} & \frac{1}{5} & -\frac{2}{5} \\ 1 & -1 & -1 \\ -\frac{2}{5} & \frac{3}{5} & \frac{4}{5} \end{pmatrix}
```


### Note: IMPORTANT THEOREM

Remember that $A^{-1}A = I$ , matrix multiplication of the matrix $A$ and its inverse $A^{-1}$ = $I$ the Identity matrix. 

```math
A^{-1}A =  \begin{pmatrix} \frac{1}{5} & \frac{1}{5} & -\frac{2}{5} \\ 1 & -1 & -1 \\ -\frac{2}{5} & \frac{3}{5} & \frac{4}{5} \end{pmatrix} \times 
\begin{pmatrix} 1 & 2 & 3 \\ 2 & 0 & 1 \\ -1 & 1 & 2 \end{pmatrix} = I \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
```




### Properties of the Adjugate Matrix

1. **Inverse Calculation**: If $A$ is invertible, then:
   ```math
   A^{-1} = \frac{1}{\det(A)} \text{adj}(A)
   ```
2. **Self-Adjugate Property**: If $A$ is already a diagonal matrix, then $\text{adj}(A)$ will also be diagonal.
3. **Zero Determinant**: If $\det(A) = 0$, the matrix $A$ is not invertible, so $\text{adj}(A)$ cannot be used to find an inverse.

The adjugate is a powerful tool, especially in theoretical linear algebra and matrix computations, helping establish properties related to inverses, determinants, and eigenvalues.



### Reference

- The adjugate matrix and the inverse matrix [The adjugate matrix and the inverse matrix](https://www.macs.hw.ac.uk/~markl/teaching/Inverses.pdf)

- Lesson Name: Adjoint of a Matrix and Inverse of a Matrix [Adjoint and Inverse of a Matrix](https://cdn1.byjus.com/wp-content/uploads/2019/04/Adjoint-and-Inverse-of-a-Matrix.pdf)

- The Engineering Maths First Aid Kit (The inverse of a matrix) : [The inverse of a matrix](https://lcn.people.uic.edu/classes/che205s17/docs/che205s17_reading_05a.pdf)

- Inverse Matrix : [Inverse Matrix](http://www.thphys.nuim.ie/Notes/EE112/09_Inverse_Matrix.pdf)














































