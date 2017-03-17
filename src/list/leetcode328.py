

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        oddPtr = head
        evenHead = evenPtr = head.next
        while oddPtr and evenPtr:
            if evenPtr.next:
                oddPtr.next = evenPtr.next
                oddPtr = oddPtr.next
            if evenPtr.next:
                evenPtr.next = evenPtr.next.next
            evenPtr = evenPtr.next
        oddPtr.next = evenHead
        return head