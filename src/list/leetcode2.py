

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    @ Amazon, Microsoft, Bloomberg, Airbnb, Adobe
    """
    def addTwoNumbers(self, l1, l2):  # RT: O(max(len(l1),len(l2)))
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1

        h1 = l1; h2 = l2
        while h1!=None and h2!=None:
            h1 = h1.next
            h2 = h2.next
        if h2!=None: l1,l2 = l2,l1

        head = l1
        carry = 0
        while l2!=None:
            asum = l1.val + l2.val + carry
            l1.val = asum%10
            carry = asum/10
            # l1 and l2 have same size
            if l2.next is None and l1.next is None and carry==1:
                l1.next = ListNode(carry)
                carry = 0
            l1 = l1.next
            l2 = l2.next

        while carry==1 and l1:
            asum = carry + l1.val
            l1.val = asum%10
            carry = asum/10
            if l1.next is None and carry==1:
                l1.next = ListNode(carry)
                break
            l1 = l1.next
        return head
