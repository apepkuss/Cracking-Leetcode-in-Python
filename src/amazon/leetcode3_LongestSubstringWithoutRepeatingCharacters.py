
class Solution(object):
    """
    @ Amazon, Adobe, Bloomberg, Yelp

    Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke"
    is a subsequence and not a substring.
    """
    def lengthOfLongestSubstring_hashtable(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLen = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLen = max(maxLen, i - start + 1)

            usedChar[s[i]] = i

        return maxLen
