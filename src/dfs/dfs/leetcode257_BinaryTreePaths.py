

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    @ Google, Apple, Facebook

    Given a binary tree, return all root-to-leaf paths.

    For example, given the following binary tree:

       1
     /   \
    2     3
     \
      5
    All root-to-leaf paths are:

    ["1->2->5", "1->3"]
    """
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):

        def dfs(root, path):
            if root.left is None and root.right is None:
                res.append(path)
                return
            if root.left:
                dfs(root.left, path + '->' + str(root.left.val))
            if root.right:
                dfs(root.right, path + '->' + str(root.right.val))

        res = []
        if root is None:
            return res
        dfs(root, str(root.val))
        return res