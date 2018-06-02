"""
author: Ricardo
pages of CLRS: chinese page: page 40 in chapter 4

Discription of the algorithms:
FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)
1  left-sum = -MAX
2  sum = 0
3  for i = mid downto low
4    sum = sum + A[i]
5    if sum > left-sum
6        left-sum = sum
7        max_left = i
8  right-sum = -MAX
9  sum = 0
10 for j = mid+1 to high
11   sum = sum + A[j]
12   if sum > right-sum
13       right-sum = sum
14       max-right = j
15 return (max-left, max_right, left-sum + right-sum)    
"""
A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

MAX_NUM = 0x0fffffff # 268435455

def find_max_crossing_subarray(array, low, mid, high):
    left_sum = -MAX_NUM
    tot_sum = 0
    max_left = mid
    for i in range(mid, low-1, -1):
        tot_sum = tot_sum + array[i]
        if tot_sum > left_sum:
            left_sum = tot_sum
            max_left = i
        
    right_sum = -MAX_NUM
    tot_sum = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1, 1):
        tot_sum = tot_sum + array[j]
        if tot_sum > right_sum:
            right_sum = tot_sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


low = 0
high = len(A) - 1
mid = int((low + high) / 2)
max_left, max_right, max_sum = find_max_crossing_subarray(A, low, mid, high)
print("max_left: " + str(max_left + 1))
print("max_right:" + str(max_right + 1))
print("max_sum:" + str(max_sum))

"""
output: 
max_left: 8
max_right:11
max_sum:43
"""