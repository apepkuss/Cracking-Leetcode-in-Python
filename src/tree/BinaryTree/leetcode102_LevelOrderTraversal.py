

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    @ Linkedin, Facebook, Amazon, Microsoft, Apple, Bloomberg

    Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its level order traversal as:
    [
      [3],
      [9,20],
      [15,7]
    ]
    """
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        currLevel = [root]
        while len(currLevel) > 0:
            nextLevel = []
            values = []
            for elem in currLevel:
                values.append(elem.val)
                if elem.left:
                    nextLevel.append(elem.left)
                if elem.right:
                    nextLevel.append(elem.right)
            if len(values) > 0:
                res.append(values)
            currLevel = nextLevel
        return res
