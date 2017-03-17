
class Solution(object):
    """
    @ Amazon, Linkedin, Snapchat, Facebook, Yelp

    Backtracking

    Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
    sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each intermediate word must exist in the word list
    For example,

    Given:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.

    Note:
    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    """

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        n = len(beginWord)
        length = 1
        curr_words = set()
        curr_words.add(beginWord)
        next_words = set()
        while True:
            # remove candidate words from wordList to avoid multiple usage
            for word in curr_words:
                if word in wordList:
                    wordList.remove(word)
            # replace each character in the candidate word with a new character,
            # then check if the new word is in the wordList. If yes, put it in
            # the set for next round; if no, ignore it.
            for word in curr_words:
                for i in xrange(n):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != ch:
                            aword = word[:i] + ch + word[i+1:]
                            if aword in wordList:
                                next_words.add(aword)
            # if the word set for next round is empty, it means we cannot get endWord
            # just with words in wordList as intermediate words; otherwise, go into next
            # round.
            if len(next_words) > 0:
                length += 1
                curr_words = next_words
                next_words.clear()
            else:
                return 0
        return length


if __name__ == "__main__":
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog"]
    res = Solution().ladderLength(beginWord, endWord, wordList)
    print res


