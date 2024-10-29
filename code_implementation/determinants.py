import scipy.linalg as la
import numpy as np

A = np.array([[2,4,2,5],
              [1,5,2,6],
              [8,5,3,2],
              [0,1,3,6]])
det = la.det(A)
print(det)

