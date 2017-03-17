

# Note that suffix trie is adopted when text doesn't change very frequently and there are many search queries.
# Reference http://www.geeksforgeeks.org/pattern-searching-set-8-suffix-tree-introduction/

# The implementation of suffix tree below can return a list of index sequences of all occurrences of a pattern
# in a text.

class TrieNode(object):
    def __init__(self):
        self.kids = {}
        self.indexes = []


class SuffixTrie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert_suffix(self, suffix, start):
        curr = self.root
        indexes = []
        for i in range(len(suffix)):
            c = suffix[i]
            if c not in curr.kids:
                curr.kids[c] = TrieNode()
            indexes.append(i)
            curr = curr.kids[c]
        curr.indexes.append(indexes)

    def search_suffix(self, suffix):
        curr = self.root
        for c in suffix:
            if c not in curr.kids:
                return None
            curr = curr.kids[c]
        return curr.indexes


def build_suffix_trie(text):
    n = len(text)
    trie = SuffixTrie()

    # insert all suffixes into trie
    for i in range(n):
        trie.insert_suffix(text[i:], i)

    return trie


def strStr(text, pattern):

    trie = build_suffix_trie(text)
    return trie.search_suffix(pattern)
