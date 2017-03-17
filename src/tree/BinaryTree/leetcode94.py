

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def inorderTraversal_iterative(self, root): # O(n) time, O(n) space
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res

        stack = []
        while len(stack) > 0 or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

    def inorderTraversal_recursive(self, root): # O(n) time
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res

        # traverse left subtree
        if root.left:
            res += self.inorderTraversal_recursive(root.left)

        # visit root
        res.append(root.val)

        # traverse right subtree
        if root.right:
            res += self.inorderTraversal_recursive(root.right)

        return res

    # Morris traversal without recursion and extra space
    def inorderTraversal_morris(self, root):
        res = []

        if root:
            curr = root
            while curr:
                # print '\n'
                # print str(curr.val) + '(current)'
                if not curr.left:
                    # print str(curr.val) + " has no left subtree."
                    res.append(curr.val)
                    # print curr.val
                    curr = curr.right
                else:
                    # print str(curr.val) + " l-> " + str(curr.left.val)
                    # find the inorder successor
                    pre = curr.left
                    while pre.right and pre.right != curr:
                        # condition1 pre.right: used to find the predecessor of current
                        # condition2 pre.right != curr: used to recover the predecessor's right link
                        # print str(pre.val) + ' r-> ' + str(pre.right.val)
                        pre = pre.right

                    if pre.right is None:
                        # make the current node as right child of its inorder predecessor
                        pre.right = curr
                        # print str(pre.val) + " r-> " + str(curr.val) + '(current).'
                        curr = curr.left
                    else:
                        # print str(pre.val) + ' r-> ' + str(curr.val)
                        # revert the changes made and fix the right child of predecessor
                        pre.right = None
                        # print 'remove the link: ' + str(pre.val) +' r-> ' + str(curr.val)
                        res.append(curr.val)
                        # print curr.val
                        curr = curr.right

        return res

if __name__ == "__main__":
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root.left, root.right = node2, node3

    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2.left, node2.right = node4, node5

    res = Solution().inorderTraversal_morris(root)
    print res

