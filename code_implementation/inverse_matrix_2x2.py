# Code implementation to get the inverse matrix of a 2x2 matrix.

from typing import List

def get_inverse_matrix_2x2(matrix: List[list]) -> list:
    # case for a 2x2 matrix
    assert len(matrix) == 2, "Matrix must be a 2x2 matrix."
    # Extracting elements from the matrix
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    # Calculating the determinant
    determinant = a * d - b * c

    # Checking if the matrix is invertible
    if determinant == 0:
        raise ValueError("Matrix is not invertible (determinant is zero).")

    # Calculating the inverse
    inverse_matrix = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant]
    ]

    return inverse_matrix


def get_inverse_matrix2(matrix: List[list]) -> list:
    assert len(matrix) == 2, "Matrix must be a 2x2 matrix."
    # Extracting elements from the matrix
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    # Calculating the determinant
    determinant = a * d - b * c

    # Checking if the matrix is invertible
    if determinant == 0:
        raise ValueError("Matrix is not invertible (determinant is zero).")

    inverse_det = 1 / determinant
    alt_matrix = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    matrix_mul = int(inverse_det) * (alt_matrix)
    return matrix_mul



matrix = [[1, 1],
          [1, 2]]

new_matrix_3x3 = [[1, 1, 2],
                  [1, 2, 3],
                  [1, 2, 3]]


print(get_inverse_matrix_2x2(matrix))
print(get_inverse_matrix2(matrix))

try:
    inv_matrix = get_inverse_matrix_2x2(matrix)
    print("Inverse of the matrix is:")
    for row in inv_matrix:
        print(row)
except ValueError as e:
    print(e)

# Will fail
# print(get_inverse_matrix_2x2(new_matrix_3x3))
