# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    @ Amazon

    You need to construct a binary tree from a string consisting of parenthesis and integers.

    The whole input represents a binary tree. It contains an integer followed by zero, one or
    two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis
    contains a child binary tree with the same structure.

    You always start to construct the left child node of the parent first if it exists.

    Example:
    Input: "4(2(3)(1))(6(5))"
    Output: return the tree root node representing the following tree:

           4
         /   \
        2     6
       / \   /
      3   1 5
    Note:
    There will only be '(', ')', '-' and '0' ~ '9' in the input string.
    An empty tree is represented by "" instead of "()".
    """
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s is None: return None
        n = len(s)
        nums = '0123456789'
        stack = []
        i = 0
        while i < n:
            c = s[i]
            # if c is a number or negative notation
            if c in nums or c == '-':
                j = i
                while i + 1 < n and s[i + 1] in nums:
                    i += 1
                val = int(s[j:i+1])
                currNode = TreeNode(val)
                if stack:
                    parent = stack[-1]
                    if parent.left:
                        parent.right = currNode
                    else:
                        parent.left = currNode
                stack.append(currNode)

            # else if c is right bracket
            elif c == ')':
                stack.pop()
            i += 1

        return stack[-1] if stack else None

if __name__ == "__main__":
    s = "4(2(3)(1))(6(5))"
    res = Solution().str2tree(s)
    print res.val