

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, sum, valuelist):
            if root.val == sum and root.left is None and root.right is None:
                res.append(valuelist)
            if root.left:
                dfs(root.left, sum-root.val, valuelist+[root.left.val])
            if root.right:
                dfs(root.right, sum-root.val, valuelist+[root.right.val])
        res = []
        if root is None: return res
        dfs(root, sum, [root.val])
        return res
