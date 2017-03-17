

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None: return
        dummy = ListNode(0)
        dummy.next = head
        # divide the original list into two parts
        slow = fast = dummy
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next is None: # has even nodes
            head2 = slow.next
            tail1 = slow
        elif fast.next.next is None: # has odd nodes
            head2 = slow.next.next
            tail1 = slow.next
        tail1.next = None

        # reverse the second half part
        pre, curr = head2, head2.next
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        head2.next = None
        head2 = pre

        # merge two parts
        p = head
        while head2:
            tmp = head2.next
            head2.next = p.next
            p.next = head2
            p = head2.next
            head2 = tmp
