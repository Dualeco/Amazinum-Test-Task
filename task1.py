import scipy as sp
import numpy as np

A = np.array([[1, 2, 3],
              [0, 1, 2],
              [2, 0, 0]])

B = np.array([1, 1, 0]).reshape(-1, 1)


def solve_lin_system(A, B):
    return sp.linalg.solve(A, B)


print('X.T = {}'.format(*solve_lin_system(A, B).T))