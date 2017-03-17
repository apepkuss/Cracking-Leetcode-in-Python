

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self, root):  # RT: O(n), Space: O(1)
        if root:
            # base step
            nodeCurrLevel = root
            nodeNextLevel, firstNodeNextLevel = None, None
            while nodeCurrLevel:
                # deal with the left child of current node
                if nodeCurrLevel.left:
                    if nodeNextLevel:
                        nodeNextLevel.next = nodeCurrLevel.left
                    nodeNextLevel = nodeCurrLevel.left
                    if firstNodeNextLevel is None:
                        firstNodeNextLevel = nodeNextLevel

                # deal with the right child of current node
                if nodeCurrLevel.right:
                    if nodeNextLevel:
                        nodeNextLevel.next = nodeCurrLevel.right
                    nodeNextLevel = nodeCurrLevel.right
                    if firstNodeNextLevel is None:
                        firstNodeNextLevel = nodeNextLevel

                # move to next node after visiting current node
                nodeCurrLevel = nodeCurrLevel.next

            # recursive step
            self.connect(firstNodeNextLevel)
