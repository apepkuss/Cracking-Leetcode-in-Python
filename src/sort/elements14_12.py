import unittest


class ListNode(object):

    def __init__(self, value):
        self.value = value
        self.original_order = -1
        self.next = None


class Elements(object):
    """
    elements 14.12 Implement a fast sorting algorithm for linked lists

    Implement a routine which sorts lists efficiently. It should be a stable sort, i.e., the relative
    positions of equal elements must remain unchanged.
    """

    @classmethod
    def sort_list(cls, head):
        # base case
        if head is None or head.next is None:
            return head

        # recursive step
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        new_head = slow.next
        slow.next = None

        # split a linked list into two sub-lists, then recursively sort these two sub-lists
        first_head = cls.sort_list(head)
        second_head = cls.sort_list(new_head)

        # merge two sorted sub-lists into a single sorted linked list
        dummy = ListNode(0)
        head = dummy
        while first_head and second_head:
            if first_head.value <= second_head.value:
                head.next = first_head
                first_head = first_head.next
            else:
                head.next = second_head
                second_head = second_head.next
            head = head.next

        if first_head:
            head.next = first_head
        elif second_head:
            head.next = second_head

        return dummy.next


class TestRun(unittest.TestCase):

    def test_case1(self):
        nums = [3,2,1,2,5,4,5,7,1,1,3,8]
        dummy = ListNode(0)
        head = dummy
        for i in nums:
            head.next = ListNode(i)
            head.next.original_order = i
            head = head.next

        res = []
        head = Elements.sort_list(dummy.next)

        keep_original_order = True
        while head and head.next:
            if head.value == head.next.value and head.original_order > head.next.original_order:
                keep_original_order = False
                break
            head = head.next

        unittest.TestCase.assertTrue(self, keep_original_order)


if __name__ == "__main__":
    unittest.TestCase.main()


