

# Jump Search
#
# Like Binary Search, Jump Search is a searching algorithm for sorted arrays. The basic idea is to check fewer
# elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching
# all elements.

# What is the optimal block size to be skipped?
# In the worst case, we have to do n/m jumps and if the last checked value is greater than the element to be
# searched for, we perform m-1 comparisons more for linear search. Therefore the total number of comparisons in
# the worst case will be ((n/m) + m-1). The value of the function ((n/m) + m-1) will be minimum when m = sqrt(n).
# Therefore, the best step size is m = sqrt(n).

# Important points:
# 1. Works only sorted arrays.
# 2. The optimal size of a block to be jumped is O(sqrt(n)). This makes the time complexity of Jump Search O(sqrt(n)).
# 3. The time complexity of Jump Search is between Linear Search (O(n)) and Binary Search (O(logn)).
# 4. Binary Search is better than Jump Search, but Jump search has an advantage that we traverse back only once
#    (Binary Search may require up to O(Log n) jumps, consider a situation where the element to be search is the
#     smallest element or smaller than the smallest). So in a system where jumping back is costly, we use Jump Search.

# Time Complexity : O(sqrt(n)). Auxiliary Space : O(1)


import math

def jumpSearch(arr, key):
    n = len(arr)

    # finding the block size to be jumped
    block = int(math.floor(math.sqrt(n)))

    # searching the block where key is present (if it is present)
    pre = 0
    step = block
    while arr[min(step, n)-1] < key:
        pre = step
        step += block
        if pre >= n:
            return -1

    # doing linear search for key in block begining with pre
    while arr[pre] < key:
        pre += 1

        if pre == min(step, n):
            return -1

    if arr[pre] == key:
        return pre

    return -1
