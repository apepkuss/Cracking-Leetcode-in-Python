
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    @ Amazon, Microsoft, Bloomberg, Airbnb

    Write a program to find the node at which the intersection of two singly linked lists begins.


    For example, the following two linked lists:

    A:           a1 -> a2
                        \
                         c1 -> c2 > c3
                        /
    B:     b1 -> b2 -> b3
    begin to intersect at node c1.


    Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
    """
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None

        p, q = headA, headB
        while p and q:
            # two linked lists have the same number of nodes
            if p.val == q.val:
                return p
            p = p.next
            q = q.next

        # if list A has less nodes
        if not p:
            p = headB
            while p and q:
                p = p.next
                q = q.next
            q = headA

        # if list B has less nodes
        elif not q:
            q = headA
            while p and q:
                p = p.next
                q = q.next
            p = headB

        while p and q:
            if p.val == q.val:
                return p
            p = p.next
            q = q.next

        return None


if __name__ == "__main__":
    node = ListNode(1)
    headA = node
    headB = node
    res = Solution().getIntersectionNode(headA, headB)
    print res.val
