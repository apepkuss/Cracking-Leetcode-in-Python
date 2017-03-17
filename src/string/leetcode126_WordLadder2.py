
### elements 19.5

class Solution(object):
    """
    @ Amazon, Yelp

    Array, Backtracking, Breadth-first Search, String

    Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s)
    from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each intermediate word must exist in the word list
    For example,

    Given:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    Return
      [
        ["hit","hot","dot","dog","cog"],
        ["hit","hot","lot","log","cog"]
      ]

    Note:
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    """
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        # do dfs to construct paths from beginWord to endWord
        # based on prevMap
        def dfsBuildPath(path, word):
            path.append(word)
            if len(prevMap[word])==0:
                currPath = path[:]
                currPath.reverse()
                res.append(currPath)
                return
            for w in prevMap[word]:
                dfsBuildPath(path, w)
                path.pop()

        res = []
        n = len(beginWord)
        prevMap = {}
        for word in wordlist:
            prevMap[word] = []

        # use two sets to simulate a queue by
        # switch them each round
        candidates = [set(), set()]
        current, previous = 0, 1
        candidates[current].add(beginWord)

        while True:
            current, previous = previous, current
            for word in candidates[previous]:
                wordlist.remove(word)
            candidates[current].clear()
            for word in candidates[previous]:
                # each time change one character in 'word'
                # if the new word exists in wordlist, save
                # it in prevMap and candidates' current set
                # for next round.
                for i in range(n):
                    part1=word[:i]; part2=word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i]!=j:
                            nextword = part1 + j + part2
                            if nextword in wordlist:
                                prevMap[nextword].append(word)
                                candidates[current].add(nextword)
            # if no previous word exists in wordlist
            # it means beginWord cannot be transformed
            # into endWord
            if len(candidates[current])==0: return res
            if endWord in candidates[current]: break

        dfsBuildPath([], endWord)
        return res