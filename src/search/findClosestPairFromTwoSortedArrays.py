

# Find the closest pair from two sorted arrays
#
# Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from
# each array.

# Method 1: A simple solution is to run two loops. The outer loop considers every element of first array and inner loop
# checks for the pair in second array. We keep track of minimum difference between ar1[i] + ar2[j] and x. The time
# complexity is O(mn), where m and n is the length of the two arrays, respectively.

# Method 2: The O(m+n) time solution with O(m+n) space.
# 1) Merge given two arrays into an auxiliary array of size m+n using merge process of merge sort. While merging, keep
#    another boolean array of size m+n to indicate whether the current element in merged array is from arr1 or arr2.
# 2) Consider the merged array and use the linear time algorithm to find the pair with sum closest to x. One extra thing
#    we need to consider only those pairs which have one element from ar1[] and other from ar2[], we use the boolean
#    array for this purpose.

# Method 3: The linear time solution with O(1) space.
# The idea is to start from left side of one array and right side of another array, and use the algorithm same as
# step 2 of above approach.
#
# 1) Initialize a variable diff as infinite, which is used to store the difference between pair and x. We need to find
#    the minimum diff.
# 2) Initialize two index variables l and r in the given sorted arrays.
#   a) Initialize first to the leftmost index in arr1: l = 0
#   b) Initialize second to the rightmost index in arr2: r = len(arr2)-1
# 3) While l < len(arr1) and r >= 0:
#   a) If abs(arr1[l]+arr2[r]-x) < diff, then update diff and res
#   b) If arr1[l]+arr2[r] < x, then l+1
#   c) Elif arr1[l]+arr2[r] > x, then r-1
#   d) Else: break

import sys

def find_closestPair(arr1, arr2, x):
    m, n = len(arr1), len(arr2)
    diff = sys.maxint
    res = []
    l, r = 0, n-1
    while l < m and r >=0:
        if abs(arr1[l]+arr2[r]-x) < diff:
            diff = abs(arr1[l]+arr2[r]-x)
            res = [arr1[l], arr2[r]]
        if arr1[l]+arr2[r] < x:
            l += 1
        elif arr1[l]+arr2[r] > x:
            r -= 1
        else:
            break
    return res