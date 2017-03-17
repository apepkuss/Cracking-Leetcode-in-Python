
import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    @ Linkedin, Google, Uber, Airbnb, Facebook, Twitter, Amazon, Microsoft

    Divide and Conquer, Linked List, Heap

    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
    """
    def mergeKLists(self, lists): # use min heap
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        arr = []
        for alist in lists:
            if alist:
                arr.append(alist)
        arr = self.buildMinHeap(arr)
        dummy = ListNode(0)
        p = dummy
        while len(arr) > 0:
            p.next, arr = self.heappop(arr)
            p = p.next
        return dummy.next

    def buildMinHeap(self, arr):
        """
        Build up a min heap
        :param arr:
        :return:
        """
        i = (len(arr) - 1) / 2
        while i >= 0:
            arr = self.heapify(arr, i)
            i -= 1
        return arr

    def heapify(self, arr, i):
        """
        Heapify an existing array
        :param arr:
        :param i:
        :return:
        """
        left = 2 * i + 1
        rite = 2 * i + 2
        minimum = i
        if left < len(arr) and arr[left].val < arr[minimum].val:
            minimum = left
        if rite < len(arr) and arr[rite].val < arr[minimum].val:
            minimum = rite
        if minimum != i:
            arr[i], arr[minimum] = arr[minimum], arr[i]
            self.heapify(arr, minimum)
        return arr

    def heappop(self, arr):
        """
        Pop out the minimum node
        :param arr:
        :return:
        """
        if len(arr) == 0:
            return None
        node = arr[0]
        if node.next:
            arr[0] = node.next
            arr = self.heapify(arr, 0)
        elif len(arr) > 1:
            arr[0] = arr[-1]
            arr = self.heapify(arr[:len(arr) - 1], 0)
        elif len(arr) > 0:
            arr = []
        return node, arr
