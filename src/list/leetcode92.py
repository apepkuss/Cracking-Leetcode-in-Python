

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if head==None or head.next==None: return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        for x in xrange(m-1):
            p = p.next
        q = p.next # q is the m-th node
        r = q.next
        for x in xrange(m, n):
            tmp = r.next
            r.next = q
            q = r
            r = tmp
        p.next.next = r
        p.next = q
        return dummy.next
