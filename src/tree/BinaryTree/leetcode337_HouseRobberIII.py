
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    @ Uber

    The thief has found himself a new place for his thievery again. There is only one entrance to this area,
    called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart
    thief realized that "all houses in this place forms a binary tree". It will automatically contact the police
    if two directly-linked houses were broken into on the same night.

    Determine the maximum amount of money the thief can rob tonight without alerting the police.
    """
    def rob_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if root is None:
                return 0,0
            robLeft = dfs(root.left)
            robRight = dfs(root.right)
            norobCurr = robLeft[1] + robRight[1]
            robCurr = max(robLeft[0]+robRight[0]+root.val, norobCurr)
            return norobCurr, robCurr
        return dfs(root)[1]

    def rob_memorization(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, path):
            if root is None: return 0
            if path not in adict:
                left, right = root.left, root.right
                ll = lr = rl = rr = None
                if left: ll, lr = left.left, left.right
                if right: rl, rr = right.left, right.right
                norobCurr = dfs(left, path + 'l') + dfs(right, path + 'r')
                robCurr = root.val + dfs(ll, path + 'll') + dfs(lr, path + 'lr') + dfs(rl, path + 'rl') + dfs(rr,
                                                                                                              path + 'rr')
                adict[path] = max(norobCurr, robCurr)
            return adict[path]

        adict = {}
        return dfs(root, '')


if __name__ == "__main__":
    root = TreeNode(5)
    node1 = TreeNode(4)
    node2 = TreeNode(7)
    node3 = TreeNode(1)
    node4 = TreeNode(2)
    node5 = TreeNode(1)
    node6 = TreeNode(10)
    node7 = TreeNode(3)
    node8 = TreeNode(8)

    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node4.right = node7
    node5.left = node8

    res = Solution().rob_dfs(root)
    print res

