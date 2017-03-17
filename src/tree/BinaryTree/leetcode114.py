

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten_recursive(self, root):  # O(1) space
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def do_flat(root):
            if root.left is None and root.right is None:
                return root
            elif root.right is None:
                left_flatten = do_flat(root.left)
                root.right = left_flatten
                root.left = None
                return root
            elif root.left is None:
                right_flatten = do_flat(root.right)
                root.right = right_flatten
                return root
            else:
                left_flatten = do_flat(root.left)
                right_flatten = do_flat(root.right)
                leaf = left_flatten
                while leaf.right is not None:
                    leaf = leaf.right
                leaf.right = right_flatten
                root.right = left_flatten
                root.left = None
                return root

        if root is not None:
            do_flat(root)

    def flatten_iterative(self, root):  # O(n) space
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        p = root
        stack = []
        while p:
            if p.left==None and p.right==None:
                if stack!=[]:
                    p.right = stack.pop()
                    p = p.right
                else: break
            elif p.left and p.right:
                stack.append(p.right)
                p.right = p.left
                p.left = None
                p = p.right
            elif p.left:
                p.right = p.left
                p.left = None
                p = p.right
            elif p.right:
                p = p.right
