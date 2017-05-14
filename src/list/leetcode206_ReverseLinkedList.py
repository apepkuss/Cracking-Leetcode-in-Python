
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    @ Uber, Facebook, Twitter, Zenefits, Amazon, Microsoft, Snapchat, Apple, Yahoo, Bloomberg, Yelp, Adobe
    
    Linked List, DFS

    Reverse a singly linked list.

    Analysis: If the question requires to reverse a part of the linked list from i to j, a dummy node should be
    created for a generic solution. But, for reversing the whole linked list, it is not necessary.
    """

    # Solution based on iterative design
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre, curr = head, head.next
        while curr:
            node = curr.next
            curr.next = pre
            pre = curr
            curr = node

        head.next = None
        return pre

    # Solution based on recursive design
    def reverseList_DFS(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        head, _ = self.dfs_reverse(head)
        return head

    def dfs_reverse(self, head):
        # base case
        if not head or not head.next:
            return head, head

        tail = head.next
        head.next = None
        newhead, newtail = self.dfs_reverse(tail)
        newtail.next = head
        newtail = head

        return newhead, newtail

