from typing import List

def matrixTranspose(matrix: List[list]) -> List[list]:
    # Transpose of a matrix
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def get_minor(matrix, row: int, col: int) -> List[list]:
    # Returns the minor matrix after removing the specified row and column.
    return [ [matrix[i][j] for j in range(len(matrix)) if j != col]
             for i in range(len(matrix)) if i != row ]

def matrixDeterminant(matrix: List[list]) -> float:
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    # Determinant for a 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for column, element in enumerate(matrix[0]):
        # Exclude first row and current column.
        K = [x[:column] + x[column + 1:] for x in matrix[1:]]
        determinant += ((-1) ** column) * element * matrixDeterminant(K)
    return determinant


def matrixInverse(matrix: List[list]) -> List[list]:
    determinant = matrixDeterminant(matrix)
    if determinant == 0:
        raise ValueError("The matrix is singular and cannot be inverted.")

    # case for 2x2 matrix
    if len(matrix) == 2:
        d, a = matrix[0][0], matrix[1][1]
        b, c = -(matrix[0][1]), -(matrix[1][0])
        return [[a/determinant, b/determinant],
                    c/determinant, d/determinant]

    # find matrix of cofactors
    cofactors = []
    for row in range(len(matrix)):
        cofactorRow = []
        for col in range(len(matrix)):
            # get the minor matrix
            minor = get_minor(matrix, row, col)
            # calculate the cofactor with correct sign
            cofactorRow.append(((-1)**(row+col)) * matrixDeterminant(minor))
        cofactors.append(cofactorRow)
    cofactors = matrixTranspose(cofactors)
    for row in range(len(cofactors)):
        for col in range(len(cofactors)):
            cofactors[row][col] = cofactors[row][col]/determinant
    return cofactors



A = [[1, 2, -1],
     [-2, 0, 1],
     [1, -1, 0]]

matrix = [[1, 1],
          [1, 2]]

matrix_3x3 = [[1, 2, 3],
              [2, 0, 1],
              [-1, 1, 2]]

matrix4x4 = [
    [1, 2, 3, 5],
    [4, 5, 6, 3],
    [7, 8, 9, 2],
    [10, 11, 7, 12]
]

print(matrixInverse(matrix))
print(matrixInverse(matrix_3x3))
print(matrixInverse(matrix4x4))