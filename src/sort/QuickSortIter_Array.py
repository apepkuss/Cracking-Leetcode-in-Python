

# QuickSort vs. MergeSort
# Quick Sort in its general form is an in-place sort (i.e. it doesn't require any extra storage) whereas merge sort
# requires O(N) extra storage, N denoting the array size which may be quite expensive. Allocating and de-allocating
# the extra space used for merge sort increases the running time of the algorithm. Comparing average complexity we
# find that both type of sorts have O(NlogN) average complexity but the constants differ. For arrays, merge sort loses
# due to the use of extra O(N) storage space.

# Most practical implementations of Quick Sort use randomized version. The randomized version has expected time
# complexity of O(nLogn). The worst case is possible in randomized version also, but worst case doesn't occur for a
# particular pattern (like sorted array) and randomized Quick Sort works well in practice.

# Iterative quick sort implementation
def quick_sort_iterative(arr, low, high):
    if low < high:

        n = len(arr)

        # initialize stack
        stack = [0] * n
        stack.append(low)
        stack.append(high)

        while stack:
            # set the low and high boundary of subarray to sort
            h = stack.pop()
            l = stack.pop()

            # set pivot element at its correct position in sorted array
            p = partition(arr, l, h)

            # if there are elements on the left side of pivot, then push
            # boundary indices of left side into stack
            if p - 1 > l:
                stack.append(l)
                stack.append(p-1)

            # if there are elements on the right side of pivot, then push
            # boundary indices of right side into stack
            if p + 1 < h:
                stack.append(p+1)
                stack.append(h)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # move pivot value to the correct position
    arr[i], arr[high] = arr[high], arr[i]
    return i