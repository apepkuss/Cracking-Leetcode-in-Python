

class TrieNode(object):
    def __init__(self):
        self.isLeaf = False
        self.children = [None for _ in xrange(26)]
        self.kids = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):  # O(n) time, n is length of key
        """
        insert a key into trie
        :param key: a string to insert
        """
        curr = self.root
        for c in key:
            if c not in curr.kids:
                curr.kids[c] = TrieNode()
            curr = curr.kids[c]

        # mark the last node as leaf
        curr.isLeaf = True

    def search(self, key):  # O(n) time, n is length of key
        """
        search a key in trie
        :param key: the key to search
        :return: True, if the key presents; otherwise, False.
        """
        curr = self.root
        for c in key:
            if c not in curr.kids:
                return False
            curr = curr.kids[c]
        return curr and curr.isLeaf

    def deleteUtil(self, node, key, idx):
        """
        Delete a key from trie in a recursive way
        :return: True, if current node has no kids and is also not a leaf node; otherwise, False.
        """
        if node:
            # base case
            if idx == len(key):
                if node.isLeaf:
                    node.isLeaf = False
                    # check if node can be removed
                    if not node.kids:
                        return True
                    return False

            # recursive step
            else:
                c = key[idx]
                if self.deleteUtil(node.kids[c], key, idx+1):
                    node.kids.pop(c, None)
                    return (not node.isLeaf) and (not node.kids)

        return False

    def delete(self, root, key):
        """
        Case 1: Key may not be there in trie. Delete operation should not modify trie.
        Case 2: Key present as unique key (no part of key contains another key (prefix), nor the key itself
                is prefix of another key in trie). Delete all the nodes.
        Case 3: Key is prefix of another key in trie. Unmark the leaf node.
        Case 4: Key present in trie, having at least one other key as prefix key. Delete nodes from end of key
                until first leaf node of longest prefix key.
        """
        if len(key) > 0:
            self.deleteUtil(self.root, key, 0)
