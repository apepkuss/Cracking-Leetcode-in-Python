

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums): # RT: O(n)
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        start,end = 0, len(nums)-1
        if start > end: return None
        if start == end: return TreeNode(nums[start])
        mid = (start+end)/2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[start:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
