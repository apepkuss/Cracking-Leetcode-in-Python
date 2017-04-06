
class TrieNode(object):
    def __init__(self, value=None):
        self.value = value
        self.kids = {}
        self.isLeaf = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if not word or len(word) == 0:
            return

        curr = self.trie.root
        for c in word:
            if c not in curr.kids:
                curr.kids[c] = TrieNode(c)
            curr = curr.kids[c]
        curr.isLeaf = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot 
        character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word or len(word) == 0:
            return False

        return self.searchUtil(word, [self.trie.root])

    def searchUtil(self, word, nodes):
        if word is None or nodes is None:
            return False

        for node in nodes:
            curr = node
            for i in range(len(word)):
                c = word[i]
                if c != '.' and c not in curr.kids:
                    break

                elif c == '.':
                    # if '.' is the last character
                    if i == len(word)-1:
                        for kid in curr.kids.values():
                            if kid.isLeaf:
                                return True
                        break

                    # if '.' is not the last character
                    else:
                        next_nodes = curr.kids.values()
                        if next_nodes and self.searchUtil(word[i+1:], next_nodes):
                            return True
                        else:
                            break

                else:
                    curr = curr.kids[c]
                    if i == len(word) - 1 and curr.isLeaf:
                        return True

        return False


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    res = wd.search("b..")
    print res

