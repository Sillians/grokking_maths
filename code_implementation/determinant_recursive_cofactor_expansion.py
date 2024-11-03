# Implementation using the Laplace Expansion (Cofactor Expansion)
# Time Complexity: This recursive approach has a time complexity of 𝑂(𝑁!), which grows factorially with the matrix size, making it inefficient for large matrices.

from typing import List

# Approach 1
def get_minor(matrix, row: int, col: int) -> List[list]:
    """
        Returns the minor matrix after removing the specified row and column.

        Parameters:
            matrix (list of lists): The original matrix.
            row (int): The row to remove.
            col (int): The column to remove.

        Returns:
            list of lists: The minor matrix.
        """

    return [ [matrix[i][j] for j in range(len(matrix)) if j != col]
             for i in range(len(matrix)) if i != row ]


def determinant(matrix: List[list]) -> float:
    """
        Calculates the determinant of an NxN matrix using recursive cofactor expansion.

        Parameters:
            matrix (list of lists): The matrix for which to compute the determinant.

        Returns:
            float: The determinant of the matrix.

        Raises:
        ValueError: If the input matrix is not square (NxN).
    """
    # Check if the matrix is square
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("The matrix must be square (NxN) to calculate the determinant.")

    # Base case for 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]

    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0 # Initialize determinant
    for col in range(len(matrix[0])):
        # Get the minor matrix by removing the first row and the current column
        minor = get_minor(matrix, 0, col)

        # calculate the cofactor
        cofactor = ((-1) ** col) * matrix[0][col] * determinant(minor)

        # Add or subtract the cofactor to the determinant
        det += cofactor

    return det


## Approach 2
def get_determinant(matrix: List[list]):
    """Recursively calculate the determinant of an n x n matrix."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)
    return det


## Approach 3
def determinant_value(M: List[list]) -> float:
    # Base case of recursive function: 1x1 matrix
    if len(M) == 1:
        return M[0][0]

    # Base case of recursive function: 2x2 matrix
    if len(M) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]

    total = 0
    for column, element in enumerate(M[0]):
        # Exclude first row and current column.
        K = [x[:column] + x[column + 1 :] for x in M[1:]]
        s = 1 if column % 2 == 0 else -1
        total += s * element * determinant(K)
    return total



matrix = [
    [1, 2, 3, 5],
    [4, 5, 6, 3],
    [7, 8, 9, 2],
    [10, 11, 7, 12]
]

A = [[1, 2, -1],
     [-2, 0, 1],
     [1, -1, 0]]

print("Determinant:", determinant(A))



q = [[2, 3, 4],
     [5, 3, 8]]



print(determinant_value(matrix))