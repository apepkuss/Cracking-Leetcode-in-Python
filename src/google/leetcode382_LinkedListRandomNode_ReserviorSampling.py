
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import random

class Solution(object):
    """
    @ Google

    Given a singly linked list, return a random node's value from the linked list. Each node must have the same
    probability of being chosen.

    Follow up:
    What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently
    without using extra space?

    Reference:
        1. Reservoir Sampling: http://www.geeksforgeeks.org/reservoir-sampling/
        2. Wikipedia: https://en.wikipedia.org/wiki/Reservoir_sampling
    """
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        # method1
        # self.nodes = []
        # while head:
        #     self.nodes.append(head)
        #     head = head.next

        # method2
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        # method1
        # idx = random.randint(0, len(self.nodes)-1)
        # return self.nodes[idx].val

        # method2: Reservoir sampling algorithm
        pool = self.head.val
        curr = self.head.next
        count = 1
        while curr:
            if random.randint(0, count) == 0:
                pool = curr.val
            curr = curr.next
            count += 1
        return pool