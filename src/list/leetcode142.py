

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return None

        # First, check if a cycle exists in
        # the list.
        p = head.next.next
        q = head.next
        while p!=None and p!=q:
            if p.next!=None and p.next!=None:
                p = p.next.next
                q = q.next
            else:
                return None

        if p==None: return None
        # Second, when p==q, the cycle exists,
        # and from the node where p meets q, move
        # pointer r from the beginning of the list
        # with the same step as q. when r,q meet
        # at some node, the node is just the result.
        r = head
        while r!=q:
            r = r.next
            q = q.next

        return r
