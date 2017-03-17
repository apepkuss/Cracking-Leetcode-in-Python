import unittest


class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class PalindromeChecker(object):

    @classmethod
    def isPalindrome_Stack(cls, head):  # O(n) time, O(n) space
        """
        Check if a singly linked list is a palindrome
        :param head: the head node of the linked list
        :return: True, if the linked list is a palindrome; False, otherwise.
        """
        if head is None or head.next is None:
            return True

        stack = []
        ptr = head
        while ptr:
            stack.append(ptr)
            ptr = ptr.next

        ptr = head
        while len(stack) > 0 and ptr:
            node = stack.pop()
            if not cls.isPalindrome(node.value, ptr.value):
                return False
            ptr = ptr.next
        return True

    @classmethod
    def isPalindrome_Reverse(cls, head):  # O(n) time, O(1) space
        """
        Check if a singly linked list is palindromic by reversing second half of the linked list
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return True

        dummy = ListNode("")
        dummy.next = head
        fast = slow = dummy
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next is None:
            dummy_mid = ListNode("")
            dummy_mid.next = slow.next
            slow.next = dummy_mid
            new_head = cls.reverse_linkedlist(dummy_mid)
        else:
            new_head = cls.reverse_linkedlist(slow.next)

        while True:
            if cls.isPalindrome(head.value, new_head.value):
                head = head.next
                new_head = new_head.next
            if head == new_head:
                if cls.isPalindrome(head.value):
                    return True
                else:
                    return False
            if (head.next is None and new_head.next) or (head.next and new_head.next is None):
                return False

    @classmethod
    def isPalindrome(cls, first, second=None):
        if second:
            if len(first) != len(second):
                return False
            return first == second[::-1]
        else:
            return first == first[::-1]

    @classmethod
    def reverse_linkedlist(cls, head):
        pre, curr = head, head.next
        pre.next = None
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre


class TestRun(unittest.TestCase):

    def test_oddNodes(self):
        arr = ["abb", "aba", "bab", "aba", "bba"]
        head = self.build_linkedlist(arr)
        res = PalindromeChecker.isPalindrome_Stack(head)
        unittest.TestCase.assertTrue(self, res)
        res = PalindromeChecker.isPalindrome_Reverse(head)
        unittest.TestCase.assertTrue(self, res)

    def test_evenNodes(self):
        arr = ["abb", "aba", "bab", "bab", "aba", "bba"]
        head = self.build_linkedlist(arr)
        res = PalindromeChecker.isPalindrome_Stack(head)
        unittest.TestCase.assertTrue(self, res)
        res = PalindromeChecker.isPalindrome_Reverse(head)
        unittest.TestCase.assertTrue(self, res)

    def build_linkedlist(self, arr):
        if arr is None or len(arr)==0:
            return None
        head = ptr = None
        for value in arr:
            if ptr is None:
                ptr = ListNode(value)
                head = ptr
            else:
                ptr.next = ListNode(value)
                ptr = ptr.next
        return head

if __name__ == "__main__":
    unittest.main()