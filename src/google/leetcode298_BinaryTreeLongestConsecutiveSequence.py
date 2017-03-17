
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @ Google

    Given a binary tree, find the length of the longest consecutive sequence path.

    The path refers to any sequence of nodes from some starting node to any node in the tree along the
    parent-child connections. The longest consecutive path need to be from parent to child (cannot be
    the reverse).

    For example,
       1
        \
         3
        / \
       2   4
            \
             5
    Longest consecutive sequence path is 3-4-5, so return 3.
       2
        \
         3
        /
       2
      /
     1
    Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
    """
    def longestConsecutive_GlobalVariable(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, length):
            if root.left:
                if root.left.val == root. val +1:
                    dfs(root.left, length+ 1)
                    self.maxlen = max(self.maxlen, length + 1)
                else:
                    dfs(root.left, 1)
            if root.right:
                if root.right.val == root.val + 1:
                    dfs(root.right, length + 1)
                    self.maxlen = max(self.maxlen, length + 1)
                else:
                    dfs(root.right, 1)

        self.maxlen = 1
        if root is None:
            return 0
        dfs(root, 1)
        return self.maxlen

    def longestConsecutive_NoGlobalVariable(self, root):
        def dfs(root, parent, lc):
            if root is None:
                return lc
            llc, rlc = 0, 0
            if parent and parent.val + 1 == root.val:
                llc = dfs(root.left, root, lc + 1)
                rlc = dfs(root.right, root, lc + 1)
            else:
                llc = max(lc, dfs(root.left, root, 1))
                rlc = max(lc, dfs(root.right, root, 1))
            return max(llc, rlc)

        res = 0
        if root is None:
            return res
        return dfs(root, None, 0)