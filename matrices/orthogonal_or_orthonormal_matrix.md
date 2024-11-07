# Orthogonal and Orthonormal Matrices

**Definitions**:
- **Orthogonal Matrix**: A square matrix $Q$ is called an orthogonal matrix if its rows and columns are orthogonal unit vectors. 
Mathematically, $Q$ satisfies:

$`Q^T Q = Q Q^T = I`$

where $`Q^T`$ is the transpose of $Q$, and $I$ is the identity matrix. This means the transpose of $Q$ is also its inverse, i.e., $`Q^{-1} = Q^T`$.


- **Orthonormal Matrix**: An orthogonal matrix is also called orthonormal if its rows and columns are not only orthogonal but also have unit length (norm equals 1). Thus, every orthogonal matrix is also orthonormal by this definition.



























### Orthogonal and Orthonormal Matrices Deep Dive



**2. Properties of Orthogonal Matrices**:
- **Inverse Equals Transpose**: As stated, \( Q^{-1} = Q^T \). This property simplifies many computations, particularly in transformations involving rotations and reflections.
- **Preserves Lengths**: For any vector \( x \), applying an orthogonal matrix \( Q \) preserves its Euclidean norm:
\[
\|Qx\| = \|x\|
\]
This is because:
\[
\|Qx\|^2 = (Qx)^T (Qx) = x^T Q^T Q x = x^T x = \|x\|^2
\]
- **Preserves Angles**: Orthogonal matrices preserve the angles between vectors, maintaining the inner product:
\[
(Qx) \cdot (Qy) = x \cdot y
\]
- **Determinant**: The determinant of an orthogonal matrix \( Q \) is always \( \pm 1 \). If \( \det(Q) = 1 \), the transformation represented by \( Q \) includes rotations without reflection. If \( \det(Q) = -1 \), it includes a reflection.

**3. Examples**:
- **2x2 Rotation Matrix**:
\[
Q = \begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{bmatrix}
\]
This matrix rotates a vector by an angle \( \theta \). It's orthogonal because:
\[
Q^T Q = \begin{bmatrix}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{bmatrix}
\begin{bmatrix}
\cos \theta & -\sin \theta \\
\end{bmatrix} = I
\]

- **2x2 Reflection Matrix**:
\[
Q = \begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
\]
This matrix reflects vectors across the x-axis. It is orthogonal because:
\[
Q^T Q = I
\]
and \( \det(Q) = -1 \), indicating a reflection.

**4. Constructing Orthogonal Matrices**:
To construct an orthogonal matrix, you can use **Gram-Schmidt orthogonalization** to take a set of linearly independent vectors and turn them into an orthonormal set.

**5. Orthogonal Transformations**:
Orthogonal matrices represent transformations such as:
- **Rotations**: Preserve orientation and distances without altering shape.
- **Reflections**: Flip across a line or plane, altering orientation but preserving distance.

These transformations are useful in computer graphics, quantum mechanics, and signal processing.

**6. Verification of Orthogonality**:
To check if a given matrix \( Q \) is orthogonal:
- Verify \( Q^T Q = I \). If this holds, \( Q \) is orthogonal.
- Check that all columns (or rows) are orthonormal vectors:
  - **Orthonormality**: Each vector has unit norm.
  - **Orthogonality**: Dot product between any two distinct vectors is zero.

**7. Orthonormal Basis**:
In an \( n \)-dimensional space, an orthonormal basis is a set of \( n \) orthonormal vectors. A matrix composed of these vectors as its columns is an orthogonal matrix.

**8. Applications**:
- **QR Decomposition**: Decomposes a matrix \( A \) into \( A = QR \), where \( Q \) is orthogonal, and \( R \) is upper triangular.
- **Principal Component Analysis (PCA)**: Uses orthogonal matrices to rotate data and align it with the axes of greatest variance.
- **Signal Processing**: Orthogonal transformations are used for efficient computations in algorithms like the Discrete Fourier Transform (DFT).

Understanding orthogonal and orthonormal matrices is crucial for working with transformations that preserve the structure of data while simplifying computation and analysis.



















### Videos 

17. Orthogonal Matrices and Gram-Schmidt : https://www.youtube.com/watch?v=0MtwqhIwdrI




