"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page 120 in chapter 9
"""
from randomized_quicksort import partition, randomized_partition

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q-1, i)
    else:
        return randomized_select(A, q+1, r, i-k)

if __name__ == '__main__':
    A = [6, 10, 13, 5, 8, 3, 2, 11]
    print(randomized_select(A, 0, 7, 5))