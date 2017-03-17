

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution(object):
    """
    Given a binary tree, a target node in the binary tree, and an integer value k, print all the nodes
    that are at distance k from the given target node. No parent pointers are available.
    """

    @classmethod
    def find_distanceNode(cls, root, target, k):

        if root is None:
            return -1

        if root == target:
            cls.find_distanceNodeDown(root, k)
            return 0

        # dl is the distance from root to target node, if target node is on the left subtree of root
        dl = cls.find_distanceNode(root.left, target, k)
        if dl != -1:
            if dl+1 == k:
                print root.value
            else:
                # search node on right subtree of root, which has k distance to target node
                cls.find_distanceNodeDown(root.right, k-dl-2)
            return dl+1

        # dr is the distance from root to target node, if target node is on the right subtree of root
        dr = cls.find_distanceNode(root.right, target, k)
        if dr != -1:
            if dr+1 == k:
                print root.value
            else:
                # search node on left subtree of root, which has k distance to target node
                cls.find_distanceNodeDown(root.left, k-dr-2)
            return dr+1

        # target node is not in either left or right subtrees of current root
        return -1

    @classmethod
    def find_distanceNodeDown(cls, root, k):
        """dfs nodes on both left and right subtrees of root, which have k distance to root."""

        if root is None or k<0:
            return

        if k == 0:
            print root.value
            return

        cls.find_distanceNodeDown(root.left, k-1)
        cls.find_distanceNodeDown(root.right, k-1)

