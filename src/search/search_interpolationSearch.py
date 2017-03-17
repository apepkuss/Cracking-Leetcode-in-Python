

# The Interpolation Search is an improvement over Binary Search for instances,
# where the values in a sorted array are uniformly distributed. Binary Search
# always goes to middle element to check. On the other hand interpolation search
# may go to different locations according the value of key being searched. For
# example if the value of key is closer to the last element, interpolation search
# is likely to start search toward the end side.


# The precondition of the algorithm is that the given array is a sorted array of n
# uniformly distributed values.
# Time Complexity : If elements are uniformly distributed, then O(log(logn)).
# In worst case it can take up to O(n). Auxiliary Space : O(1)

def interpolationSearch(arr, key):
    n = len(arr)
    lo, hi = 0, n-1
    while lo <= hi:
        # Probe position formula. The idea of formula is to return higher
        # value of pos when the element to be searched is closer to arr[hi].
        # And smaller value when closer to arr[lo].
        pos = lo + (key - arr[lo]) * (hi - lo) / (arr[hi] - arr[lo])

        if arr[pos] == key: return pos

        if arr[pos] < key:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1