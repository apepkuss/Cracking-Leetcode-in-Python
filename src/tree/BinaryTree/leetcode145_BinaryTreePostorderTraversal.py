

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    Tree, Stack

    Given a binary tree, return the postorder traversal of its nodes' values.

    For example:
    Given binary tree {1,#,2,3},
       1
        \
         2
        /
       3
    return [3,2,1].

    Note: Recursive solution is trivial, could you do it iteratively?
    """
    def postorderTraversal_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res

        pre = None
        stack = [root]
        while len(stack) > 0:
            curr = stack[-1]
            if (curr.left is None and curr.right is None) or (pre and (pre == curr.left or pre == curr.right)):
                res.append(curr.val)
                pre = stack.pop()
            else:
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
        return res

    def postorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res

        if root.left:
            res += self.postorderTraversal_recursive(root.left)
        if root.right:
            res += self.postorderTraversal_recursive(root.right)
        res.append(root.val)

        return res