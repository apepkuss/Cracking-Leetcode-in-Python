
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def sortedListToBST_ListtoArray(self, head): # RT: O(n), Space: O(n)
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head== None:
            return None

        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next

        return self.sortedArrayToBST(sorted(nums))

    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) / 2 == 0:
            index = len(nums) / 2 - 1
        else:
            index = len(nums) / 2
        root = TreeNode(nums[index])
        root.left = self.sortedArrayToBST(nums[:index])
        root.right = self.sortedArrayToBST(nums[index + 1:])

        return root

    def sortedListToBST(self, head):  # RT: O(n), Space: O(n)
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def buildBST(node):
            if node is None:
                return None
            if node.next is None:
                return TreeNode(node.val)
            dummy = ListNode(0)
            dummy.next = node
            pre, slow, fast = dummy, node, node
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                pre = pre.next
            pre.next = None
            root = TreeNode(slow.val)
            root.left = buildBST(node)
            root.right = buildBST(slow.next)
            return root

        return buildBST(head)

if __name__ == "__main__":
    nums = [1, 3]
    dummy = ListNode(0)
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next

    mysolution = Solution()
    res = mysolution.sortedListToBST(dummy.next)
    print res