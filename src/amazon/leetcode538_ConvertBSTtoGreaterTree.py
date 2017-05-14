
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    @ Amazon
    
    Tree
    
    Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

    Example:
    
    Input: The root of a Binary Search Tree like this:
                  5
                /   \
               2     13
    
    Output: The root of a Greater Tree like this:
                 18
                /   \
              20     13
    """
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right):
            return root

        rsum = self.dfs(root.right, 0)
        root.val += rsum
        self.dfs(root.left, root.val)

        return root

    def dfs(self, node, asum):
        if not node:
            return asum

        if not node.left and not node.right:
            node.val += asum
            return node.val

        # update right subtree
        asum = self.dfs(node.right, asum)
        node.val += asum
        # update left subtree
        return self.dfs(node.left, node.val)



