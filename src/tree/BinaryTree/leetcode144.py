

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def preorderTraversal_iterative(self, root):  # O(n) time, O(n) space
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
        stack = [root]
        while stack != []:
            node = stack.pop()
            res += [node.val]
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return res

    def preorderTraversal_recursive(self, root):  # O(n) time
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None: return res

        # root
        res += [root.val]
        # left subtree
        if root.left is not None:
            res += self.preorderTraversal_recursive(root.left)
        # right subtree
        if root.right is not None:
            res += self.preorderTraversal_recursive(root.right)

        return res
