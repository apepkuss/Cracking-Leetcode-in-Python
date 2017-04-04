
class Solution(object):
    """
    @ Dropbox, Uber
    
    Backtracking
    
    Given a pattern and a string str, find if str follows the same pattern.
    
    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
    
    Examples:
    pattern = "abab", str = "redblueredblue" should return true.
    pattern = "aaaa", str = "asdasdasdasd" should return true.
    pattern = "aabb", str = "xyzabcxzyabc" should return false.
    Notes:
    You may assume both pattern and str contains only lowercase letters.
    """
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        adict = {}
        return self.backtrack(pattern, 0, str, 0, adict)

    def backtrack(self, pat, i, str, j, adict):
        if len(pat) == i and len(str) == j:
            return True
        if len(pat) == i or len(str) == j:
            return False

        # get current character in pat
        key = pat[i]

        # if adict contains pat[i]
        if key in adict:
            value = adict[key]
            # check if str[j:] starts with value
            if not str.startswith(value, j):
                return False

            return self.backtrack(pat, i+ 1, str, j + len(value), adict)

        # if adict does not contain pat[i]
        for k in range(j, len(str)):
            value = str[j:k + 1]
            # following check is necessary, because value
            # could belong to a different key
            if value in adict.values():
                continue

            # add key-value pair into adict
            adict[key] = value

            if self.backtrack(pat, i + 1, str, k + 1, adict):
                return True

            adict.pop(key, None)

        return False
