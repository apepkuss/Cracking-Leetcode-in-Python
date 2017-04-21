

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    @ Adobe, Apple, Microsoft
    
    Linked List
    
    Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

    Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list 
    should become 1 -> 2 -> 4 after calling your function.
    """

    # The interesting part of this problem is the root node is not given, but the target node is given. Therefore,
    # node deletion operation can be implemented by using the value of the successor node of target node to replace
    # the value of target node, then repeat this process on all other successor nodes.
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            next_node = node.next
            node.val = next_node.val

            if not next_node.next:
                node.next = None
                break

            node = next_node
