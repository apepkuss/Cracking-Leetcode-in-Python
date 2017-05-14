
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    @ Amazon
    
    Hash Table, Tree
    
    Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree 
    sum of a node is defined as the sum of all the node values formed by the subtree rooted at 
    that node (including the node itself). So what is the most frequent subtree sum value? If 
    there is a tie, return all the values with the highest frequency in any order.

    Examples 1
    Input:
    
      5
     /  \
    2   -3
    return [2, -3, 4], since all the values happen only once, return all of them in any order.
    Examples 2
    Input:
    
      5
     /  \
    2   -5
    return [2], since 2 happens twice, however -5 only occur once.
    Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
    """
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res

        adict = {}
        self.max_freq = 0
        self.dfs(root, adict)

        for key, value in adict.items():
            if value == self.max_freq:
                res.append(key)

        return res

    def dfs(self, node, adict):
        if not node: return 0

        left = self.dfs(node.left, adict)
        right = self.dfs(node.right, adict)
        asum = node.val + left + right

        if asum not in adict:
            adict[asum] = 1
        else:
            adict[asum] += 1
        # update max frequency
        self.max_freq = max(self.max_freq, adict[asum])
        return asum


