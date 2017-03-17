
class Solution(object):
    """
    @ Google

    Given a sequence of words, check whether it forms a valid word square. A sequence of words forms a valid word
    square if the kth row and column read the exact same string, where 0 <= k < max(numRows, numColumns).

    Note:
    1. The number of words given is at least 1 and does not exceed 500.
    2. Word length will be at least 1 and does not exceed 500.
    3. Each word contains only lowercase English alphabet a-z.
    """
    def validWordSquare1(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        m = len(words)
        cols = []
        for j in range(m):
            s = ''
            for i in range(m):
                if j < len(words[i]):
                    s += words[i][j]
            cols.append(s)

        for i in range(m):
            if words[i] != cols[i]:
                return False
        return True

    def validWordSquare(self, words): # O(m*n) time, m words, the maximum length of one in words is n
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range(len(words)):
            for j in range(len(words[i])):
                # to compare words[i][j] with words[j][i], should guarantee i and j inbound.
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True


if __name__ == "__main__":
    solution = Solution()
    words = ["abcdw", "bnrtx", "crmy", "dtye"]
    assert(not solution.validWordSquare(words))
    words = ["abcd","bnrt","crmy","dtye"]
    assert(solution.validWordSquare(words))

