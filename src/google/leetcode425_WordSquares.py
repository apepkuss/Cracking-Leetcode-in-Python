
class TrieNode(object):
    def __init__(self):
        self.prefix = []
        self.kids = {}

class Solution(object):
    """
    @ Google

    Trie, Backtracking

    Given a set of words (without duplicates), find all word squares you can build from them.

    A sequence of words forms a valid word square if the kth row and column read the exact same string,
    where 0 <= k < max(numRows, numColumns).

    For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word
    reads the same both horizontally and vertically.

    b a l l
    a r e a
    l e a d
    l a d y

    Note:
    There are at least 1 and at most 1000 words.
    All words will have the exact same length.
    Word length is at least 1 and at most 5.
    Each word contains only lowercase English alphabet a-z.
    """

    # The key part of this question is which data structures to choose, trie or hashtable.
    # They cause different time complexity for different operations. For looking up prefix,
    # it will use O(N*L) time to construct a trie, while O(N* L^2) for hashtable. But for
    # lookup operation, hashtable is O(1) time, while O(L) time for trie.

    # Time Complexity Analysis:
    # Let N be the number of words, and L be the length of each word
    # 1. Build up a prefix trie: for each word and each length, O(N*L) time for a prefix trie
    # 2. DFS search with backtracking: for the worst case, in each level are N words, search L levels, O((N*L)^L) time.
    # The total time complexity is O(N*L + (N*L)^L).


    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        res = []
        if not words: return res

        # build a trie for checking prefix
        trie = self.buildTrie(words)
        for word in words:
            # dfs + backtracking
            self.search(len(words[0]), trie, [word], res)

        return res

    def buildTrie(self, words): # O(N*L) time, N is the number of words, L is the length of each
        """
        Build up a trie for searching prefix
        :param words: a list of word used to construct trie
        :return: the root node of trie
        """
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.kids:
                    curr.kids[c] = TrieNode()
                curr.prefix.append(word)
                curr = curr.kids[c]
        return root

    def search(self, size, root, wordlist, res): # O(N^L) time
        """
        use dfs + backtracking to search a set of words which form a word square
        :param size: the length of a word, which is a fixed number.
        :param root: the root node of trie
        :param wordlist: a list of candidate words
        :param res: a list that stores each word list forming word square
        """
        if size == len(wordlist):
            res.append(wordlist)
            return

        idx = len(wordlist )
        prefix = ''
        for word in wordlist:
            prefix += word[idx]

        # find the words in trie, which have prefix
        words = self.findWordsWithPrefix(root, prefix)
        for word in words:
            self.search(size, root, wordlist+ [word], res)

    def findWordsWithPrefix(self, root, prefix): # O(L) time
        """
        Search on the trie to find words having a specified prefix
        :param root: the root node of trie
        :param prefix: the prefix to search on trie
        :return: a list of words having the prefix
        """
        words = []
        curr = root
        for c in prefix:
            if c not in curr.kids:
                return words
            curr = curr.kids[c]
        words = curr.prefix
        return words








