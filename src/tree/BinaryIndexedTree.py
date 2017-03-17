

class BinaryIndexedTree(object):
    """
    We have an array arr[0 . . . n-1]. We should be able to
        1 Find the sum of first i elements.
        2 Change value of a specified element of the array arr[i] = x where 0 <= i <= n-1.

    A simple solution is to run a loop from 0 to i-1 and calculate sum of elements. To update a value, simply do
    arr[i] = x. The first operation takes O(n) time and second operation takes O(1) time. Another simple solution
    is to create another array and store sum from start to i at the i-th index in this array. Sum of a given
    range can now be calculated in O(1) time, but update operation takes O(n) time now. This works well if the number
    of query operations are large and very few updates.

    Can we perform both the operations in O(log n) time once given the array?
    One Efficient Solution is to use Segment Tree that does both operations in O(logn) time. Using Binary Indexed Tree,
    we can do both tasks in O(logn) time. The advantages of Binary Indexed Tree over Segment are, requires less space
    and very easy to implement.

    Representation
        Binary Indexed Tree is represented as an array. Let the array be BITree[]. Each node of Binary Indexed
        Tree stores sum of some elements of given array. Size of Binary Indexed Tree is equal to n where n is size
        of input array.

    Reference link: http://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
    """

    # Returns sum of arr[0..index]. This function assumes
    # that the array is preprocessed and partial sums of
    # array elements are stored in BITree[].
    @classmethod
    def getsum(cls, BITTree, i):  # O(logn) time
        """
        Get the sum of first i elements in the array
        :param BITTree: the binary indexed tree
        :param i: the index, inclusive
        :return:
        """
        s = 0  # initialize result

        # index in BITree[] is 1 more than the index in arr[]
        i = i + 1

        # Traverse ancestors of BITree[index]
        while i > 0:
            # Add current element of BITree to sum
            s += BITTree[i]

            # Move index to parent node in getSum View
            i -= i & (-i)
        return s

    # Updates a node in Binary Index Tree (BITree) at given index
    # in BITree.  The given value 'val' is added to BITree[i] and
    # all of its ancestors in tree.
    @classmethod
    def updatebit(cls, BITTree, n, i, v):  # O(logn) time
        """
        Update a specified node of the target binary indexed tree
        :param BITTree: the binary indexed tree to update
        :param n: the number of the nodes
        :param i: the target node to update
        :param v: new value set to the target node
        :return: updated binary index tree
        """

        # index in BITree[] is 1 more than the index in arr[]
        i += 1

        # Traverse all ancestors and add 'val'
        while i <= n:
            # Add 'val' to current node of BI Tree
            BITTree[i] += v

            # Update index to that of parent in update View
            i += i & (-i)

    # Constructs and returns a Binary Indexed Tree for given
    # array of size n.
    @classmethod
    def construct(cls, arr):  # O(n*logn) time, O(n) space
        """
        Construct a binary indexed tree for a specified array
        :param arr: an array
        :return: a binary indexed tree
        """
        n = len(arr)

        # Create and initialize BITree[] as 0
        BITTree = [0] * (n + 1)

        # Store the actual values in BITree[] using update()
        for i in range(n):
            cls.updatebit(BITTree, n, i, arr[i])

        # Uncomment below lines to see contents of BITree[]
        # for i in range(1,n+1):
        #      print BITTree[i],
        return BITTree