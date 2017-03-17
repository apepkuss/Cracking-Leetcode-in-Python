

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):  # RT: O(n)
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        fast = head
        n = 1
        # compute the length of the linked list
        while fast.next:
            fast = fast.next
            n += 1

        k = k % n
        slow = fast = head
        step = 0
        while step < k:
            fast = fast.next
            step += 1

        while fast.next:
            fast = fast.next
            slow = slow.next

        fast.next = head
        head = slow.next
        slow.next = None
        return head
