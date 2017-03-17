
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    @ Uber, Facebook, Twitter, Zenefits, Amazon, Microsoft, Snapchat, Apple, Yahoo, Bloomberg, Yelp, Adobe

    Reverse a singly linked list.

    Analysis: If the question requires to reverse a part of the linked list from i to j, a dummy node should be
    created for a generic solution. But, for reversing the whole linked list, it is not necessary.
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        pre, curr = head, head.next
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        head.next = None
        head = pre
        return head