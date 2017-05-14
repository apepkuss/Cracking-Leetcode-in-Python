
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
        if not headA or not headB:
            return None

        la = 0  # length of listA
        pa = headA
        while pa:
            la += 1
            pa = pa.next

        lb = 0  # length of listB
        pb = headB
        while pb:
            lb += 1
            pb = pb.next

        pa, pb = headA, headB
        while la > lb:
            la -= 1
            pa = pa.next
        while la < lb:
            lb -= 1
            pb = pb.next

        while pa != pb:
            pa = pa.next
            pb = pb.next

        return pa


if __name__ == "__main__":
    node = ListNode(1)
    headA = node
    headB = node
    res = Solution().getIntersectionNode(headA, headB)
    print res.val
