"""
author: Ricardo
pages of CLRS: chinese page: page 84 in chapter 6

"""

def parent(i):
    """
    return the index of the i's parent
    """
    return i // 2

def left(i):
    """
    return the i's left brother's index
    """
    return 2*i

def right(i):
    """
    return the i's right brother's index
    """
    return 2*i + 1

def heapsize(A):
    return len(A) - 1

def max_heapify(A, i):
    """
    keep the nature of heap structure
    """
    l = left(i)
    r = right(i)
    largest = 0
    if l <= heapsize(A) and A[l] >= A[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize(A) and A[r] >= A[i]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
    return A

def max_heapify_quick(A, i):
    count = len(A)
    largest = count
    while i != largest:
        if l <= heapsize(A) and A[l] >= A[i]:
            largest = l
        else:
            largest = i
        if r <= heapsize(A) and A[r] >= A[i]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            i, largest = largest, count
    return A