
class LRUCache(object):
    """
    @ Google, Uber, Facebook, Twitter, Zenefits, Amazon, Microsoft, Snapchat, Yahoo, Bloomberg, Palantir

    Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following
    operations: get and set.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
                      it should invalidate the least recently used item before inserting a new item.
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.adict = {}
        self.linkedList = DoublyLinkedList()

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.adict:
            # get the node by key
            node = self.adict[key]
            # update linked list by moving the node to
            # the tail of linked list
            self.linkedList.remove(node)
            self.linkedList.append(node)
            return node.val
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.capacity == 0:
            return

        if key in self.adict:
            node = self.adict[key]
            node.val = value

            # update linked list
            self.linkedList.remove(node)
            self.linkedList.append(node)
        else:
            # first, check if the number of items in adict is equal to
            # the capacity of the cache.
            # If the cache is full, remove the least recently used item
            if len(self.adict) == self.capacity:
                # get current LRU node
                node = self.linkedList.head.next_node
                # remove the key-node item from adict
                self.adict.pop(node.key, None)
                # update the linked list
                self.linkedList.remove(node)

            # creat a new node for key
            node = ListNode(key, value)
            # add new key-node item to adict
            self.adict[key] = node
            # append the node to linked list
            self.linkedList.append(node)


class ListNode(object):
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev_node = None
        self.next_node = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def append(self, node):
        node.prev_node = self.tail.prev_node
        self.tail.prev_node.next_node = node
        node.next_node = self.tail
        self.tail.prev_node = node

    def remove(self, node):
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node



if __name__ == "__main__":
    cache = LRUCache(1)
    cache.set(2, 1)
    print cache.get(2)
    cache.set(3, 2)
    print cache.get(2)
    print cache.get(3)
