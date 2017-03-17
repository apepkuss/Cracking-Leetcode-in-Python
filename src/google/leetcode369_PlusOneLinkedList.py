
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    @ Google
    Given a non-negative number represented as a singly linked list of digits, plus one to the number.

    The digits are stored such that the most significant digit is at the head of the list.

    Example:
        Input:
        1->2->3

        Output:
        1->2->4
    """
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = ListNode(1)
        dummy.next = head

        parent = {head :None}
        p = head
        while p.next:
            parent[p.next] = p
            p = p.next

        carry = (p.val + 1) / 10
        p.val = (p.val + 1) % 10
        while carry and parent[p]:
            p = parent[p]
            asum = p.val + carry
            carry = asum / 10
            p.val = asum % 10
        if carry == 0:
            return dummy.next
        elif parent[p] is None:
            return dummy


