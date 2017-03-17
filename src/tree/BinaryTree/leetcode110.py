

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        def helper(root):
            if root is None:
                return True, 0

            # check left subtree
            left = helper(root.left)
            if left[0] == False:
                return False, -1

            # check right subtree
            right = helper(root.right)
            if right[0] == False:
                return False, -1

            # check if the depths of the two subtrees
            # differ by more than 1
            if abs(left[1]-right[1]) <= 1:
                return True, 1+max(left[1], right[1])
            else:
                return False, -1
        return helper(root)[0]
