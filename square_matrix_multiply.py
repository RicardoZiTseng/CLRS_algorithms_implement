"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page: page 43 in chapter 4
"""
from numpy import matrix
from numpy import zeros
def matrix_multiply(A,B):
    A_row = A.shape[0]
    A_col = A.shape[1]
    B_row = B.shape[0]
    B_col = B.shape[1]
    if A_col != B_row:
        print("the dimension of A and B do nit match!")
    else:
        C = zeros(shape = (A_row, B_col))
        for i in range(A_row):
            for j in range(B_col):
                C[i, j] = 0
                for k in range(A_col):
                    C[i, j] = C[i, j] + A[i, k] * B[k, j]
        return C

A = matrix('1 0 0; 0 1 0; 0 0 1; 1 2 3')
B = matrix('0 0 1 1; 0 1 0 2; 1 0 0 3')
print(matrix_multiply(A, B))