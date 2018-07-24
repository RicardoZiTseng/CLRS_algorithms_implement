"""
author: Ricardo
pages of CLRS: chinese page: page 84 in chapter 6

"""

MIN_MUM = -0XFFFFFFFF

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

def max_heapify(A, heap_size, i):
    """
    keep the nature of heap structure
    """
    l = left(i)
    r = right(i)
    largest = 0
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, heap_size, largest)

def max_heapify_quick(A, heap_size, i):
    count = len(A)
    largest = count
    l = left(i)
    r = right(i)
    while i != largest:
        if l <= heap_size and A[l] >= A[i]:
            largest = l
        else:
            largest = i
        if r <= heap_size and A[r] >= A[i]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            i, largest = largest, count

def build_max_heap(A):
    heap_size = len(A) - 1
    for i in range(heap_size//2, 0, -1):
        max_heapify(A, heap_size, i)

def test_build_max_heap(A):
    build_max_heap(A)
    print(A)

def heapsort(A):
    build_max_heap(A)
    heap_size = len(A) - 1
    for i in range(len(A)-1, 1, -1):
        A[1], A[i] = A[i], A[1]
        heap_size -= 1
        max_heapify(A, heap_size, 1)

def test_heapsort(A):
    heapsort(A)
    print(A)

def heap_maximum(A):
    return A[1]

def heap_extract_max(A, heap_size):
    if heap_size < 1:
        raise ValueError('heap underflow!')
    max_ = A[1]
    A[1] = A[heap_size]
    heap_size -= 1
    max_heapify(A, heap_size, 1)
    return max_, heap_size

def heap_increase_key(A, i, key):
    if key < A[i]:
        raise ValueError("new key value is smaller than current key!")
    A[i] = key
    while i > 1 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)
    
def max_heap_insert(A, key):
    A.append(MIN_MUM)
    heap_size = len(A) - 1
    heap_increase_key(A, heap_size, key)

if __name__ == '__main__':
    A = [None, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    build_max_heap(A)
    print(A)
    # heap_increase_key(A, 9, 15)
    # print(A)
    max_heap_insert(A, 18)
    print(A)