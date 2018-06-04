"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page: page 109 in chapter 8

Discription of the algorithms:
A[1...n], A.lenth = n. A store all the elements which we need to sort.
B[1...n], B store the output of the sorted array.
COUNTING_SORT(A,B,k)
1   let C[0...k] be a new array
2   for i = 0 to k
3       C[i] = 0
4   for j = 1 to A.lenth
5       C[A[j]] = C[A[j]] + 1  //C now contains the number of elements equal to j
6   for i = 1 to k
7       C[j] = C[j] + C[j-1]   //C now contains the number of elements less than or equal to i
8   for j = A.lenth downto 1
9       B[C[A[j]]] = A[j]
10      C[A[j]] = C[A[j]] - 1 
"""

def counting_sort(A, B, k):
    C = [0] * (k+1)
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1

A = [2,5,3,0,2,3,0,3]
B = [0,0,0,0,0,0,0,0]
counting_sort(A, B, 5)
print(B)