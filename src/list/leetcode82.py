

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates_twoPointers(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre, curr = dummy, head.next
        while curr:
            if pre.next.val != curr.val:
                pre = pre.next
                curr = curr.next
            else:
                while curr and pre.next.val == curr.val:
                    curr = curr.next
                pre.next = curr
                if curr:
                    curr = curr.next
        return dummy.next

    def deleteDuplicates_threePointers(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre, curr, next = dummy, head, head.next
        while next:
            if curr.val != next.val:
                pre = curr
                curr = next
                next = next.next
            else:
                while next and next.val == curr.val:
                    next = next.next
                curr = next
                pre.next = curr
                if next:
                    next = next.next
                else:
                    break
        return dummy.next
