

# Find k closest elements to a given value. Given a sorted array arr[] and a value X, find the k closest elements to
# X in arr[].
#
# Examples:
# Input: K = 4, X = 35
#        arr[] = {12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56}
# Output: 30 39 42 45
#
# Note that if the element is present in array, then it should not be in output, only the other closest elements are
# required.

# Two methods to solve this question
#
# 1. Simple solution is to do linear search for k closest elements
#   a) Start from the first element and search for the crossover point, before which elements are smaller than or equal
#      to X, and after which elements are greater). This step takes O(n) time.
#   b) Once we find crossover point, we can compare elements on both sides of crossover point to pick k closest elements.
#      This takes O(k) time.
# The total time complexity is O(n).
#
# 2. Optimized solution is to find k closest elements in O(logn + k) time. The idea is to use Binary Search to find
#    crossover point in O(Logn) time. Then, we can pick k closest elements in O(k) time.


def find_kClosestElements(arr, x, k):
    res = []
    n = len(arr)
    lo = find_crossover(arr, x)
    hi = lo + 1
    count = 0

    while arr[lo] == x:
        lo -= 1

    while arr[hi] == x:
        hi += 1

    if (lo+1) + (n-hi+1) < k:
        print 'The total number of elements in array is less than k.'
        return res

    while lo >=0 and hi < n and count < k:
        if x-arr[lo] < arr[hi]-x:
            res.append(arr[lo])
            lo -= 1
        else:
            res.append(arr[hi])
            hi += 1
        count += 1

    # There is no more element on right side
    while lo >= 0 and count < k:
        res.append(arr[lo])
        lo -= 1
        count += 1

    # There is no more element on left side
    while hi < n and count < k:
        res.append(arr[hi])
        hi += 1
        count += 1

    return res

def find_crossover(arr, x):
    lo, hi = 0, len(arr)-1

    # all elements in array are less than or equal to x
    if arr[hi] <= x:
        return hi

    # all elements in array are greater than x
    if arr[lo] >= x:
        return lo

    # binary search for crossover point
    while lo <= hi:
        mid = lo + (hi-lo) >> 1

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid -1