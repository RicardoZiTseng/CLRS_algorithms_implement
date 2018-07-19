"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page: page 95 in chapter 7
"""
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

if __name__ == '__main__':
    array = [2, 8, 7, 1, 3, 5, 6, 4]
    idx = partition(array, 0, 7)
    print("after the first partition, the array A is:")
    print(array)

    array = [2, 8, 7, 1, 3, 5, 6, 4]
    quick_sort(array, 0, 7)
    print("the quick sort result of the array A is:")
    print(array) 