

# Given an array of n elements, where each element is at most k away from its target position, devise an algorithm
# that sorts in O(n log k) time. For example, let us consider k is 2, an element at index 7 in the sorted array,
# can be at indexes 5, 6, 7, 8, 9 in the given array.

# Method 1: based on insertion sort. the time complexity is O(nk).
def kSortedArray_insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1

        # the following internal while-loop runs at most k times.
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

# Method 2: use min heap. Building up a min heap takes O(k) time for k elements; removing operation uses O(n) time,
#           while adding new elements need O((n-k)log(n-k)) time in total.
def kSortedArray_minHeap(arr):
    arr = build_minHeap(arr)
    res = []
    for i in range(len(arr)):
        val, arr = extract_minValue(arr)
        res.append(val)
    return res

def build_minHeap(arr):
    harr = arr
    i = (len(arr)-1)/2
    while i >= 0:
        harr = minHeapify(harr, i)
        i -= 1
    return harr

def minHeapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    smallest = i
    if left < len(arr) and arr[left] < arr[smallest]:
        smallest = left
    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        arr = minHeapify(arr, smallest)
    return arr

def extract_minValue(arr):
    value = arr[0]
    arr[0] = arr[-1]
    arr = arr[:len(arr)-1]
    arr = minHeapify(arr, 0)
    return value, arr


