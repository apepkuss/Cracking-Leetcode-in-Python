

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def findSwapNodes(root):
            # in-order traverse the binary tree
            if root:
                findSwapNodes(root.left)
                if self.pre and self.pre.val > root.val:
                    self.node2 = root
                    if self.node1 is None:
                        self.node1 = self.pre
                self.pre = root
                findSwapNodes(root.right)

        self.node1, self.node2, self.pre = None, None, None
        findSwapNodes(root)
        # swap two nodes
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
