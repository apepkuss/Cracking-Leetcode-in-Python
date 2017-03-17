

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    @ Amazon, Microsoft, Bloomberg, Yahoo

    Given a linked list, determine if it has a cycle in it.

    Follow up: Can you solve it without using extra space?
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        # use fast and slow pointers to check. If slow pointer meets fast pointer at some node, it means there is a
        # cycle in the linked list.
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        return False