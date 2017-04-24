
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    @ Amazon, Linkedin, Apple, Facebook, Microsoft

    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: The lowest common ancestor is defined 
    between two nodes v and w as the lowest node in T that has both v and w as descendants 
    (where we allow a node to be a descendant of itself).
    """
    def lowestCommonAncestor_recursive(self, root, p, q): # O(n) time, O(1) space
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        # find p or q
        if root == p or root == q:
            return root

        # find p and q on left and right subtrees
        left = self.lowestCommonAncestor_recursive(root.left, p, q)
        right = self.lowestCommonAncestor_recursive(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        else:
            return right

    def lowestCommonAncestor_iterative(self, root, p, q):  # O(n) time, O(n) space
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        queue = [root]
        parent = {root: None}

        # find p and q by BST, as the purpose is to find LOWEST common ancestor
        while p not in parent or q not in parent:
            node = queue.pop(0)
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        ancestors = set()
        # add p and its ancestors in ancestor set
        while p:
            ancestors.add(p)
            p = parent[p]

        # if current q is p's ancestor, then find the target
        while q not in ancestors:
            q = parent[q]

        return q