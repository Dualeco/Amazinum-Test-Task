import time

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def count_neighbors(x, y, matrix):
    num_rows = matrix.shape[0]
    num_cols = matrix.shape[1]

    count = 0

    range_x = range((0 if x - 1 < 0 else x - 1), (num_rows if x + 2 > num_rows else x + 2), 1)
    range_y = range((0 if y - 1 < 0 else y - 1), (num_cols if y + 2 > num_cols else y + 2), 1)

    for i in range_x:
        for j in range_y:
            if not (i == x and j == y) and matrix[i][j] == 1:
                count += 1

    return count


def should_cell_live(alive_now, num_neighbors):
    if alive_now:
        if num_neighbors == 2 or num_neighbors == 3:
            return True
        else:
            return False
    else:
        if num_neighbors == 3:
            return True
        else:
            return False


def run_iteration(matrix):
    new_matrix = np.zeros_like(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            num_neighbors = count_neighbors(i, j, matrix)
            live = should_cell_live(matrix[i][j], num_neighbors)
            new_matrix[i][j] = live

    return new_matrix

def get_nth_iteration(matrix, n=1):
    for it in range(n):
        matrix = run_iteration(matrix)
        print(it)
        print(matrix)

    return matrix

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def next(self):
        self.matrix = run_iteration(self.matrix)

state = np.array([[1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 1, 1],
                  [1, 0, 0, 1, 0, 0, 1],
                  [0, 1, 1, 0, 1, 1, 0],
                  [1, 1, 1, 1, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 0, 1, 1, 0, 1]])
print("Initial state:")
print(state)
seventh_it = get_nth_iteration(state, 7)
print("7th iteration:")
print(seventh_it)


print("Generate custom matrix:")
w = int(input("Enter generated matrix width"))
h = int(input("Enter generated matrix height"))

def generate_matrix(size):
    return np.random.randint(2, size=(w, h))

def run_infinitely(matrix):
    while True:
        time.sleep(1)
        new_matrix = run_iteration(matrix)
        plot_matrix(new_matrix)
        if np.array_equal(matrix, new_matrix):
            break
        else:
            matrix = new_matrix

print("Animate played in popup:")

m_obj = Matrix(generate_matrix((w, h)))

fig, ax = plt.subplots()

def plot_matrix(i):
    old = m_obj.matrix
    m_obj.next()
    if not np.array_equal(old, m_obj.matrix):
        ax.imshow(m_obj.matrix)
        ax.set_axis_off()

# In Pycharm pls enable to show plots in a popup window
anim = FuncAnimation(fig, plot_matrix, interval=500, save_count=250)
plt.show()