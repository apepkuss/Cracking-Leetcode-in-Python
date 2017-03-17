

# Find median in a stream of integers (running integers)
#
# Given that integers are read from a data stream. Find median of elements read so far in efficient way. For simplicity
# assume there are no duplicates. For example, let us consider the stream 5, 15, 1, 3 ...
#
# After reading 1st element of stream - 5 -> median - 5
# After reading 2nd element of stream - 5, 15 -> median - 10
# After reading 3rd element of stream - 5, 15, 1 -> median - 5
# After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on...


# For getting the median, when the input size is odd, we take the middle element of sorted data. If the input size is
# even, we pick the average of middle two elements of sorted data.

# Note that output is effective median of integers read from the stream so far. Such an algorithm is called online
# algorithm. Any algorithm that can guarantee output of i-elements after processing i-th element, is said to be online
# algorithm.

# Method 1: Insertion Sort
# Insertion sort is an online algorithm that sorts the data appeared so far. At any instance of sorting, after sorting
# i'th element, the first i elements of array are sorted. The insertion sort doesn't depend on future data to sort data
# input till that point. This is the key part of insertion sort that makes it an online algorithm. However, insertion
# sort takes O(n^2) time to sort n elements.


# Method 2: Augmented self balancing binary search tree (AVL, RB, etc.)
# At every node of BST, maintain number of elements in the subtree rooted at that node. We can use a node as root of
# simple binary tree, whose left child is self balancing BST with elements less than root and right child is self
# balancing BST with elements greater than root. The root element always holds effective median.
# If left and right subtrees contain same number of elements, root node holds average of left and right subtree root
# data. Otherwise, root contains same data as the root of subtree which is having more elements. After processing an
# incoming element, the left and right subtrees (BST) are differed utmost by 1.


# Method 3: use a max heap and a min heap
# Similar to balancing BST in Method 2 above, we can use a max heap on left side to represent elements that are less
# than effective median, and a min heap on right side to represent elements that are greater than effective median.

# After processing an incoming element, the number of elements in heaps differ utmost by 1 element. When both heaps
# contain same number of elements, we pick average of heaps root data as effective median. When the heaps are not
# balanced, we select effective median from the root of heap containing more elements.

