import scipy as sp
import numpy as np

A = np.array([[1, 2, 3],
              [0, 1, 2],
              [2, 0, 0]])

B = np.array([1, 1, 0]).reshape(-1, 1)


def solve_lin_system(A, B):
    return sp.linalg.solve(A, B)

print("A = \n{}".format(A))
print("B = \n{}".format(B))
print("Solution:")
print('X.T = {}'.format(*solve_lin_system(A, B).T))
print()
w = int(input("Enter A matrix width"))
h = int(input("Enter A matrix height"))
print("Enter A matrix rowwise entries one by one:")
A = [[int(input()) for x in range (w)] for y in range(h)]
print("A = \n{}".format(A))

print("Enter B vector entries one by one:")
B = np.reshape([int(input()) for x in range (h)], (-1, 1))
print("B = \n{}".format(B))
print("Solution:")
print('X.T = {}'.format(*solve_lin_system(A, B).T))
