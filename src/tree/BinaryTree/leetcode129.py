
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, sum):
            # base case
            if root. left is None and root. right is None:
                self.totalsum += sum
            # recursive step
            else:
                if root.left: dfs(root.left, sum* 10 + root.left.val)
                if root.right: dfs(root.right, sum * 10 + root.right.val)

        if root is None:
            return 0
        self.totalsum = 0
        dfs(root, root.val)
        return self.totalsum


