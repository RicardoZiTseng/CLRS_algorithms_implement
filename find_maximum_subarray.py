"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page: page 41 in chapter 4

Discription of the algorithms:
FIND-MAXIMUM-SUBARRAY(A, low, high)
1  if high == low
2       return (low, high, A[low])
3  else mid = [low + high] / 2
4       (left-low, left-high, left-sum) = FIND-MAXIMUM-SUBARRAY(A, low, mid)
5       (right-low, right-high, right-sum) = FIND-MAXIMUM-SUBARRAY(A, mid+1, high)
6       (cross-low, cross-high, cross-sum) = FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)
7       if left-sum >= right_sum and left_sum >= cross_sum
8           return(left-low, left-high, left-sum)
9       else if right-sum >= left-sum and right-sum >= cross-sum
10          return(right-low, right-high, right-sum)
11      else return(cross-low, cross-high, cross-sum)
"""

# A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
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

def find_maximum_subarray(array, low, high):
    if low == high:
        return (low, high, array[low])
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = find_maximum_subarray(array, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(array, mid+1, high)
        (cross_left, cross_right, cross_sum) = find_max_crossing_subarray(array, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_left, cross_right, cross_sum)

if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    (left, right, sumValue) = find_maximum_subarray(A, 0, len(A)-1)
    print("left is : {0}, right is : {1}, Sum is : {2}".
            format(left, right, sumValue))
"""
out:
left is : 7, right is : 10, Sum is : 43
"""