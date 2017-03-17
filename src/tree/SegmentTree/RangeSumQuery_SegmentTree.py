import math

class RangeSumQuery(object):

    # segment tree is a complete binary tree, therefore, for an array of length n, segment tree
    # has 2*n-1 nodes.
    segTree = None

    @classmethod
    def SegmentTree(cls, arr):
        x = math.ceil(math.log(len(arr), 2))
        size = 2 * math.pow(2, x) - 1
        cls.segTree = [None for _ in xrange(size)]
        # build up segment tree
        cls.constructSegTree(arr, 0, len(arr)-1, 0)

    @classmethod
    def constructSegTree(cls, arr, ss, se, si):
        """
        Build up segment tree from a specified array
        :param arr:
        :param ss: the starting index of a segment that segTree[si] represents
        :param se: the ending index of a segment that segTree[si] represents
        :param si: the index of current node of segment tree
        """
        # Base case: save the value of arr[ss] in segTree[si], which is leaf node
        if ss == se:
            cls.segTree[si] = arr[ss]
            return arr[ss]

        # Recursive step: sum the values of left and right sub-trees
        mid = (ss+se)/2
        cls.segTree[si] = cls.constructSegTree(arr, ss, mid, 2*si+1) + \
                          cls.constructSegTree(arr, mid+1, se, 2*si+2)
        return cls.segTree[si]

    @classmethod
    def getSum(cls, n, qs, qe):
        """
        Get the sum of range from qs to qe.
        :param n: the length of the target array
        :param qs: the staring index of the range to query
        :param qe: the ending index of the range to query
        :return: the sum of the specified range
        """
        if qs > qe or qs < 0 or qe > n-1:
            print "Invalid range to query"
            return None

        cls.getSumUtil(0, n-1, qs, qe, 0)

    @classmethod
    def getSumUtil(cls, ss, se, qs, qe, si):
        """
        Get the sum of a specified range from qs to qe
        :param ss: the starting index of the segment current node segTree[si] represents
        :param se: the ending index of the segment current node segTree[si] represents
        :param qs: the starting index of the query range
        :param qe: the ending index of the query range
        :param si: the index of current segment tree node
        :return: the sum of the specified range
        """
        if qs<=ss and se<=qe:
            return cls.segTree[si]

        if ss>qe or se<qs:
            return 0

        mid = (ss+se)/2
        return cls.getSumUtil(ss, mid, qs, qe, 2*si+1) + cls.getSumUtil(mid+1, se, qs, qe, 2*si+2)

    @classmethod
    def updateValue(cls, arr, i, new_value):
        """
        Update the value of arr[i], and meanwhile update the segment tree
        """

        # check for invalid input index
        if i < 0 or i > len(arr) - 1:
            print "The element to update out of range"
            return

        # get the difference between new value and old value
        diff = new_value - arr[i]

        # update the value in array
        arr[i] = new_value

        # update the values of nodes in segment tree
        cls.updateValueUtil(0, len(arr) - 1, i, diff, 0)

    @classmethod
    def updateValueUtil(cls, ss, se, i, diff, si):
        """
        Update the nodes in segment tree, which have given index of their range
        :param ss: the starting index of the segment that segTree[si] represents
        :param se: the ending index of the segment that segTree[si] represents
        :param i: the index of the element to be updated in array
        :param diff: the value to be added to all nodes which have i in range.
        :param si: the index of current node in the segment tree. The initial value is 0.
        """
        # check if the index is in range of the segment of current node si
        if ss <= i <= se:
            # update the value of current node and its children
            cls.segTree[si] += diff
            if ss != se:
                mid = (ss + se) / 2
                cls.updateValueUtil(ss, mid, i, diff, 2 * si + 1)
                cls.updateValueUtil(mid + 1, se, i, diff, 2 * si + 2)

    @classmethod
    def updateRangeUtil(cls, ss, se, us, ue, diff, si):
        """
        Update segment tree for the updates of a range of array
        """

        if ss>se or ss>ue or se<us:
            print "Invalid range"
            return

        # leaf node
        if ss == se:
            cls.segTree[si] += diff
            return

        mid = (ss+se)/2
        cls.updateRangeUtil(ss, mid, us, ue, diff, 2*si+1)
        cls.updateRangeUtil(mid+1, se, us, ue, diff, 2*si+2)

        cls.segTree[si] = cls.segTree[2*si+1] + cls.segTree[2*si+2]