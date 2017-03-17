

# Find the k'th largest element in a stream
#
# Given an infinite stream of integers, find the k'th largest element at any point of time. Extra space allowed is O(k).
#
# Example:
#
# Input:
# stream[] = {10, 20, 11, 70, 50, 40, 100, 5, ...}
# k = 3
#
# Output:    {_,   _, 10, 11, 20, 40, 50,  50, ...}
#

# Method 1: Keep an array of size k.
# The idea is to keep the array sorted so that the k'th largest element can be found in O(1) time. For every new element
# in stream, check if the new element is smaller than current k'th largest element. If yes, then ignore it. If no, then
# remove the smallest element from array and insert new element in sorted array. Time complexity for insertion operation
# is O(k).


# Method 2: Use a Self Balancing Binary Search Tree (AVL, RB, etc.) of size k. The k'th largest element can be found in O(Logk) time.
# For every new element in stream, check if the new element is smaller than current k'th largest element. If yes, then
# ignore it. If no, then remove the smallest element from the tree and insert new element. Time complexity of processing
# a new element is O(Logk).


# Method 3: use MinHeap of size k to store k largest elements of stream. The k'th largest element is always at root and
# can be found in O(1) time.
# For every new element, compare the new element with root of heap. If new element is smaller, then ignore it. Otherwise,
# replace root with new element and call heapify for the root of modified heap. Time complexity of finding the k'th largest
# element is O(Logk).

import heapq

def find_kthLargest(stream, k):
    harr = [v for i, v in enumerate(stream) if i < k]
    heapq.heapify(harr)
    for v in stream:
        if harr[0] < v:
            harr[0] = v
            heapq.heapify(harr)
    return harr[0]