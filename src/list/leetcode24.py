

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs_swapvalues(self, head):
        if head == None or head.next == None: return head
        p, q = head, head.next
        while True:
            p.val, q.val = q.val, p.val
            if q.next == None or q.next.next == None: break
            p = q.next
            q = p.next
        return head

    def swapPairs_swapnodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy.next

        while fast and fast.next:
            fast = fast.next

            # swap a node pair
            slow.next.next = fast.next
            fast.next = slow.next
            slow.next = fast

            # move fast and slow pointers to next position
            fast = fast.next.next
            slow = slow.next.next

        return dummy.next
