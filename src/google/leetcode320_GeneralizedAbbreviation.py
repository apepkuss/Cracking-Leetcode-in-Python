
class Solution(object):
    """
    @ Google

    Write a function to generate the generalized abbreviations of a word.

    Example:
        Given word = "word", return the following list (order does not matter):
        ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
        "w1r1", "1o2", "2r1", "3d", "w3", "4"]
    """
    def generateAbbreviations_dfs1(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def dfs(curr, pos, count):
            """
            curr: the current string
            pos: the index of the character in word
            count: the number of the characters being handled
            """
            if pos == len(word):
                if count != 0:
                    curr += str(count)
                res.append(curr)
            else:
                # case 1: replace word[pos] with numbers
                dfs(curr, pos+ 1, count + 1)

                # case 2: keep word[pos]
                if count != 0: curr += str(count)
                curr += word[pos]
                dfs(curr, pos + 1, 0)

        res = []
        dfs('', 0, 0)
        return res

    def generateAbbreviations_dfs2(self, word):
        def dfs(curr, i):
            if i == len(word):
                res.append(curr)
                return
            # case 1: keep word[i]
            dfs(curr + word[i], i + 1)

            # case 2: replace word[i] with different nums
            size = len(word) - i
            for l in range(1, size):
                dfs(curr + str(l) + word[i + l], i + l + 1)
            dfs(curr + str(size), len(word))

        res = []
        dfs('', 0)
        return res


if __name__ == "__main__":
    word = 'word'
    res = Solution().generateAbbreviations_dfs(word)
    print res
