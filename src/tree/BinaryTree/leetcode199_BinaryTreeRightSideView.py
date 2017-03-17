
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    @ Amazon

    Given a binary tree, imagine yourself standing on the right side of it, return 
    the values of the nodes you can see ordered from top to bottom.

    For example:
    Given the following binary tree,
      1            <---
    /   \\
    2     3        <---
    \\     \\
     5      4      <---
    You should return [1, 3, 4].
    """

    # The idea is to traverse the tree level by level (BFS). The last node in each level should be
    # in the final result.
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None: return res
        curr_level = [root]
        while len(curr_level) > 0:
            next_level = []
            for i in range(len(curr_level)):
                if i == len(curr_level)-1:
                    res.append(curr_level[i].val)
                if curr_level[i].left:
                    next_level.append(curr_level[i].left)
                if curr_level[i].right:
                    next_level.append(curr_level[i].right)
            curr_level = next_level
        return res