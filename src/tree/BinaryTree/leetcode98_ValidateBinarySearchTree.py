
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    @ Amazon, Microsoft, Bloomberg, Facebook

    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    Example 1:
        2
       / \
      1   3
    Binary tree [2,1,3], return true.
    Example 2:
        1
       / \
      2   3
    Binary tree [1,2,3], return false.
    """
    # Method 1: make use of in-order traversal of a BST, as the result of in-order traversal should be a sequence in
    # increasing order
    def isValidBST_inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root== None:
            return True
        vals = self.inorderTraversal(root)
        # case1: the result from inorder traversal is not a increasing sequence
        # case2: the result from inorder traversal contains duplicates
        # for the two cases above, return false
        if (len(vals) > 1 and (vals != sorted(vals))) or (len(vals) > len(list(set(vals)))):
            return False
        return True

    def inorderTraversal(self, root):
        vals = []
        if root:
            stack = []
            while stack != [] or root:
                if root:
                    # traverse left subtree
                    stack.append(root)
                    root = root.left
                else:
                    # traverse root and right subtree
                    root = stack.pop()
                    vals.append(root.val)
                    root = root.right
        return vals

    # Method 2: recursive method
    def isValidBST_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        return self.validBST(root, -sys.maxint - 1, sys.maxint)

    def validBST(self, root, lower, upper):
        if root is None: return True
        return lower < root.val < upper and self.validBST(root.left, lower, root.val) and self.validBST(
            root.right, root.val, upper)
