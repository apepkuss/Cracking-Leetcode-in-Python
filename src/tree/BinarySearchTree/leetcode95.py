

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(start, end):
            # left/right subtree is None
            if start>end: return [None]
            res = []
            for rootval in xrange(start, end+1):
                # get all possible left subtrees
                lefttrees = dfs(start, rootval-1)
                # get all possible right subtrees
                righttrees = dfs(rootval+1, end)
                # build up all possible trees
                for lefttree in lefttrees:
                    for righttree in righttrees:
                        root = TreeNode(rootval)
                        root.left = lefttree
                        root.right = righttree
                        res.append(root)
            return res

        if n==0: return []
        return dfs(1,n)
