
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    @ Amazon, Linkedin, Apple, Microsoft

    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
    the nodes of the first two lists.
    """
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        p = dummy

        # merger l1 and l2
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        # if l1 has more nodes than l2
        if l1: p.next = l1

        # if l2 has more nodes than l1
        if l2: p.next = l2

        return dummy.next