

# Time Complexity: Time complexity of the implementation below is same as time complexity of QuickSort for arrays.
# It takes O(n^2) time in worst case and O(nLogn) in average and best cases. The worst case occurs when the linked
# list is already sorted.
# The important things about implementation are, it changes pointers rather swapping data.

# Can we implement random quick sort for linked list?
# QuickSort can be implemented for Linked List only when we can pick a fixed point as pivot (like last element in
# the implementation below). Random QuickSort cannot be efficiently implemented for Linked Lists by picking random
# pivot.


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def quick_sort_singlyLinkedList(head):
    tail = get_tail(head)
    return quick_sort_recur(head, tail)

def get_tail(head):
    p = head
    while p and p.next:
        p = p.next
    return p

def quick_sort_recur(head, tail):
    if not head or head == tail:
        return head

    new_head, new_tail, pivot = partition(head, tail)

    # quick sort the left side of pivot
    if new_head != pivot:
        # before sorting, find the tail node p before pivot first
        p = new_head
        while p.next != pivot:
            p = p.next
        p.next = None

        # then, recursively quick sort the list before pivot
        new_head = quick_sort_recur(new_head, p)

        # append pivot to the tail of the sorted list
        p = get_tail(new_head)
        p.next = pivot

    # quick sort the right side of pivot
    pivot.next = quick_sort_recur(pivot.next, new_tail)

    return new_head

def partition(head, tail):
    pivot = tail
    pre, curr, end = None, head, tail
    new_head = None
    while curr != pivot:
        if curr.val < pivot.val:
            if not new_head:
                new_head = curr
            pre = curr
            curr = curr.next

        else:
            # move curr node to next of tail, and then change tail
            if pre:
                pre.next = curr.next
            tmp = curr.next
            curr.next = None
            end.next = curr
            end = curr
            curr = tmp
    # if all nodes have bigger value than pivot node, then pivot node
    # becomes the head of new list
    if not new_head:
        new_head = pivot
    return new_head, end, pivot

