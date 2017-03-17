

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    """
    @ Amazon, Microsoft, Bloomberg, Uber

    Hash Table, LinkedList

    A linked list is given such that each node contains an additional random pointer which could point
    to any node in the list or null.

    Return a deep copy of the list.
    """
    def copyRandomList(self, head): # RT: O(n)
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None: return head

        # copy every existed node in the original
        # list and insert the copy node into the list
        # just next to the original node.
        # before: 1->2->3->4
        # after:  1->1->2->2->3->3->4->4
        p = head
        while p:
            node = RandomListNode(p.label)
            node.next = p.next
            p.next = node
            p = node.next

        # deal with the random pointers
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        # separate the copy list from the
        # the hybrid list, and recover the
        # original list
        dummy = RandomListNode(0)
        dummy.next = head.next
        q = dummy
        p = head
        while p:
            q.next = p.next
            p.next = p.next.next
            q = q.next
            p = p.next

        return dummy.next
