

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    @ Amazon, Linkedin, Apple, Microsoft
    
    Linked List
    
    Merge two sorted linked lists and return it as a new list. The new list 
    should be made by splicing together the nodes of the first two lists.
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(0)
        ptr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                ptr = ptr.next
                l1 = l1.next
            else:
                ptr.next = l2
                ptr = ptr.next
                l2 = l2.next
        if l1:
            ptr.next = l1
        elif l2:
            ptr.next = l2
        return dummy.next
