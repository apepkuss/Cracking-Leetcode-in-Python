
class TrieNode(object):
    def __init__(self, value=None):
        self.value = value
        self.isLeaf = False
        self.kids = {}

class Solution(object):
    """
    @ Microsoft, Google, Airbnb
    
    Backtracking, Trie
    
    Given a 2D board and a list of words from the dictionary, find all words in the board.

    Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those 
    horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
    
    For example,
    Given words = ["oath","pea","eat","rain"] and board =
    
    [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    Return ["eat","oath"].
    Note:
    You may assume that all inputs are consist of lowercase letters a-z.
    """

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = set()
        if not words or not board:
            return []

        # build up a trie with words
        trie = self.buildTrie(words)

        m, n = len(board), len(board[0])
        # used[i][j] denotes if the (i,j)-th cell is used or not
        used = [[False] * n for _ in range(m)]

        # dfs search boards
        for i in range(m):
            for j in range(n):
                self.backtrack(trie, used, board, i, j, '', res)

        return list(res)

    def buildTrie(self, words):
        """Build up a trie with a given word list
        """
        root = TrieNode()

        for word in words:
            curr = root
            for c in word:
                if c not in curr.kids:
                    curr.kids[c] = TrieNode(c)
                curr = curr.kids[c]
            curr.isLeaf = True

        return root

    def backtrack(self, trieNode, used, board, i, j, value, res):
        c = board[i][j]
        if trieNode.kids and c in trieNode.kids:
            tnode = trieNode.kids[c]
            if tnode.isLeaf:
                res.add(value + c)
            used[i][j] = True

            # up
            if i > 0 and not used[i - 1][j]:
                self.backtrack(tnode, used, board, i - 1, j, value + c, res)

            # down
            if i < len(board) - 1 and not used[i + 1][j]:
                self.backtrack(tnode, used, board, i + 1, j, value + c, res)

            # left
            if j > 0 and not used[i][j - 1]:
                self.backtrack(tnode, used, board, i, j - 1, value + c, res)

            # right
            if j < len(board[0]) - 1 and not used[i][j + 1]:
                self.backtrack(tnode, used, board, i, j + 1, value + c, res)

            used[i][j] = False


if __name__ == "__main__":
    board = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
    words = ["oath", "pea", "eat", "rain"]
    res = Solution().findWords(board, words)
    print res



