
# use deque to maintain a LRU linked list
# deque provides append and pop operations with approximately O(1) performance in either direction.
from collections import deque

class Node(object):
    """
    Frequency doubly linked list node:
    current node has higher frequency than its previous node, but less than its next neighbor.
    """
    def __init__(self, frequency):
        self.frequency = frequency
        self.keys = deque()
        self.pre, self.next = None, None


class LFUCache(object):
    """
    @ Amazon, Google

    Design


    Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

    Follow up:
    Could you do both operations in O(1) time complexity?

    Example:

    LFUCache cache = new LFUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.get(3);       // returns 3.
    cache.put(4, 4);    // evicts key 1.
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # a linked list, in which nodes are sorted by their frequencies
        self.head = None
        # capacity of LFU cache
        self.capacity = capacity
        # a key-value dictionary: key is the given key, value is the given value
        self.valueHash = {}
        # a key-FrequencyNode dictionary: key is the given key, value is a frequency list node
        self.nodeHash = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.valueHash:
            self.increase_frequency(key)
            return self.valueHash[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return

        if key in self.valueHash:
            self.valueHash[key] = value
        else:
            # check current capacity of LFU cache
            if len(self.valueHash) == self.capacity:
                self.removeOld()

            # add the key-value pair to the key-value dictionary
            self.valueHash[key] = value

            # add the key to the head of the frequency linked list
            self.addToHead(key)

        # update the frequency of the key
        self.increase_frequency(key)


    def increase_frequency(self, key):
        """
        Increase the frequency of key by one
        :param key:
        :return:
        """
        node = self.nodeHash[key]
        node.keys.remove(key)

        if node.next is None:
            node.next = Node(node.occurrence + 1)
            node.next.pre = node
            node.next.keys.append(key)
        elif node.next.frequency == node.occurrence + 1:
            node.next.keys.append(key)
        else:
            anode = Node(node.occurrence + 1)
            anode.keys.append(key)
            anode.pre = node
            anode.next = node.next
            node.next.pre = anode
            node.next = anode

        self.nodeHash[key] = node.next
        if len(node.keys) == 0:
            self.remove(node)

    def remove(self, node):
        """
        Remove a specified node from frequency linked list
        :param node: the node to be removed
        """
        if node.pre is None:
            self.head = node.next
        else:
            node.pre.next = node.next

        if node.next:
            node.next.pre = node.pre

    def removeOld(self):
        """
        Remove the least recently used key from frequency linked list
        """
        if self.head is None:
            return

        key = self.head.keys.popleft()

        if len(self.head.keys) == 0:
            self.remove(self.head)

        self.valueHash.pop(key, None)
        self.nodeHash.pop(key, None)


    def addToHead(self, key):
        """
        Add a new key as head node to frequency linked list
        :param key: the new key
        """
        if self.head is None:
            self.head = Node(0)
            self.head.keys.append(key)
        elif self.head.frequency > 0:
            node = Node(0)
            node.keys.append(key)
            node.next = self.head
            self.head.pre = node
            self.head = node
        else:
            self.head.keys.append(key)

        self.nodeHash[key] = self.head


if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print cache.get(1)
    cache.put(3, 3)
    print cache.get(2)
    print cache.get(3)
    cache.put(4, 4)
    print cache.get(1)
    print cache.get(3)
    print cache.get(4)



