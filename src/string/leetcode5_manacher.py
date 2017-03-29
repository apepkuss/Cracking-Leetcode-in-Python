import unittest


class Solution(object):

    def longestPalindrome_manacher(self, s):  # RT: O(n), Space: O(n)
        # preprocess the target string
        T = Solution.preprocess(s)
        # compute the
        dp = Solution.compute_longest_palindrome(T)

        # find the maximum element in dp
        maxlen = 0
        centeridx = 0
        for x in xrange(1, len(T)-1):
            if maxlen < dp[x]:
                maxlen = dp[x]
                centeridx = x

        # being divided by 2 means removing '#' characters
        start = (centeridx-maxlen-1)/2
        return s[start:start+maxlen]

    @classmethod
    def preprocess(cls, s):  # O(n) time
        """
        Insert '#' into the original string between every two characters:
            '^' denotes the starting position of the new string,
            '$' denotes the ending position of the new string.
        """
        n = len(s)
        if n == 0: return "^$"
        res = "^"
        for x in xrange(n):
            res += "#" + s[x]
        res += "#$"
        return res

    @classmethod
    def compute_longest_palindrome(cls, T):
        """
        Compute the longest palindromic substring T
        :param T:
        :return:
        """
        # dp[x] denotes the length of the longest palindrome centered at T[x]
        dp = [0 for _ in xrange(len(T))]

        center, rightEdge = 0, 0
        for x in xrange(1, len(T) - 1):
            # x'=center-(x-center)
            x_mirror = center - (x - center)

            dp[x] = min(rightEdge - x, dp[x_mirror]) if rightEdge > x else 0

            # attempt to expand palindrome centering at x
            while x-dp[x]-1>=0 and x+dp[x]+1<=len(T) and T[x+dp[x]+1] == T[x-dp[x]-1]:
                dp[x] += 1

            # If palindrome centered at x expand past rightEdge,
            # update center and rightEdge based on expanded palindrome
            if x + dp[x] > rightEdge:
                center = x
                rightEdge = x + dp[x]

        return dp

    def LPS_manacher(self, s):  # RT: O(n), Space: O(n)

        if len(s) < 2: return s

        # simulate inserting $ symbols between each pair of characters and the head and tail position of input s
        n = len(s) * 2 + 1

        # dp[i] denotes the length of the longest palindromic substring centered at s[i]
        dp = [0] * n
        dp[0] = 0
        dp[1] = 1

        # the index of current center character
        center = 1
        # the right edge of longest palindromic substring centered at index of center
        rightEdge = 2

        maxLPSLength = 0
        maxLPSCenter = 0

        # i denotes current right edge
        for i in xrange(2, n-1):
            # j denotes mirror position of i
            j = center - (i - center)

            # if current right edge i is within center right edge rightEdge
            if rightEdge - i > 0:
                dp[i] = min(rightEdge - i, dp[j])

            # attempt to expand palindrome centers at i
            while 0 < (i - dp[i]) and (i + dp[i]) < n-1 and \
                    (((i + dp[i] + 1) % 2 == 0) or (s[(i + dp[i] + 1)/2] == s[(i - (dp[i] + 1))/2])):
                dp[i] += 1

            # track maxLPSLength
            if dp[i] > maxLPSLength:
                maxLPSLength = dp[i]
                maxLPSCenter = i

            # If current LPS centered at i expands past rightEdge,
            # update center and rightEdge based on current LPS
            if i + dp[i] > rightEdge:
                center = i
                rightEdge = i + dp[i]

        start = (maxLPSCenter - maxLPSLength) / 2
        end = start + maxLPSLength - 1
        return s[start : end+1]


class TestRun(unittest.TestCase):

    def test_case1(self):
        s = "abaab"
        actual = Solution().LPS_manacher(s)
        expected = "baab"
        unittest.TestCase.assertEqual(self, first=expected, second=actual)


if __name__ == "__main__":
    unittest.main()




