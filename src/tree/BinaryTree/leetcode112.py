
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(root, sum):
            if root is None:
                return False
            # base case
            if root.val == sum and root.left is None and root.right is None:
                return True
            # recursive step
            return dfs(root.left, sum - root.val) or dfs(root.right, sum - root.val)

        return dfs(root, sum)
