

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    @ Bloomberg, Uber, Google
    
    Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
    Note: You may assume k is always valid, 1 <= k <= BST's total elements.
    """
    def kthSmallest(self, root, k): # O(n) time, O(n) space)
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while len(stack)>0 or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k-=1
                if k==0: return root.val
                root = root.right