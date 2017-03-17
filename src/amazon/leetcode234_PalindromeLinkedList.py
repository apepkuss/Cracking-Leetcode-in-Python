

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    @ Amazon, Facebook

    Given a singly linked list, determine if it is a palindrome.

    Follow up: Could you do it in O(n) time and O(1) space?

    Use fast and slow pointers to get the center of the list, then reverse the second part of the list;
    then compare the two sub-lists.

    """
    def isPalindrome(self, head): # O(n) time, O(1) space
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        # find list center
        fast, slow = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        secondHead = slow.next
        slow.next = None

        # reverse second part of the list
        p1 = secondHead
        p2 = p1.next

        while p1 and p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp

        secondHead.next = None

        # compare two sublists
        p = p2 if p2 else p1
        q = head
        while p:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True

