
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    @ Microsoft, Baidu

    DFS

    Given a binary tree, find the maximum path sum.

    For this problem, a path is defined as any sequence of nodes from some starting
    node to any node in the tree along the parent-child connections. The path must
    contain at least one node and does not need to go through the root.

    For example:
    Given the below binary tree,

           1
          / \
         2   3
    Return 6.
    """

    # For each node, there can be four ways that the max path goes through the node
    # 1. the node only
    # 2. max path through left child + the node
    # 3. max path through right child + the node
    # 4. max path through left child + the node + right child
    #
    # Therefore, the idea is to keep track of four paths and pick up the max one in
    # the end. One more thing to be noticed is root of every subtree need to return
    # maximum path sum such that at most one child of root is involved. This is needed
    # for parent function call.
    #

    def maxPathSum_node2node(self, root):
        """
<<<<<<< HEAD
        Compute the maximum node-to-node path sum
=======
        Maximum sum path from node to node
>>>>>>> 829ce7e... 1. update 28 KMP;
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node is None:
                return 0

            lmax = dfs(node.left)
            rmax = dfs(node.right)

            # max_single represents max path for parent function call. The path must
            # include at most one child of the root
            max_single = max(lmax + node.val, rmax + node.val, node.val)

            # max_top represents the sum when the max path is the fourth way
            max_top = max(max_single, lmax + rmax + node.val)

            # store current max sum after considering the four ways
            self.max = max(self.max, max_top)

            return max_single

        if root is None: return 0
        import sys
        self.max = -sys.maxint - 1
        dfs(root)
        return self.max

    def maxPathSum_root2leaf(self, root):
<<<<<<< HEAD
        """Compute the maximum root-to-leaf path sum"""
=======
>>>>>>> 829ce7e... 1. update 28 KMP;

        def dfs(node):
            if node is None:
                return 0

            # node is a leaf
            if node.left is None and node.right is None:
                return node.val

            ls = dfs(node.left)
            rs = dfs(node.right)

            return max(ls, rs) + node.val

        if root is None:
            return 0

        return dfs(root)

    def maxPathSum_leaf2leaf(self, root):
<<<<<<< HEAD
        """Compute the maximum leaf-to-leaf path sum"""
=======
>>>>>>> 829ce7e... 1. update 28 KMP;

        def dfs(node):
            if node is None:
                return 0

            # node is a leaf
            if node.left is None and node.right is None:
                return node.val

            ls = dfs(node.left)
            rs = dfs(node.right)

<<<<<<< HEAD
            # if node.left and node.right:
            #     self.max = max(self.max, ls + rs + node.val)
            #     # return the max sum for parent function call, which includes only
            #     # one child of node
            #     return max(ls, rs) + node.val
            # elif node.left:
            #     # no need to update self.max because we just need leaf to leaf sum
            #     return ls + node.val
            # else:
            #     return rs + node.val

            self.max = max(self.max, ls + rs + node.val)
            return max(ls, rs) + node.val
=======
            if node.left and node.right:
                self.max = max(self.max, ls + rs + node.val)
                # return the max sum for parent function call, which includes only
                # one child of node
                return max(ls, rs) + node.val
            elif node.left:
                # no need to update self.max because we just need leaf to leaf sum
                return ls + node.val
            else:
                return rs + node.val
>>>>>>> 829ce7e... 1. update 28 KMP;


        import sys
        self.max = -sys.maxint - 1
        dfs(root)
        return self.max