

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        currLevel = [root]
        reversed = False
        while len(currLevel) > 0:
            nextLevel = []
            values = []
            for item in currLevel:
                values.append(item.val)
                if item.left:
                    nextLevel.append(item.left)
                if item.right:
                    nextLevel.append(item.right)
            if len(values) > 0:
                res.append(values[::-1] if reversed else values)
            reversed = not reversed
            currLevel = nextLevel
        return res
