

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        dummy = ListNode(0)
        dummy.next = head
        ghead = gtail = ListNode(0)
        ltail = dummy
        p = dummy.next
        while p:
            if p.val < x:
                ltail.next = p
                p = p.next
                ltail = ltail.next
            else:
                gtail.next = p
                p = p.next
                gtail = gtail.next
        ltail.next = ghead.next
        gtail.next = None
        return dummy.next