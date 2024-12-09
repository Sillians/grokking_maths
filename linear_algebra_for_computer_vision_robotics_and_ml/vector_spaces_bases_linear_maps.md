# Vector Spaces, Bases, Linear Maps

## Motivations: Linear Combinations, Linear Independence and Rank
  - Linear combination
  - inner product of two vectors
  - Euclidean norm *(Not in details)
  - Cosine of an angle *(Not in details)
  - multiplication operation on matrices
  - Identity matrix *
  - linear systems
  - Transpose of a matrix *
  - Orthogonal matrices *
  - singular value decomposition * (ridge regression(l2 norm), lasso(l1 norm), PCA)
  - Norm of a matrix *
  - low-rank approximation *
  - Low-rank decomposition *


## Vector Spaces
  - addition and scalar multiplication
  - Associativity of matrices *
  - Identity matrix *
  - Inverse of a matrix *
  - Commutative property of a matrix *
  - Invertible matrices *
  - abelian group
  - Monoid Matrix


## Indexed Families; the Sum Notation $` \sum_{i \in I} a_{i}`$
   - Sequences of vectors
   - indexed families of vectors
   - sequences and sets (An indexed family is a generalization of a sequence, but a multiset is a generalization of a set.)
   - Associative and Commutative binary operation
   - Linear Independence, Subspaces
   - Affine Combinations *
   - Convex combinations *


## Bases of a Vector Space
   - vector space and subspace
   - 


## Matrices
   - Definitions
   - Sum of matrices *
   - scalar multiplication *
   - product of matrices *
   - square matrix *
   - Identity matrix *
   - matrix transpose *
   - inverse matrix *
   - non-singular matrix (invertible matrix) *
   - singular matrix (Not invertible matrix) *
   - Associative property of matrix multiplication


## Linear Maps
   - linear transformation
   - 



























## Monoid Matrix
A **Monoid Matrix** is a conceptual framework that combines ideas from algebraic structures called **monoids** 
with matrices. To understand it, we first break it down:

---

### **Monoids in Algebra**
A **monoid** is an algebraic structure consisting of:
1. A set \(M\).
2. A binary operation (\(\circ\)) that is:
   - **Associative**: For all \(a, b, c \in M\), \((a \circ b) \circ c = a \circ (b \circ c)\).
   - **Has an Identity Element**: There exists \(e \in M\) such that \(e \circ a = a \circ e = a\) for all \(a \in M\).

Example:
- Natural numbers (\(\mathbb{N}\)) with addition (\(+\)) as the operation and \(0\) as the identity.
- Natural numbers (\(\mathbb{N}\)) with multiplication (\(*\)) as the operation and \(1\) as the identity.

---

### **Matrix Form**
A **Monoid Matrix** is a matrix whose entries come from a monoid \(M\), with matrix operations (e.g., addition, multiplication) modified to use the monoid's binary operation instead of standard arithmetic.

#### Characteristics:
1. **Matrix Entries**:
   - Elements of the matrix belong to the monoid \(M\).
   - Operations on the matrix follow the monoid's binary operation.

2. **Matrix Multiplication**:
   If \(A = [a_{ij}]\) and \(B = [b_{ij}]\) are monoid matrices, their product \(C = [c_{ij}]\) is computed as:
   \[
   c_{ij} = \bigoplus_{k} (a_{ik} \circ b_{kj}),
   \]
   where:
   - \(\circ\) is the binary operation of the monoid.
   - \(\oplus\) is typically the monoid's "additive" operation if defined.

#### Identity Matrix:
The identity matrix in this context would have the monoid's identity element (\(e\)) on the diagonal and all other elements as the "zero" of the monoid.

---

### **Applications**
Monoid matrices appear in:
1. **Tropical Algebra**:
   - Entries are real numbers, and operations are defined as:
     - Addition: \(\min\) or \(\max\),
     - Multiplication: Standard addition.
   - Used in optimization and scheduling problems.

2. **Semiring Extensions**:
   - Extends the concept to monoids that are part of a semiring structure.

3. **Graph Theory**:
   - Adjacency matrices with monoid operations to represent paths and weights in graphs.

4. **Automata Theory**:
   - Transition matrices where states and transitions form a monoid.

---

### **Example**

#### Tropical Algebra:
Consider a monoid matrix under tropical operations:
\[
A = 
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}, \quad
B = 
\begin{bmatrix}
4 & 1 \\
2 & 3
\end{bmatrix}.
\]
**Tropical Matrix Multiplication**:
- **Addition**: \(\min(a, b)\),
- **Multiplication**: \(a + b\).

Compute \(C = A \times B\):
\[
c_{ij} = \min_k(a_{ik} + b_{kj}),
\]

For \(c_{11}\):
\[
c_{11} = \min((1+4), (2+2)) = \min(5, 4) = 4.
\]

Continue similarly for other entries.

---

### **Advantages**
- Useful in abstract algebraic studies and specialized computation models.
- Extends classical matrix concepts to new domains like optimization, logic, and formal languages.

The concept of a monoid matrix bridges algebraic structures and computational applications, making it a versatile mathematical tool.



## invertible elements of a monoid M
In a **monoid** \(M\), an element is considered **invertible** if it has a corresponding inverse element that satisfies certain conditions with respect to the monoid's binary operation. Here's a detailed breakdown:

---

### **Definition of Invertible Elements in a Monoid**

A monoid \(M = (M, \circ, e)\) consists of:
- A set \(M\),
- A binary operation \(\circ\) that is **associative**,
- An identity element \(e \in M\) such that \(e \circ a = a \circ e = a\) for all \(a \in M\).

An element \(a \in M\) is **invertible** if there exists an element \(b \in M\) such that:
\[
a \circ b = e \quad \text{and} \quad b \circ a = e,
\]
where \(e\) is the identity element of the monoid.

The element \(b\) is called the **inverse** of \(a\), and it is denoted as \(a^{-1}\).

---

### **Key Properties of Invertible Elements**
1. **Uniqueness of the Inverse**:
   - If \(b\) and \(c\) are inverses of \(a\), then \(b = c\). This follows from the associativity of the operation and the properties of the identity element.

2. **Subset of \(M\)**:
   - The set of all invertible elements in \(M\) forms a **group** under the monoid's operation. This is because:
     - The operation is associative,
     - The identity element \(e\) is its own inverse,
     - The inverse of each invertible element exists and is unique.

---

### **Examples of Invertible Elements**
#### Example 1: Monoid of Integers under Addition
- Monoid: \((\mathbb{Z}, +, 0)\),
- Identity element: \(0\).

In this monoid:
- No element \(a \neq 0\) has an inverse since \(a + b = 0\) only if \(b = -a\), and \(-a \notin \mathbb{Z}^+\) (positive integers). Hence, this is not invertible unless extended into integers.

---

#### Example 2: Monoid of Nonzero Real Numbers under Multiplication
- Monoid: \((\mathbb{R}^*, \times, 1)\),
- Identity element: \(1\).

In this monoid:
- An element \(a \in \mathbb{R}^*\) is invertible if there exists \(b = \frac{1}{a}\), because \(a \times b = 1\).
- Every element in \(\mathbb{R}^*\) is invertible.

---

#### Example 3: Matrix Monoid
- Monoid: \((M_n(\mathbb{R}), \cdot, I)\), where \(M_n(\mathbb{R})\) is the set of all \(n \times n\) matrices with real entries, and \(I\) is the identity matrix.

In this monoid:
- A matrix \(A \in M_n(\mathbb{R})\) is invertible if there exists \(B \in M_n(\mathbb{R})\) such that \(A \cdot B = I\) and \(B \cdot A = I\).
- The invertible matrices form a **group** known as the **general linear group**, denoted as \(GL(n, \mathbb{R})\).

---

### **Non-Invertible Elements in a Monoid**
An element \(a \in M\) that does not have an inverse is called a **non-invertible element** or sometimes a **zero divisor** in certain contexts. 

#### Example:
In the monoid of integers modulo \(n\) under multiplication, \((\mathbb{Z}_n, \cdot, 1)\):
- The element \(a\) is invertible if \(\gcd(a, n) = 1\).
- Otherwise, \(a\) is non-invertible.

---

### **Conclusion**
The set of invertible elements in a monoid is an important subset that forms a **group**. Identifying invertible elements depends on the structure of the monoid and the properties of its binary operation. This concept is crucial in algebraic structures, group theory, and applications in cryptography and matrix theory.



## Abelian Group
An **abelian group** is a type of mathematical group in which the group operation is commutative. It generalizes the concept of addition or multiplication in familiar number systems.

---

### **Definition of an Abelian Group**

A group \(G = (G, \circ)\) is **abelian** if it satisfies the following properties:

1. **Closure**: For all \(a, b \in G\), \(a \circ b \in G\).
2. **Associativity**: For all \(a, b, c \in G\), \((a \circ b) \circ c = a \circ (b \circ c)\).
3. **Identity Element**: There exists an element \(e \in G\) such that \(a \circ e = e \circ a = a\) for all \(a \in G\).
4. **Inverse Element**: For each \(a \in G\), there exists an element \(b \in G\) such that \(a \circ b = b \circ a = e\).
5. **Commutativity**: For all \(a, b \in G\), \(a \circ b = b \circ a\).

---

### **Examples of Abelian Groups**

1. **Integers under Addition**:
   - Group: \((\mathbb{Z}, +)\),
   - Operation: Addition (\(+\)),
   - Identity Element: \(0\),
   - Inverse: For \(a \in \mathbb{Z}\), the inverse is \(-a\).

2. **Real Numbers under Addition**:
   - Group: \((\mathbb{R}, +)\),
   - Identity Element: \(0\),
   - Commutativity holds because \(a + b = b + a\).

3. **Nonzero Real Numbers under Multiplication**:
   - Group: \((\mathbb{R}^*, \cdot)\),
   - Identity Element: \(1\),
   - Inverse: For \(a \neq 0\), the inverse is \(a^{-1} = 1/a\).

4. **Vectors under Addition**:
   - Group: \((\mathbb{R}^n, +)\),
   - Operation: Component-wise addition,
   - Identity Element: \((0, 0, \dots, 0)\),
   - Inverse: For \((a_1, a_2, \dots, a_n)\), the inverse is \((-a_1, -a_2, \dots, -a_n)\).

5. **Cyclic Groups**:
   - Example: \((\mathbb{Z}_n, +)\), the integers modulo \(n\) under addition.

---

### **Non-Abelian vs. Abelian Groups**

- A group is **abelian** if \(a \circ b = b \circ a\) for all elements.
- A group is **non-abelian** if the commutative property does not hold for at least one pair of elements.

#### Example:
The group of \(2 \times 2\) invertible matrices under multiplication is **non-abelian** because matrix multiplication is not commutative.

---

### **Applications of Abelian Groups**

1. **Cryptography**:
   - Abelian groups are used in elliptic curve cryptography and discrete logarithm problems.
   
2. **Number Theory**:
   - Fundamental in studying modular arithmetic, diophantine equations, and primes.

3. **Physics**:
   - Symmetry groups in quantum mechanics and other physical systems are often abelian.

4. **Linear Algebra**:
   - Vector spaces are abelian groups under vector addition.

---

### **Properties of Abelian Groups**

1. The **order** of the elements (smallest \(n\) such that \(a^n = e\)) is well-defined.
2. The direct product of abelian groups is also abelian.
3. Every subgroup of an abelian group is abelian.
4. The group of integers modulo \(n\), \(\mathbb{Z}_n\), is cyclic and hence abelian.

Abelian groups provide a foundational structure in both pure and applied mathematics. They are simple yet powerful tools in abstract algebra and beyond.



## sequences and sets
The statement is insightful and highlights two distinct ways to extend familiar mathematical concepts: sequences and sets. Here's a detailed explanation of the comparisons:

---

### **Indexed Family: A Generalization of a Sequence**
An **indexed family** is a collection of elements indexed by a set, not necessarily by the natural numbers (as in the case of sequences).

#### **Definition**:
An indexed family is represented as:
\[
\{a_i\}_{i \in I},
\]
where:
- \(I\) is the **index set**,
- \(a_i\) is the element corresponding to the index \(i\).

#### **Generalization**:
- A sequence is a special case of an indexed family where \(I = \mathbb{N}\), the set of natural numbers.
- In an indexed family, the index set \(I\) can be any set, finite or infinite.

#### **Examples**:
1. A sequence: \(\{a_n\}_{n \in \mathbb{N}} = a_1, a_2, a_3, \dots\).
2. An indexed family with arbitrary index set: \(\{x_t\}_{t \in T}\), where \(T\) could be any set (e.g., real numbers, integers, or even abstract sets).

---

### **Multiset: A Generalization of a Set**
A **multiset** allows elements to appear more than once, unlike a standard set where elements are unique.

#### **Definition**:
A multiset is represented as:
\[
\{a, a, b, c, c, c\},
\]
where:
- The elements \(a, b, c\) may repeat.
- Each element is associated with a **multiplicity**, indicating how many times it appears.

#### **Generalization**:
- A set is a special case of a multiset where the multiplicity of each element is either 0 or 1.

#### **Examples**:
1. A set: \(\{a, b, c\}\).
2. A multiset: \(\{a, a, b, c, c, c\}\), where \(a\) has multiplicity 2, \(b\) has multiplicity 1, and \(c\) has multiplicity 3.

---

### **Comparison**

| **Property**            | **Indexed Family**                | **Multiset**                         |
|--------------------------|------------------------------------|---------------------------------------|
| **Basic Idea**           | Collection indexed by a set.      | Collection where elements can repeat.|
| **Relation to Sequence** | A sequence is a special case.     | Not directly related to sequences.   |
| **Relation to Set**      | Requires indices, not just elements. | Generalizes sets by allowing repetition. |
| **Structure**            | Defined by index-element pairs.   | Defined by elements and multiplicities. |
| **Use Cases**            | Functions, mappings, ordered collections. | Counting problems, frequency analysis.|

---

### **Key Takeaways**
1. **Indexed Families** extend the concept of sequences by allowing arbitrary index sets, making them powerful for describing parametrized collections.
2. **Multisets** extend the concept of sets by allowing repeated elements, useful in situations where duplication matters.

Both concepts are foundational in mathematics, with distinct roles in algebra, analysis, and combinatorics.



## Linear Independence, Subspaces
### **Linear Independence and Subspaces**

Linear independence and subspaces are fundamental concepts in linear algebra, essential for understanding vector spaces and their structure.

---

### **Linear Independence**
#### **Definition**:
A set of vectors \(\{v_1, v_2, \dots, v_k\}\) in a vector space \(V\) is **linearly independent** if the only solution to the equation:
\[
c_1v_1 + c_2v_2 + \dots + c_kv_k = 0
\]
is:
\[
c_1 = c_2 = \dots = c_k = 0.
\]

#### **Key Properties**:
1. If a set of vectors is **linearly dependent**, at least one vector can be written as a linear combination of the others.
2. Linear independence implies that no vector in the set provides redundant information.

#### **Geometric Interpretation**:
- In \(\mathbb{R}^2\): Two vectors are linearly independent if they are not collinear.
- In \(\mathbb{R}^3\): Three vectors are linearly independent if they do not lie in the same plane.

#### **Example**:
- Vectors \((1, 0)\) and \((0, 1)\) in \(\mathbb{R}^2\) are linearly independent.
- Vectors \((1, 1)\), \((2, 2)\), and \((3, 3)\) are linearly dependent because all are scalar multiples of \((1, 1)\).

---

### **Subspaces**
#### **Definition**:
A **subspace** of a vector space \(V\) is a subset \(W \subseteq V\) that is itself a vector space under the same addition and scalar multiplication operations as \(V\).

#### **Conditions for a Subspace**:
A subset \(W\) of \(V\) is a subspace if:
1. \(W\) contains the **zero vector** (\(0 \in W\)).
2. \(W\) is **closed under addition**: If \(u, v \in W\), then \(u + v \in W\).
3. \(W\) is **closed under scalar multiplication**: If \(v \in W\) and \(c \in \mathbb{R}\), then \(cv \in W\).

#### **Examples**:
1. The set of all vectors of the form \((x, 0)\) in \(\mathbb{R}^2\) is a subspace.
2. The set of all polynomials of degree at most \(n\) is a subspace of the vector space of all polynomials.

#### **Non-Examples**:
- The set of all vectors \((x, y)\) with \(x \geq 0\) in \(\mathbb{R}^2\) is **not** a subspace because it is not closed under scalar multiplication (e.g., \(c(x, y)\) may not satisfy \(x \geq 0\) for \(c < 0\)).

---

### **Connection Between Linear Independence and Subspaces**

1. **Basis**:
   - A **basis** of a subspace is a set of linearly independent vectors that span the subspace.
   - The number of vectors in a basis is the **dimension** of the subspace.

2. **Span**:
   - The **span** of a set of vectors is the smallest subspace containing those vectors.
   - If the vectors are linearly independent, they form a basis for the span.

3. **Linear Independence in Subspaces**:
   - Any linearly independent set in a subspace can be extended to form a basis for the subspace.

---

### **Applications**
- **Linear Independence** is used to solve systems of linear equations, determine the rank of matrices, and identify redundant features in data.
- **Subspaces** are essential for understanding null spaces, column spaces, and eigenspaces in linear algebra.

These concepts form the backbone of many fields, including machine learning, quantum mechanics, and engineering.




## **Bilinear Form in Matrix Context**

A **bilinear form** is a mathematical function that combines two vectors and maps them to a scalar, while being **linear** in each of its arguments. In the context of matrices, bilinear forms can be represented and computed compactly using matrix multiplication.

---

### **Definition of a Bilinear Form**

A bilinear form on a vector space \( V \) over a field (e.g., real numbers \( \mathbb{R} \)) is a function \( B: V \times V \to \mathbb{R} \) such that:

1. **Linearity in the First Argument**:
   \[
   B(\alpha \mathbf{u} + \beta \mathbf{v}, \mathbf{w}) = \alpha B(\mathbf{u}, \mathbf{w}) + \beta B(\mathbf{v}, \mathbf{w}),
   \]
   for all vectors \( \mathbf{u}, \mathbf{v}, \mathbf{w} \in V \) and scalars \( \alpha, \beta \).

2. **Linearity in the Second Argument**:
   \[
   B(\mathbf{u}, \alpha \mathbf{v} + \beta \mathbf{w}) = \alpha B(\mathbf{u}, \mathbf{v}) + \beta B(\mathbf{u}, \mathbf{w}),
   \]
   for all vectors \( \mathbf{u}, \mathbf{v}, \mathbf{w} \in V \) and scalars \( \alpha, \beta \).

---

### **Matrix Representation of Bilinear Forms**

If \( B \) is a bilinear form and \( \mathbf{x}, \mathbf{y} \in \mathbb{R}^n \) are column vectors, then \( B \) can be represented using a square matrix \( A \in \mathbb{R}^{n \times n} \) as:
\[
B(\mathbf{x}, \mathbf{y}) = \mathbf{x}^T A \mathbf{y},
\]
where:
- \( \mathbf{x}^T \) is the transpose of \( \mathbf{x} \),
- \( A \) is the **matrix associated** with the bilinear form,
- \( \mathbf{y} \) is the second vector.

---

### **Special Cases of Bilinear Forms**

1. **Symmetric Bilinear Forms**:
   A bilinear form \( B(\mathbf{x}, \mathbf{y}) \) is symmetric if:
   \[
   B(\mathbf{x}, \mathbf{y}) = B(\mathbf{y}, \mathbf{x}) \quad \text{for all } \mathbf{x}, \mathbf{y}.
   \]
   In matrix terms, this means \( A \) is symmetric (\( A = A^T \)).

2. **Skew-Symmetric Bilinear Forms**:
   A bilinear form \( B(\mathbf{x}, \mathbf{y}) \) is skew-symmetric if:
   \[
   B(\mathbf{x}, \mathbf{y}) = -B(\mathbf{y}, \mathbf{x}) \quad \text{for all } \mathbf{x}, \mathbf{y}.
   \]
   In matrix terms, this means \( A \) is skew-symmetric (\( A^T = -A \)).

3. **Quadratic Form**:
   A **quadratic form** is derived from a bilinear form by setting \( \mathbf{x} = \mathbf{y} \):
   \[
   Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}.
   \]

---

### **Properties of Bilinear Forms**

1. **Linearity**:
   Bilinear forms are linear in both arguments, making them versatile for transformations and projections.

2. **Relation to Inner Products**:
   Symmetric bilinear forms generalize the concept of inner products.

3. **Change of Basis**:
   If \( P \) is a change-of-basis matrix, the bilinear form matrix \( A \) transforms as:
   \[
   A' = P^T A P.
   \]

---

### **Examples**

1. **Standard Dot Product**:
   The dot product in \( \mathbb{R}^n \) is a bilinear form where \( A = I \) (the identity matrix):
   \[
   B(\mathbf{x}, \mathbf{y}) = \mathbf{x}^T I \mathbf{y} = \mathbf{x} \cdot \mathbf{y}.
   \]

2. **Energy in Physics**:
   The energy \( E = \frac{1}{2} \mathbf{x}^T K \mathbf{x} \) (where \( K \) is the stiffness matrix) is a quadratic form derived from a bilinear form.

---

### **Applications**

1. **Geometry**:
   Bilinear forms describe distances, angles, and areas.

2. **Physics**:
   Used in mechanics, elasticity, and electromagnetism.

3. **Machine Learning**:
   Kernel functions in support vector machines can involve bilinear forms.

4. **Linear Algebra**:
   Bilinear forms appear in eigenvalue problems and matrix factorization.

Bilinear forms unify geometric and algebraic properties, enabling powerful tools for problem-solving in multiple domains.


























































