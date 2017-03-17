

# Find three closest elements from given three sorted arrays.
#
# Given three sorted arrays A[], B[] and C[], find 3 elements i, j and k from A, B and C respectively such that
# max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized. Here abs() indicates absolute value.
#
# Example :
#
# Input: A[] = {1, 4, 10}
#        B[] = {2, 15, 20}
#        C[] = {10, 12}
# Output: 10 15 10
# 10 from A, 15 from B and 10 from C
#
# Input: A[] = {20, 24, 100}
#        B[] = {2, 19, 22, 79, 800}
#        C[] = {10, 12, 23, 24, 119}
# Output: 24 22 23
# 24 from A, 22 from B and 23 from C

# Method 1: a simple solution is to run three nested loops to consider all triplets from A, B, and C arrays. Compute
#           the value of max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) for every triplet and return the
#           minimum of all values. Time complexity is O(n^3).


# Method 2: Use Binary Search. The time complexity is O(nLogn).
# 1. Iterate over all elements of A[],
#   a) Binary search for elements just smaller than or equal to A[i] in B[] and C[], and compute the difference.
# 2. Return overall minimum.


# Method 3:
# Suppose p, q, r is the length of A, B, and C, respectively.
# 1. Initialize three index variables i, j, k to 0
# 2. Loop while i<p, j<q, k<r:
#   a) Find x = min(A[i], B[j], C[k]) and y = max(A[i], B[j], C[k]))
#   b) Compute diff = min(diff, y - x)
#   c) Increment the index of the array which is the minimum.
#
# Time complexity is O(p+q+r).
#

import sys

def find_closest(A, B, C):
    p, q, r = len(A), len(B), len(C)
    i, j, k = 0, 0, 0
    diff = sys.maxint
    res = []
    while i<p and j<q and k<r:
        minval = min(A[i], B[j], C[k])
        maxval = max(A[i], B[j], C[k])

        diff = min(diff, maxval-minval)
        if diff > maxval - minval:
            diff = maxval - minval
            res = [A[i], B[j], C[k]]

        if minval == A[i]:
            i += 1
        elif minval == B[j]:
            j += 1
        else:
            k += 1
    return res

