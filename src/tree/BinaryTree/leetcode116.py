

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect_recursive(self, root):  # RT: O(n), Space: O(1)
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect_recursive(root.left)
            self.connect_recursive(root.right)

    def connect_iterative(self, root):  # RT: O(n), Space: O(1)
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            curr = root
            while curr:
                nextLevel = None
                # traverse all nodes of current level
                while curr:
                    if curr.left:
                        # locate the start node of next level
                        if nextLevel is None:
                            nextLevel = curr.left
                        curr.left.next = curr.right

                        if curr.next:
                            curr.right.next = curr.next.left
                    curr = curr.next
                # set current node as the first node of next level
                curr = nextLevel
