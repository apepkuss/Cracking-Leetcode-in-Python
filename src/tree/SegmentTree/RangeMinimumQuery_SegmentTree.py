import sys

class RangeMinimumQuery(object):
    """
    Segment tree can be used to compute the maximum, minimum, or sum of a given range of an array.
    The following code demonstrates how to construct a segment tree for a specified array, and how
    to get range minimum value. When there is an update on an element of the array, how to update
    the segment tree.

    Representation of Segment trees
        1. Leaf Nodes are the elements of the input array.
        2. Each internal node represents some merging of the leaf nodes. The merging may be different
           for different problems. For this problem, merging is sum of leaves under a node.
        An array representation of tree is used to represent Segment Trees. For each node at index i,
        the left child is at index 2*i+1, right child at 2*i+2 and the parent is at math.floor((i-1)/2).

    Construction of Segment Tree from given array
        All levels of the constructed segment tree will be completely filled except the last level.
        Also, the tree will be a Full Binary Tree because we always divide segments in two halves
        at every level. Since the constructed tree is always full binary tree with n leaves, there
        will be (n-1) internal nodes. So total number of nodes will be (2n-1).
    """
    # the size of segTree is 2*pow(2,ceil(log(n,2)))-1, where n is the length of arr
    segTree = []

    @classmethod
    def construct_tree(cls, arr, low, high, pos):
        if low == high:
            cls.segTree[pos] = arr[low]
        else:
            mid = (low+high)/2
            cls.construct_tree(arr, low, mid, 2*pos+1)
            cls.construct_tree(arr, mid+1, high, 2*pos+2)
            cls.segTree[pos] = min(cls.segTree[2 * pos + 1], cls.segTree[2 * pos + 2])

    @classmethod
    def get_rangeMinValue(cls, qlow, qhigh, low, high, pos):
        """
        Get the minimum value in the range of an array
        :param qlow: the low boundary of a specified range
        :param qhigh: the high boundary of a specified range
        :param low: the low boundary of the range represented by current visiting node in segment tree
        :param high: the high boundary of the range represented by current visiting node in segment tree
        :param pos: the index of current visiting node in segment tree
        :return: the minimum value in the specified range
        """
        # total overlap
        if qlow <= low and qhigh >= high:
            return cls.segTree[pos]

        # no overlap
        if qlow > high or qhigh < low:
            return sys.maxint

        # partial overlap
        mid = (low+high)/2
        return min(cls.get_rangeMinValue(qlow, qhigh, low, mid, 2*pos+1), \
                   cls.get_rangeMinValue(qlow, qhigh, mid+1, high, 2*pos+2))

    @classmethod
    def updateValue(cls, arr, i, new_value):
        """
        Update the value of arr[i], and meanwhile update the segment tree
        """

        # check for invalid input index
        if i < 0 or i > len(arr) - 1:
            print "The element to update out of range"
            return

        # update the value in array
        arr[i] = new_value

        # update the values of nodes in segment tree
        cls.updateValueUntil(0, len(arr) - 1, i, new_value, 0)

    @classmethod
    def updateValueUntil(cls, ss, se, i, new_value, si):
        """
        Update the nodes in segment tree, which have given index of their range
        :param ss: the starting index of the segment represented by the current node, segTree[si]
        :param se: the ending index of the segment represented by the current node, segTree[si]
        :param i: the index of the element to be updated in array
        :param diff: the value to be added to all nodes which have i in range.
        :param si: the index of current node in the segment tree. The initial value is 0.
        """
        if ss == se:
            cls.segTree[si] = new_value
            return cls.segTree[si]

        mid = ss + (se - ss) / 2
        if i <= mid:
            left = cls.updateValueUntil(ss, mid, i, new_value, 2*si+1)
            cls.segTree[si] = min(left, cls.segTree[2*si+2])
        else:
            right = cls.updateValueUntil(mid+1, se, i, new_value, 2*si+2)
            cls.segTree[si] = min(cls.segTree[2*si+1], right)
        return cls.segTree[si]







