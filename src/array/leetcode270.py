
class Solution(object):
    """
    @ Microsoft, Google, Snapchat

    Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
    Note: Given target value is a floating point. You are guaranteed to have only one unique value in the BST that is
    closest to the target.
    """
    def closestValue_recursive(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def dfs(root, minval):
            if root is None: return minval
            if root.val == target: return root.val

            if abs(root.val - target) < abs(minval - target):
                minval = root.val

            if root.val < target:
                return dfs(root.right, minval)
            else:
                return dfs(root.left, minval)

        import sys
        return dfs(root, sys.float_info.max)

    def closestValue_iterative(self, root, target):
        import sys
        minval = sys.float_info.max
        while root:
            if root.val == target:
                return root.val
            if abs(root.val-target) < abs(minval-target):
                minval = root.val
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return minval