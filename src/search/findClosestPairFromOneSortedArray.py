

# Find the pair in array whose sum is closest to x.
#
# Given a sorted array and a number x, find a pair in array whose sum is closest to x.
# Examples:
#   Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
#   Output: 22 and 30
#
#   Input: arr[] = {1, 3, 4, 7, 10}, x = 15
#   Output: 4 and 10
#

# A simple solution is to consider every pair and keep track of closest pair (absolute
# difference between pair sum and x is minimum). Finally print the closest pair. Time
# complexity of this solution is O(n^2).

# An efficient solution can find the pair in O(n) time. The algorithm is
# 1) Initialize a variable diff as infinite, which is used to store the difference between pair and x. We need to find
#    the minimum diff.
# 2) Initialize two index variables l and r in the given sorted array.
#   a) Initialize first to the leftmost index: l = 0
#   b) Initialize second to the rightmost index: r = n-1
# 3) while l < r:
#   a) if abs(arr[l]+arr[r]-x) < diff, then update diff and res
#   b) if arr[l]+arr[r] < x, then l+1
#   c) else r-1

import sys

def find_closestPair(arr, x):
    n = len(arr)
    res = []
    diff = sys.maxint
    l, r = 0, n-1
    while l < r:
        if abs(arr[l]+arr[r]-x) < diff:
            diff = abs(arr[l]+arr[r]-x)
            res = [arr[l], arr[r]]

        if arr[l] + arr[r] < x:
            l += 1
        elif arr[l] + arr[r] > x:
            r -= 1
        else:
            break
    return res

