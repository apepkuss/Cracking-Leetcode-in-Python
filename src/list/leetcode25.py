

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        while fast:
            # fix a k-size range to reverse
            step = 0
            while step < k - 1 and fast:
                fast = fast.next
                step += 1

            if fast is None: return dummy.next

            # reverse the node in k-group
            headptr, pre, curr, nextptr = slow.next, slow.next, slow.next.next, slow.next.next.next
            while pre != fast:
                curr.next = pre
                pre = curr
                curr = nextptr
                if nextptr is not None:
                    nextptr = nextptr.next
            slow.next.next = curr
            slow.next = pre

            # move slow and fast points
            slow = headptr
            fast = curr

        return dummy.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    head = node1
    node1.next = node2

    mysolution = Solution()
    result = mysolution.reverseKGroup(head, 2)
    print result
