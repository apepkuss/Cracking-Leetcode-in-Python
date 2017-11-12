class Solution(object):
    """
    Given a string, find the length of the longest substring without repeating characters.

    Examples:
    1. Given "abcabcbb", the answer is "abc", which the length is 3.
    2. Given "bbbbb", the answer is "b", with the length of 1.
    3. Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """
    def lengthOfLongestSubstring_dfs(self, s):  # LTE
        """
        :type s: str
        :rtype: int
        """
        def dfs(s, substr):
            if len(s) == 0 or s[0] in substr:
                self.length = max(self.length, len(substr))
                return True
            for i in xrange(len(s)):
                if dfs(s[i + 1:], substr + s[i]):
                    return True
            return False

        if s is None: return 0
        if len(s) < 2: return len(s)

        self.length = 0
        for i in xrange(len(s)):
            dfs(s[i+1:], s[i])
        return self.length

    def lengthOfLongestSubstring_hashtable(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None: return 0
        if len(s) < 2: return len(s)

        dict = {}
        maxlength = 0
        length = 0
        i = 0
        while i < len(s):
            if not dict.has_key(s[i]) or dict[s[i]] == -1:
                dict[s[i]] = i
                length += 1
            else:
                maxlength = max(maxlength, length)
                length = i - dict[s[i]]
                for key in dict.keys():
                    if dict[key] < dict[s[i]]:
                        dict[key] = -1
                dict[s[i]] = i
            i += 1
        maxlength = max(maxlength, length)
        return maxlength

    def lengthOfLongestSubstring_slidingWindow(self, s):
        if s is None: return 0
        if len(s) < 2: return len(s)
        n = len(s)
        # mimic ascii table
        table = [0] * 128
        res = 0
        i = 0
        for j in xrange(n):
            idx = ord(s[j])
            i = max(table[idx], i)
            res = max(res, j - i + 1)
            table[idx] = j + 1
        return res



if __name__ == "__main__":
    s = "abcabcbb"
    res = Solution().lengthOfLongestSubstring_slidingWindow(s)
    print res