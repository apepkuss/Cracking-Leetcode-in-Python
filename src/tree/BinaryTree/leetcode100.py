

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree_iterative(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None:
            return q is None
        if q is None:
            return p is None
        stack = [(p,q)]
        while len(stack) > 0:
            root1, root2 = stack.pop()
            if root1 is None and root2 is None:
                continue
            elif root1 and root2 and root1.val == root2.val:
                stack.append((root1.left, root2.left))
                stack.append((root1.right, root2.right))
            else:
                return False
        return True

    def isSameTree_recursive(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None:
            return q is None
        if q is None:
            return False
        if p.val == q.val:
            return self.isSameTree_recursive(p.left, q.left) and self.isSameTree_recursive(p.right, q.right)
        else:
            return False
