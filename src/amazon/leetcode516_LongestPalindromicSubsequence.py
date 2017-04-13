

class Solution(object):
    """
    @ Amazon, Uber
    
    DP
    
    Given a string s, find the longest palindromic subsequence's length in s. 
    You may assume that the maximum length of s is 1000.
    
    Example 1:
    Input: "bbbab"
    Output: 4
    One possible longest palindromic subsequence is "bbbb".
    
    Example 2:
    Input: "cbbd"
    Output: 2
    One possible longest palindromic subsequence is "bb".
    """

    def longestPalindromeSubseq(self, s):  # O(n^2) time, O(n^2) space
        """
        :type s: str
        :rtype: int
        """
        # check if s is palindrome itself
        if s == s[::-1]:
            return len(s)

        n = len(s)

        # table[i][j] indicates longest palindrome subsequence of s[i..j]
        table = [[0] * n for _ in range(n)]

        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1

                if i == j:
                    table[i][j] = 1
                elif s[i] == s[j]:
                    table[i][j] = table[i + 1][j - 1] + 2
                else:
                    table[i][j] = max(table[i][j - 1], table[i + 1][j])

        return table[0][n - 1]



