

# Function to check if a singly linked list is palindrome
# Given a singly linked list of characters, write a function that returns true if the given list is palindrome, else false.


# Method 1: Use a stack
# A simple solution is to use a stack of list nodes. This mainly involves three steps:
#
# 1. Traverse the linked list from the head to the tail one time and push values of all nodes into a stack;
# 2. Traverse the linked list again. For each visited node, pop out a value from the stack, and compare the value with
#    the value of current visited node.
# 3. If all nodes matched, return True; otherwise, return False.
#
# Time complexity of the algorithm is O(n), space complexity is O(n) for stack.
#




# Method 2: Reverse the linked list
#
# 1. Get the middle of the linked list with fast-slow two pointers;
# 2. Reverse the second half of the linked list;
# 3. Check if the first half and second half are identical;
# 4. Constructing the original linked list by reversing the second half and attaching it back to the first half.
#
# Time complexity is O(n), space complexity is O(1).
#

# An interesting algorithm for finding the middle of a linked list

class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_nodes(self, values):
        curr = self.head

        for value in values:
            if not curr:
                curr = ListNode(value)
                self.head = curr
            else:
                node = ListNode(value)
                curr.next = node
                curr = node

    def find_middle(self):
        count = 0
        mid = self.head
        curr = self.head
        while curr:
            if count & 1:
                mid = mid.next
            count += 1
            curr = curr.next
        print 'count: ' + str(count)
        return mid

    def print_list(self):
        curr = self.head
        while curr:
            print curr.value
            curr = curr.next


if __name__ == "__main__":
    values = [1,2,3,4,5,6]
    llist = LinkedList()
    llist.add_nodes(values)
    llist.print_list()
    node = llist.find_middle()
    print node.value

