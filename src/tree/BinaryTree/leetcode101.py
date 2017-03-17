

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric_iterative(self, root):
        if root is None:
            return True

        lqueue = [root.left]
        rqueue = [root.right]
        while len(lqueue) > 0 and len(rqueue) > 0:
            root1, root2 = lqueue.pop(0), rqueue.pop(0)
            if root1 is None and root2 is None:
                continue
            elif root1 and root2 and root1.val == root2.val:
                lqueue.append(root1.left)
                rqueue.append(root2.right)

                lqueue.append(root1.right)
                rqueue.append(root2.left)
            else:
                return False
        return True

    def isSymmetric_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkSymmetry(root1, root2):
            if root1 is None:
                return root2 is None
            if root2 is None:
                return False
            if root1.val == root2.val:
                return checkSymmetry(root1.left, root2.right) and checkSymmetry(root1.right, root2.left)
            else:
                return False

        if root is None:
            return True
        return checkSymmetry(root.left, root.right)
