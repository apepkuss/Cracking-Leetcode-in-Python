

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    @ Linkedin, Bloomberg, Microsoft
    
    Tree, BFS, Stack
    
    Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its zigzag level order traversal as:
    [
      [3],
      [20,9],
      [15,7]
    ]
    """
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res

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

            if values:
                res.append(values[::-1] if reversed else values)

            reversed = not reversed
            currLevel = nextLevel
        return res
