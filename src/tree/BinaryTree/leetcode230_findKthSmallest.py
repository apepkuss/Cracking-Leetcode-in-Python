

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class AugmentedTreeNode(TreeNode):
    def __init__(self, x):
        TreeNode.__init__(self, x)
        # the number of the nodes on the left subtree
        self.left_count = 0

class Solution(object):
    """
    @ Bloomberg, Uber, Google

    Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
    Note: You may assume k is always valid, 1 <= k <= BST's total elements.

    Method 1 is better for immutable BST, while method 2 is better for mutable BST.
    Method 3 is based on Morris Traversal algorithm, which has O(1) addition space.
    """
    # Method 1: Inorder traversal in O(n) time, O(n) space, where n is total nodes in tree.
    # Inorder traversal of BST retrieves elements of tree in the sorted order. The inorder traversal uses stack
    # to store to be explored nodes of tree. The idea is to keep track of popped elements which participate in
    # the order statics.
    def kthSmallest_InorderTraversal(self, root, k): # O(n) time, O(n) space)
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while len(stack)>0 or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k-=1
                if k==0:
                    return root.val
                root = root.right


    # Method 2: Augmented tree data structure. O(h) time, where h is the height of tree. O(n) additional space
    #           for saving the node count on the left subtree of each node.
    # The idea is to maintain rank of each node. We can keep track of elements in a subtree of any node while
    # building the tree. Assume that the root is having N nodes in its left subtree. If K = N + 1, root is K-th
    # node. If K < N, we will continue our search (recursion) for the Kth smallest element in the left subtree
    # of root. If K > N + 1, we continue our search in the right subtree for the (K-N-1)-th smallest element.
    # Note that we need the count of elements in left subtree only.

    def build_bst(self, values):
        """
        Build up a binary search tree based on the given list of values.
        :param values: a list of values
        :return: the root of the bst
        """
        n = len(values)
        root = None
        for i in range(n):
            node = AugmentedTreeNode(values[i])
            # insert the new node into BST
            root = self.insert_node(root, node)
        return root

    def insert_node(self, root, node):
        """
        Insert the new node in the existing BST
        :param root: the root of BST
        :param node: the new node to insert
        :return: the root of BST after inserting the new node
        """
        if not root:
            return node

        parent = root
        curr = root
        while curr:
            if node.val < curr.val:
                # increase the node count on the left subtree of current node
                curr.left_count += 1
                curr = curr.left
            else:
                curr = curr.right

        if node.val < parent.val:
            # insert the new node on left side
            parent.left = node
        else:
            # insert the new node on right side
            parent.right = node

        return root

    def kthSmallest_AugmentedTree(self, root, k):
        res = -1
        if root:
            curr = root
            while curr:
                if curr.left_count + 1 == k:
                    res = curr.val
                    break
                elif k > curr.left_count:
                    # the node count on the left subtree is less than k,
                    # so search on the right subtree
                    k = k - curr.left_count - 1
                    curr = curr.right
                else:
                    curr = curr.left
        return res


    # Method 3: Morris Traversal based inorder traversal with O(1) space.
    # The idea is to use Morris Traversal. In this traversal, we first create links to Inorder successor and
    # print the data using these links, and finally revert the changes to restore original tree.
    def kthSmallest_Morris(self, root, k):
        import sys
        count = 0
        ksmall = sys.maxint
        curr = root
        while curr:
            if not curr.left:
                count += 1
                if count == k:
                    ksmall = curr.val
                    break
                curr = curr.right
            else:
                pre = curr.left

                while pre.right and pre.right != curr:
                    pre = pre.right

                if not pre.right:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    count += 1
                    if count == k:
                        ksmall = curr.val
                        break
                    curr = curr.right
        return ksmall
