import numpy as np


def generate_full_rank_matrix(n):
    while True:
        matrix = np.random.randint(low=1, high=20, size=(n, n))
        if np.linalg.matrix_rank(matrix) == n:
            return matrix


def is_identity_matrix(matrix):
    identity_matrix = np.eye(matrix.shape[0])
    return np.array_equal(matrix, identity_matrix)


def add_rows(matrix, i, j, number):
    matrix[j] += matrix[i] * number


def swap_rows(matrix, i, j):
    matrix[[i, j], :] = matrix[[j, i], :]


if __name__ == "__main__":
    print(type(generate_full_rank_matrix(5)))
