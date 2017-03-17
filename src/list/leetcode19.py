

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None or (head.next is None and n == 1):
            return None

        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        step = 0
        while step < n and fast:
            fast = fast.next
            step += 1

        if fast is None:
            return dummy.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
