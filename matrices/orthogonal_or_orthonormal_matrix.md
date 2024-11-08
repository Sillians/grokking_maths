# Orthogonal and Orthonormal Matrices

## Orthogonal matrices

### **DEFINITIONS**:

- **Orthogonal Matrix**: A square matrix $Q$ is called an orthogonal matrix if its rows and columns are orthogonal unit vectors. 
This means each column vector in the matrix is orthogonal (perpendicular) to every other column vector and has a unit length (magnitude of 1). 
Mathematically, $Q$ satisfies:

$`Q^T Q = Q Q^T = I`$

where $`Q^T`$ is the transpose of $Q$, and $I$ is the identity matrix. This means the transpose of $Q$ is also its inverse, i.e., $`Q^{-1} = Q^T`$.

- **Orthogonal Matrix**: We say that $2$ vectors are orthogonal if they are perpendicular to each other. i.e. the dot product of the two vectors is zero.

- **Orthogonal Matrix**: We say that a set of vectors {$`\vec{v}_1, \vec{v}_2, \dots, \vec{v}_n`$} are mutually orthogonal if every pair of vectors is orthogonal. i.e.

$`\vec{v}_i . \vec{v}_j = 0`$, for all $`i \neq j`$

### Example

The set of vectors $`\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix} 1 \\ \sqrt{2} \\ 1 \end{pmatrix}, \quad \mathbf{v}_3 = \begin{pmatrix} 1 \\ -\sqrt{2} \\ 1 \end{pmatrix}`$ is mutually orthogonal

To confirm orthogonality, each pairwise dot product of these vectors should equal zero.

### Step 1: Calculate $`\mathbf{v}_1 \cdot \mathbf{v}_2`$

$`\mathbf{v}_1 \cdot \mathbf{v}_2 = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ \sqrt{2} \\ 1 \end{pmatrix} = (1)(1) + (0)(\sqrt{2}) + (-1)(1) = 1 + 0 - 1 = 0`$

### Step 2: Calculate $`\mathbf{v}_1 \cdot \mathbf{v}_3`$

$`\mathbf{v}_1 \cdot \mathbf{v}_3 = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ -\sqrt{2} \\ 1 \end{pmatrix} = (1)(1) + (0)(-\sqrt{2}) + (-1)(1) = 1 + 0 - 1 = 0`$

### Step 3: Calculate $`\mathbf{v}_2 \cdot \mathbf{v}_3`$

$`\mathbf{v}_2 \cdot \mathbf{v}_3 = \begin{pmatrix} 1 \\ \sqrt{2} \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ -\sqrt{2} \\ 1 \end{pmatrix} = (1)(1) + (\sqrt{2})(-\sqrt{2}) + (1)(1) = 1 - 2 + 1 = 0`$


Since all pairwise dot products are zero, we can conclude that $`\mathbf{v}_1`$, $`\mathbf{v}_2`$, and $`\mathbf{v}_3`$ are indeed mutually orthogonal.


## Orthonormal matrix and vectors

- We say a set of vectors $S$ is orthonormal if every vector in $S$ has magnitude $1$ and the set of vectors are mutually orthogonal. 

To say that vectors $`\mathbf{q}_1, \mathbf{q}_2, \ldots, \mathbf{q}_n`$ are **orthonormal** means that:

1. **Each vector has a length (or norm) of 1**: 
   $`\mathbf{q}_i^T \mathbf{q}_i = 1 \quad \text{for each } i`$ , This property indicates that each vector is **normalized**.

2. **Each pair of vectors is orthogonal** (perpendicular to each other):
   $`\mathbf{q}_i^T \mathbf{q}_j = 0 \quad \text{if } i \neq j`$ , This orthogonality ensures that each vector is directionally independent from the others.

Together, these properties make the set **orthonormal**. In other words, each vector points in a unique direction and has unit length.

### Why Orthonormal Vectors are Linearly Independent
Orthonormal vectors are always linearly independent because no vector in the set can be written as a combination of the others. 
This follows from the fact that they are mutually perpendicular; each vector contributes a unique, non-overlapping component in its respective direction.


Let's break down the process of converting the given mutually orthogonal vectors $`\mathbf{v}_1`$, $`\mathbf{v}_2`$, and $`\mathbf{v}_3`$ into an orthonormal set by normalizing each vector. 
This means we’ll adjust each vector to have a magnitude (or norm) of $1$.

Given the vectors:

$`\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix} 1 \\ \sqrt{2} \\ 1 \end{pmatrix}, \quad \mathbf{v}_3 = \begin{pmatrix} 1 \\ -\sqrt{2} \\ 1 \end{pmatrix}`$

we'll compute the normalized form of each.

### Step 1: Normalizing $`\mathbf{v}_1`$
1. Calculate the magnitude of $`\mathbf{v}_1`$:
   $`|\mathbf{v}_1| = \sqrt{1^2 + 0^2 + (-1)^2} = \sqrt{1 + 0 + 1} = \sqrt{2}`$

2. Divide each component of $`\mathbf{v}_1`$ by $`|\mathbf{v}_1|`$:

   $`\mathbf{u}_1 = \frac{\mathbf{v}_1}{|\mathbf{v}_1|} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \\ -\frac{1}{\sqrt{2}} \end{pmatrix}`$


### Step 2: Normalizing $`\mathbf{v}_2`$
1. Calculate the magnitude of $`\mathbf{v}_2`$:

   $`|\mathbf{v}_2| = \sqrt{1^2 + (\sqrt{2})^2 + 1^2} = \sqrt{1 + 2 + 1} = \sqrt{4} = 2`$


2. Divide each component of $`\mathbf{v}_2`$ by $`|\mathbf{v}_2|`$:

   $`\mathbf{u}_2 = \frac{\mathbf{v}_2}{|\mathbf{v}_2|} = \frac{1}{2} \begin{pmatrix} 1 \\ \sqrt{2} \\ 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} \\ \frac{\sqrt{2}}{2} \\ \frac{1}{2} \end{pmatrix}`$


### Step 3: Normalizing $`\mathbf{v}_3`$
1. Calculate the magnitude of $`\mathbf{v}_3`$:
   
  $`|\mathbf{v}_3| = \sqrt{1^2 + (-\sqrt{2})^2 + 1^2} = \sqrt{1 + 2 + 1} = \sqrt{4} = 2`$

2. Divide each component of $`\mathbf{v}_3`$ by $`|\mathbf{v}_3|`$:

    $`\mathbf{u}_3 = \frac{\mathbf{v}_3}{|\mathbf{v}_3|} = \frac{1}{2} \begin{pmatrix} 1 \\ -\sqrt{2} \\ 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} \\ -\frac{\sqrt{2}}{2} \\ \frac{1}{2} \end{pmatrix}`$

### Final Orthonormal Set
The set of vectors $`\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}`$ is orthonormal:

$`\mathbf{u}_1 = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \\ -\frac{1}{\sqrt{2}} \end{pmatrix}, \quad \mathbf{u}_2 = \begin{pmatrix} \frac{1}{2} \\ \frac{\sqrt{2}}{2} \\ \frac{1}{2} \end{pmatrix}, \quad \mathbf{u}_3 = \begin{pmatrix} \frac{1}{2} \\ -\frac{\sqrt{2}}{2} \\ \frac{1}{2} \end{pmatrix}`$

### Proposition: Orthogonal Sets and Linear Independence
An orthogonal set of non-zero vectors is linearly independent because no vector in the set can be expressed as a linear combination 
of the others due to their orthogonal nature. Therefore, the orthonormal set $`\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}`$ is also linearly independent.



- **Orthonormal Matrix**: An orthogonal matrix is also called orthonormal if its rows and columns are not only orthogonal but also have unit length (norm equals 1). 
Thus, every orthogonal matrix is also orthonormal by this definition.

An **orthonormal matrix** $Q$ is a matrix where each column vector is orthonormal, meaning each column has a unit length `(norm = 1)` and is 
perpendicular (orthogonal) to the others. This type of matrix has some special properties:


1. **Identity Matrix from $`Q^T Q`$:** If $Q$ has orthonormal columns, then $`Q^T Q = I`$, where $I$ is the identity matrix. 
This is due to the dot product properties of orthonormal vectors.


2. **Orthogonal Matrix:** If $Q$ is a square orthonormal matrix (same number of rows and columns), it’s called an **orthogonal matrix**. For orthogonal matrices:
   - $`Q^T = Q^{-1}`$, which means the transpose of $Q$ is also its inverse.
   - $`Q Q^T = I`$ and $`Q^T Q = I`$.

    For example, if  $`Q = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}`$
    then $`Q^{T} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}`$.

    Both $Q$ and $`Q^{T}`$ are orthogonal matrices, and their product is the identity.


3. **Examples of Orthogonal Matrices:**
   - **Rotation matrices** like:
   
      $`Q = \begin{pmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{pmatrix}`$
   
    This matrix represents a rotation by an angle $\theta$ and is orthogonal because it preserves the lengths of vectors and maintains orthogonality.

   - **Hadamard matrices** (common in signal processing) are square orthogonal matrices that don’t involve complex numbers or roots, such as:
     
      $`Q = \frac{1}{2} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & -1 & 1 \end{pmatrix}`$


4. **Rectangular Orthonormal Matrices:** Non-square matrices can also have orthonormal columns, like:

    $`Q = \frac{1}{3} \begin{pmatrix} 1 & -2 \\ 2 & -1 \\ 2 & 2 \end{pmatrix}`$


   In this case, $`Q^T Q = I`$ still holds, but $`Q Q^T`$ does not yield the identity matrix due to its non-square shape.

Orthogonal matrices are significant in linear algebra because they maintain vector lengths and angles, making them useful in applications 
like signal processing, transformations, and solving systems of equations.


### Orthonormal columns are good

Orthonormal columns simplify matrix operations significantly. Here’s why they’re advantageous and how they relate to projection matrices:

1. **Projection Matrix with Orthonormal Columns:** If a matrix $Q$ has orthonormal columns, then the projection matrix $P$ onto the column space of $Q$ is given by:
   $`P = Q Q^T`$

   Here’s why this works:
   - In general, the projection matrix is defined as $`P = Q^T (Q^T Q)^{-1} Q^T`$.
   - When $Q$ has orthonormal columns, $`Q^T Q = I`$, so $`(Q^T Q)^{-1} = I`$. Thus, $P$ simplifies to $`Q Q^T`$.

2. **Special Case with Square Orthonormal Matrices:** If $Q$ is a square matrix with orthonormal columns (making it an orthogonal matrix), 
    $`P = Q Q^T = I`$. This indicates that $Q$’s columns span the entire space, so projecting onto $Q$’s column space covers the whole space, 
    making $P$ effectively the identity matrix.

3. **Simplified Calculations for Projections:** In an orthonormal basis, projecting any vector $`\mathbf{b}`$ onto the basis vector $`\mathbf{q}_i`$ 
becomes straightforward. The projection component $`\hat{x}_i`$ onto $`\mathbf{q}_i`$ is simply the dot product:
   
   $`\hat{x}_i = \mathbf{q}_i^T \mathbf{b}`$
   
   This avoids more complex calculations because:
   - Normally, for a projection onto a non-orthonormal basis, we would need to solve $`A^T A \hat{x} = A^T b`$.
   - With orthonormal columns, this simplifies to $`\hat{x} = Q^T b`$.

Orthonormal columns make the math behind projections, transformations, and decompositions simpler and more computationally efficient, 
especially in solving systems and optimizing algorithms in applications like machine learning and signal processing.



## Gram-Schmidt Process

The Gram-Schmidt process is a method for converting a set of independent vectors into an orthonormal set that spans the same space.
With elimination, our goal was "make the matrix triangular". Now out goal is "make the matrix orthogonal".

### Steps of the Gram-Schmidt Process

1. **Start with Independent Vectors**: Given vectors $a$ and $b$ (or more if in higher dimensions), 
we want to generate orthonormal vectors $q_1$ and $q_2$ that span the same plane or space.

2. **Orthogonalize the First Vector**: 
   - We start by finding orthogonal vectors $A$ and $B$ that span the same space as $a$ and $b$. 
   - Then the unit vectors $`q_1 = \frac{A}{\| A \|}`$ and $`q_2 = \frac{B}{\| B \|}`$ from the desired orthonormal basis.
   
   - Set $A = a$.
   - This means that $`q_1 = \frac{A}{\| A \|}`$ will be our first unit vector in the desired orthonormal basis.

3. **Project the Second Vector**:
   - We need to find a vector $B$ that is orthogonal to $A$ in the space spanned by $a$ and $b$ by projecting $b$ onto $a$ and letting $`B = b - p`$. 
   - This can be done by removing the component of $b$ that aligns with $A$.
   - Calculate the projection of $b$ onto $A$: 
   
     $`\text{proj}_A(b) = \frac{A^T b}{A^T A} A`$
   
   - Subtract this projection from $b$ to get $B$, which is orthogonal to $A$: 
   
     $`B = b - \text{proj}_A(b) = b - \frac{A^T b}{A^T A} A`$
   
   - Normalize $B$ to get the unit vector $`q_2 = \frac{B}{\| B \|}`$.

4. **Orthogonalize Additional Vectors**:
   - What if we had started with three independent vectors, $a$, $b$ and $c$? Then we'd find a vector $C$ orthogonal to both $A$ and $B$ by subtracting
   from $c$ it components in $A$ and $B$ directions:

     $`C = c - \frac{A^T c}{A^T A} A - \frac{B^T c}{B^T B} B`$
   
   - Normalize $C$ to get $`q_3 = \frac{C}{\| C \|}`$, and repeat for additional vectors if necessary.


### **Example:**

Find the orthonormal basis for the vectors $`a = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}`$ and $`b = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}`$
using the Gram-Schmidt process.

### Step-by-Step Solution

1. **Start with Vector $A = a$**:
   - We take $A = a$ as our first vector, so $q_1$ will be the unit vector in the direction of $A$.

2. **Calculate $B$ by Removing the Projection of $b$ on $a$ **:
   - We want $B$ to be orthogonal to $A$, so we project $b$ onto $a$ and subtract:
     $`B = b - \frac{A^T b}{A^T A} A`$
   
   - Calculate the projection factor:
   
     $`A^T b = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} = 1 \cdot 1 + 1 \cdot 0 + 1 \cdot 2 = 3`$
     
     $`A^T A = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = 1 + 1 + 1 = 3`$
   
   - So the projection of $b$ onto $a$ is:
     
     $`\frac{A^T b}{A^T A} A = \frac{3}{3} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}`$
   
   - Subtract this projection from $b$ to get $B$:
     
     $`B = b - \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} - \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ -1 \\ 1 \end{bmatrix}`$

3. **Normalize $A$ and $B$ to Get $q_1$ and $q_2$**:
   - Normalize $A$ to get $q_1$:
   
     $`q_1 = \frac{A}{\| A \|} = \frac{1}{\sqrt{3}} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}} \end{bmatrix}`$
   
   - Normalize $B$ to get $q_2$:
   
     $`q_2 = \frac{B}{\| B \|} = \frac{1}{\sqrt{2}} \begin{bmatrix} 0 \\ -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix}`$

4. **Form the Matrix $Q$**:
   - Combine $q_1$ and $q_2$ to form $Q$:
   
     $`Q = \begin{bmatrix} q_1 & q_2 \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{3}} & 0 \\ \frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{2}} \end{bmatrix}`$
      
      The column space of $Q$ is the plane spanned by $a$ and $b$.
   
5. **Matrix $R$**:
   - When we studied elimination, we wrote the process in terms of matrices and found $`A = LU`$. A similar equation $`A= QR`$ relates our starting matrix 
     $A$ to the result $Q$ of the Gram-Schmidt process. Where $L$ was lower triangular, $R$ is upper triangular.
   - Suppose we have a matrix $`A = \begin{bmatrix} a_1 & a_2 \end{bmatrix}`$, where $a_1$ and $a_2$ are column vectors.

   **Properties of $Q$ and $R$**:
   - The decomposition $`A = QR`$ implies that $`Q^T Q = I`$, so $`R = Q^T A`$. 
     This shows that the transformation preserves the geometry of the column space of $A$ while giving an orthonormal basis for that space in $Q$
     and expressing the scaling/projection information in $R$.
 
   - The matrix $R$ can be obtained as $`R = Q^T A`$, where $A$ is the original matrix formed by vectors $a$ and $b$.

### Summary
- The orthonormal basis for the space spanned by $a$ and $b$ is given by the columns of $Q$:

  $`q_1 = \begin{bmatrix} \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}} \end{bmatrix}, \quad q_2 = \begin{bmatrix} 0 \\ -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix}`$

This basis allows for projections or further matrix operations in the same subspace defined by $a$ and $b$.


### Summary
The Gram-Schmidt process turns $A$ into a product of an orthonormal matrix $Q$ and an upper triangular matrix $R$, where $Q$ 
contains orthonormal columns, and $`R = Q^T A`$. The orthogonality conditions ensure $R$ is upper triangular and makes the decomposition 
ideal for simplifying various matrix operations, especially in projections and linear transformations.




### Reference

- Orthogonal matrices and Gram-Schmidt: [Orthogonal matrices and Gram-Schmidt](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/7ac32be444c25e48590f47573833ccc6_MIT18_06SCF11_Ses2.4sum.pdf)

- 6.3 Orthogonal and orthonormal vectors: [6.3 Orthogonal and orthonormal vectors](https://www.ucl.ac.uk/~ucahmdl/LessonPlans/Lesson10.pdf)

- Lecture 12: Orthonormal Matrices: [Orthogonal Matrices](https://ocw.mit.edu/courses/res-18-011-algebra-i-student-notes-fall-2021/mit18_701f21_lect12.pdf)

- Orthogonal Matrices and Matrix Norms Lecture # 3: [Orthogonal Matrices and Matrix Norms](https://www.cse.psu.edu/~b58/cse456/lecture3.pdf)



### Videos 

- `17. Orthogonal Matrices and Gram-Schmidt (MIT OpenCourseWare)`

[![IMAGE ALT TEXT](http://img.youtube.com/vi/0MtwqhIwdrI/0.jpg)](http://www.youtube.com/watch?v=0MtwqhIwdrI "17. Orthogonal Matrices and Gram-Schmidt")


- `Orthogonality and Orthonormality`

[![IMAGE ALT TEXT](http://img.youtube.com/vi/6nqMegdbxik/0.jpg)](http://www.youtube.com/watch?v=6nqMegdbxik "Orthogonality and Orthonormality:")


- `The Gram-Schmidt Process`

[![IMAGE ALT TEXT](http://img.youtube.com/vi/zHbfZWZJTGc/0.jpg)](http://www.youtube.com/watch?v=zHbfZWZJTGc "The Gram-Schmidt Process")


- `Orthogonal Matrices`

[![IMAGE ALT TEXT](http://img.youtube.com/vi/JfqZdTVsvso/0.jpg)](http://www.youtube.com/watch?v=JfqZdTVsvso "Orthogonal Matrices")


- `Orthogonal Matrices and their Properties | Linear Algebra`

[![IMAGE ALT TEXT](http://img.youtube.com/vi/wGgg2ywmNIA/0.jpg)](http://www.youtube.com/watch?v=wGgg2ywmNIA "Orthogonal Matrices and their Properties | Linear Algebra")































