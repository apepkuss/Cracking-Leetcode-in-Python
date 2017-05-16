
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    @ Microsoft, Bloomberg,
    
    Linked List
    
    You are given two non-empty linked lists representing two non-negative integers. The most 
    significant digit comes first and each of their nodes contain a single digit. Add the two 
    numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    
    Follow up:
    What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
    
    Example:
    
    Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 8 -> 0 -> 7
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1

        dummy = ListNode(0)

        # compute the sizes of l1 and l2, respectively
        size1 = self.get_size(l1)
        size2 = self.get_size(l2)

        # case 1: the sizes of l1 and l2 are same
        if size1 == size2:
            carry = self.get_sum(l1, l2, dummy)
            if carry:
                node = ListNode(carry)
                node.next = dummy.next
                dummy.next = node

        # case 2: the sizes are different
        else:
            if size1 < size2:
                l1, l2 = l2, l1
                size1, size2 = size2, size1
            diff = size1 - size2
            p = l1
            while diff > 1:
                p = p.next
                diff -= 1
            tail = p
            p = p.next
            tail.next = None

            # add l2 and right sub-list of l1
            carry = self.get_sum(p, l2, dummy)

            # add carry and left sub-list of l1
            carry = self.add(l1, carry)
            if carry:
                node = ListNode(carry)
                node.next = l1
                l1 = node

            tail.next = dummy.next
            dummy.next = l1

        return dummy.next

    def get_size(self, alist):
        p = alist
        size = 0
        while p:
            size += 1
            p = p.next
        return size

    def get_sum(self, l1, l2, dummy):
        if not l1.next and not l2.next:
            val = l1.val + l2.val
        else:
            carry = self.get_sum(l1.next, l2.next, dummy)
            val = l1.val + l2.val + carry

        carry = val / 10
        node = ListNode(val % 10)
        node.next = dummy.next
        dummy.next = node
        return carry

    def add(self, l1, val):
        if not l1.next:
            asum = l1.val + val
        else:
            carry = self.add(l1.next, val)
            asum = l1.val + carry

        l1.val = asum % 10
        carry = asum / 10
        return carry


def build_list(nums):
    dummy = ListNode(0)
    p = dummy
    for num in nums:
        p.next = ListNode(num)
        p = p.next
    return dummy.next


def print_list(head):
    res = []
    p = head
    while p:
        res.append(p.val)


if __name__ == "__main__":
    nums1 = [0]
    nums2 = [2,7,8]
    l1 = build_list(nums1)
    l2 = build_list(nums2)
    head = Solution().addTwoNumbers(l1, l2)
    print_list(head)



