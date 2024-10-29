# Implementation using the Laplace Expansion (Cofactor Expansion)

from typing import List

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
    """
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



matrix = [
    [1, 2, 3, 5],
    [4, 5, 6, 3],
    [7, 8, 9, 2],
    [10, 11, 7, 12]
]
print("Determinant:", determinant(matrix))