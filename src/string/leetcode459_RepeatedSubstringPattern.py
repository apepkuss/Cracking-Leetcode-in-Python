

class Solution(object):
    """
    @ Amazon, Google

    String

    Given a non-empty string check if it can be constructed by taking a substring of it
    and appending multiple copies of the substring together. You may assume the given
    string consists of lowercase English letters only and its length will not exceed 10000.

    Example 1:
    Input: "abab"

    Output: True

    Explanation: It's the substring "ab" twice.
    """

    class Solution(object):
        def repeatedSubstringPattern(self, str):
            """
            :type str: str
            :rtype: bool
            """
            n = len(str)
            # if the length of a substring can be divided by the length of s,
            # and the new string constructed by the substring is same as s,
            # then return True
            for l in range(1, n / 2 + 1):
                if n % l == 0:
                    s = str[:l] * (n / l)
                    if s == str:
                        return True
            return False