import sys
import math


class RangeMinimumQuery(object):
    """
    Given an array of integer numbers, find the minimum value from a specified range from qs to qe.

    In total, there are 5 approaches to RMQ question. Here 3 of them are given. The other two algorithms are
    Square Root Decomposition and Sparse Table Algorithm.
    """

    @classmethod
    def simple_solution(cls, arr, qs, qe):
        """
        A simple solution is to iterate and compare each elements from qs to qe.
        Time complexity is O(n) in worst case, and space complexity is O(1).
        """
        min_val = arr[qs]
        for x in xrange(qs+1, qe+1):
            min_val = min(min_val, arr[x])

        return min_val

    @classmethod
    def dp_solution(cls, arr, qs, qe):
        """
        The solution uses a table to store the sum values of all ranges. The problem is if arr is mutable,
        then it becomes expensive to update the table.

        Time complexity is O(n^2) to fill the table, but a query can be done in O(1) time. Space complexity
        is O(n^2).
        """

        n = len(arr)

        # build dp table for future query
        # table[x][y] indicates the minimum value in the range between x and y, inclusively.
        table = [[sys.maxint]*n for _ in xrange(n)]

        # k indicates the length of the range
        for k in xrange(1, n+1):
            # x indicates the starting position of the range
            for x in xrange(n-k):
                y = x + k - 1
                if x == y:
                    table[x][y] = arr[x]
                else:
                    table[x][y] = min(table[x][y-1], arr[y])

        # do the query
        return table[qs][qe]

    @classmethod
    def SegTree(cls, arr, qs, qe):
        """
        This solution is suitable for that the arr is mutable.

        The time complexity for building up segment tree is O(n); doing a query is in O(logn) time.
        Space complexity is O(n).
        """
        n = len(arr)

        # IMPORTANT: the size of SegTree
        tree_size = 2 * pow(2, math.ceil(math.log(n, 2))) - 1
        segTree = [sys.maxint for _ in xrange(tree_size)]

        # construct segment tree from arr
        cls.construct_segTree(segTree, 0, arr, 0, len(arr)-1)

        return cls.query_minValue(segTree, qs, qe, 0, n-1, 0)

    @classmethod
    def construct_segTree(cls, segTree, i, arr, start, end):
        """
        Construct a segment tree, which is a list
        :param segTree: the target segment tree
        :param i: the index of the element added to segTree
        :param arr: the given array
        :param start: the starting index of the range being handled in arr
        :param end: the ending index of the range being handled in arr
        :return: the constructed segment tree
        """

        if start == end:
            segTree[i] = arr[start]
            return segTree[i]

        # the index of left child of current node i in segTree
        left = 2*i+1
        # the index of right child of current node i in segTree
        right = 2*i+2
        mid = (start + end) / 2
        segTree[i] = min(cls.construct_segTree(segTree, left, arr, start, mid), \
                         cls.construct_segTree(segTree, right, arr, mid+1, end))
        return segTree[i]

    @classmethod
    def query_minValue(cls, segTree, qs, qe, ss, se, idx):
        """
        Get the minimum value of a specified range.
        :param segTree: the segment tree
        :param qs: the starting index of the query range
        :param qe: the ending index of the query range
        :param ss: the starting index of current range to search in array
        :param se: the ending index of current range to search in array
        :param idx: the SegTree index of minimum value in current range
        :return: the minimum value in the query range
        """

        if qs<=ss and se<=qe:
            return segTree[idx]

        if qs>se or qe<ss:
            return sys.maxint

        mid = (ss+se)/2
        return min(cls.query_minValue(segTree, qs, qe, ss, mid, 2*idx+1), \
                   cls.query_minValue(segTree, qs, qe, mid+1, se, 2*idx+2))








