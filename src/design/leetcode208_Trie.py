
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [None]*26
        self.isLeaf = False

class Trie(object):
    """
    @ Google, Uber, Facebook, Twitter, Microsoft, Bloomberg

    Implement a trie with insert, search, and startsWith methods.

    Note:
    You may assume that all inputs are consist of lowercase letters a-z.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if len(word) > 0:
            ptr = self.root
            for i in range(len(word)):
                idx = ord(word[i])-97
                if ptr.data[idx] is None:
                    ptr.data[idx] = TrieNode()
                ptr = ptr.data[idx]
                if i == len(word)-1:
                    ptr.isLeaf = True
                    break

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if len(word) > 0:
            ptr = self.root
            for i in range(len(word)):
                idx = ord(word[i])-97
                if ptr.data[idx] is None:
                    break
                ptr = ptr.data[idx]
                if i == len(word)-1 and ptr.isLeaf:
                    return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) > 0:
            ptr = self.root
            for i in range(len(prefix)):
                idx = ord(prefix[i])-97
                if ptr.data[idx] is None:
                    break
                ptr = ptr.data[idx]
                if i == len(prefix)-1:
                    return True
        return False


if __name__ == "__main__":
    trie = Trie()
    trie.insert('a')
    print trie.search('a')
    print trie.startsWith('a')