
class Solution(object):
    """
    @ Amazon, Microsoft, Bloomberg

    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example:

    Input: "babad"

    Output: "bab"

    Note: "aba" is also a valid answer.
    Example:

    Input: "cbbd"

    Output: "bb"
    """
    # 方法1：DP解法，dp[i][j]表示索引i和j之间的子串是否为palindromic。初始化矩阵时，需要先判断长度为1和2的子串。
    # 然后从长度为3开始，最大到n，按照如下算法进行判断当前长度的子串是否为回文：对于子串s[i], s[i+1], ..., s[j-1], s[j]。
    # 如果s[i+1],...,s[j-1]是回文，并且s[i]==s[j]，那么s[i],...,s[j]就是回文。
    def longestPalindrome_dp(self, s): # RT: O(n^2) TLE error, Space: O(n^2)
        n = len(s)

        # dp[i][j] indicates whether the substring from i to j is a palindrome or not.
        dp = [[False] * n for _ in xrange(n)]

        # initialize the matrix
        for x in xrange(n):
            dp[x][x] = True

        maxlength = 1
        idx = 0
        # populate the remaining cells of the matrix
        for length in xrange(2, n + 1):
            for x in xrange(n - length + 1):
                y = x + length - 1
                if s[x] == s[y] and dp[x + 1][y - 1]:
                    dp[x][y] = True
                    if maxlength < length:
                        maxlength = length
                        idx = x
        return s[idx:idx + maxlength]


    # 方法2：对方法1的空间复杂度加以改进。算法的思路是每个回文都是从中间元素为中心两侧对称的字符串，而中心点可能是某个字符
    # 也可能是两个字符中间的位置。对于一个长度为n的字符串，这样的中心点有2n-1个：有n个字符，每个字符为一个；另外n个字符中，
    # 每两个字符中间的位置为一个中间点，这样的位置有n-1个。依次以这2n-1个位置为中心点进行判定，获得最大回文子串。每次扩展为O(n)，
    # 所以总的时间复杂度为O(n^2)。
    def longestPalindrome_CenterAround(self, s):  # RT: O(n^2) TLE error, Space: O(1)
        def expandAroundCenter(s, c1, c2):
            l, r = c1, c2
            n = len(s)
            while l >= 0 and r <= n - 1 and s[l] == s[r]:
                l -= 1;
                r += 1
            return s[l + 1:r]

        n = len(s)
        if n == 0: return ""
        maxstring = s[0]
        for x in xrange(1, n):
            # centered at the whitespace between s[x-1] and s[x]
            substring = expandAroundCenter(s, x - 1, x)
            if len(maxstring) < len(substring):
                maxstring = substring

            # centered at the character s[x]
            substring = expandAroundCenter(s, x, x)
            if len(maxstring) < len(substring):
                maxstring = substring
        return maxstring


    # 方法3：Manacher's algorithm. 该方法利用回文的对称特性避免重复计算。
    def longestPalindrome_manacher(self, s):  # RT: O(n), Space: O(n)

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
        for i in xrange(2, n):
            # j denotes current left edge
            j = center - (i - center)

            # if current right edge i is within center right edge rightEdge
            if rightEdge > i:
                dp[i] = min(rightEdge - i, dp[j])

            # attempt to expand palindrome centers at i
            while 0 < (i - dp[i]) and (i + dp[i]) < n-1 and \
                    (((i + dp[i] + 1) % 2 == 0) or (s[i + dp[i] + 1] == s[i - (dp[i] + 1)])):
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






