

class Solution(object):
    """
    @ Google

    Design two functions:
        addFilter(String filter): add a filter, which is a string, and could contains * matching 0 or more characters
                                  for example h*o or fo*d
        boolean isWordBlacklisted(String word): check if word matches some filter
                For example:
                    food -> true
                    hello -> true
                    foo -> false
                    fod -> true
                    foood -> true
                    focfd -> true
    """

    def __init__(self):
        self.root = None

    def addFilter(self, filter):
        if self.root is None:
            self.root = TrieNode()
        curr = self.root
        for c in filter:
            if c not in curr.kids:
                curr.kids[c] = TrieNode()
            curr = curr.kids[c]
        curr.end = True

    def isWordBlacklisted(self, node, word):
        if not word:
            return node.end
        if word[0] not in node.kids:
            if '*' not in node.kids:
                return False
            return any(self.isWordBlacklisted(node.kids['*'], word[i:]) for i in range(len(word) + 1))
        return self.isWordBlacklisted(node.kids[word[0]], word[1:])


class TrieNode(object):

    def __init__(self):
        self.kids = {}
        self.end = False


if __name__ == "__main__":
    trie = Solution()
    trie.addFilter('fo*de')
    assert(trie.isWordBlacklisted(trie.root, 'foaide'))
    trie.addFilter('h*o')
    trie.addFilter('fo*d')
    assert (trie.isWordBlacklisted(trie.root, 'food'))
    assert (trie.isWordBlacklisted(trie.root, 'hello'))
    assert (not trie.isWordBlacklisted(trie.root, 'foo'))
    assert (trie.isWordBlacklisted(trie.root, 'fod'))
    assert (trie.isWordBlacklisted(trie.root, 'foood'))
    assert (trie.isWordBlacklisted(trie.root, 'focfd'))