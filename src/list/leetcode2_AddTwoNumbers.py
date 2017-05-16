
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    @ Amazon, Microsoft, Bloomberg, Airbnb, Adobe

    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
    order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    
    342 + 465 = 807
    
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    """

    def addTwoNumbers(self, l1, l2): # O(n) space
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        if l2 is None: return l1

        h1, h2 = l1, l2
        head = node = ListNode(0)
        carry, remainder, asum = 0, 0, 0

        while h1 or h2 or carry != 0:
            h1_val = h1.val if h1 else 0
            h2_val = h2.val if h2 else 0
            asum = h1_val + h2_val + carry
            carry = asum / 10
            remainder = asum % 10

            node.next = ListNode(remainder)
            node = node.next

            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None

        return head.next


if __name__ == "__main__":
    node0 = ListNode(2)
    node1 = ListNode(4)
    node2 = ListNode(3)
    node0.next = node1
    node1.next = node2

    node3 = ListNode(5)
    node4 = ListNode(6)
    node5 = ListNode(4)
    node3.next = node4
    node4.next = node5

    res = Solution().addTwoNumbers(node0, node3)
    print res