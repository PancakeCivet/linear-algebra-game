import numpy as np


def generate_full_rank_matrix(n):
    while True:
        matrix = np.random.randint(low=1, high=20, size=(n, n))  # 生成一个n阶随机整数矩阵
        if np.linalg.matrix_rank(matrix) == n:  # 判断矩阵的秩是否为n
            return matrix
