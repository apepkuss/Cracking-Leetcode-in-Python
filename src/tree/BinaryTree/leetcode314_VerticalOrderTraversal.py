# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    @ Google, Snapchat, Facebook

    Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
    If two nodes are in the same row and column, the order should be from left to right.

    Analysis: this question cannot be solved using dfs algorithm, because the order of the nodes in the result should follow
    the visiting order level by level. Therefore, BFS algorithm is a good choice.
    """
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # save the leftmost and rightmost positions
        leftmost, ritemost = 0, -1
        # queue for bfs, in which the element is a tuple of node and its position info
        queue = []
        # key is the position, while value is a list of nodes that are in the position
        table = {}
        if root:
            queue.append((root, 0))
            leftmost = 0
            ritemost = 0

        while queue:
            node, pos = queue.pop(0)
            if table.has_key(pos):
                table[pos].append(node.val)
            else:
                table[pos] = [node.val]

            if node.left:
                queue.append((node.left, pos - 1))
                leftmost = min(leftmost, pos - 1)
            if node.right:
                queue.append((node.right, pos + 1))
                ritemost = max(ritemost, pos + 1)

        res = []
        for i in xrange(leftmost, ritemost + 1):
            res.append(table[i])
        return res
