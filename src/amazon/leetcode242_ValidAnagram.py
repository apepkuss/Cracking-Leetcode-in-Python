
class Solution(object):
    """
    @ Amazon, Uber, Yelp

    Hash Table

    Given two strings s and t, write a function to determine if t is an anagram of s.

    For example,
    s = "anagram", t = "nagaram", return true.
    s = "rat", t = "car", return false.

    Note:
    You may assume the string contains only lowercase alphabets.

    Follow up:
    What if the inputs contain unicode characters? How would you adapt your solution to such case?
    """

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        adict = {}
        for c in s:
            if c not in adict:
                adict[c] = 1
            else:
                adict[c] += 1

        for c in t:
            if c not in adict:
                return False
            else:
                adict[c] -= 1

        for v in adict.values():
            if v != 0:
                return False

        return True


if __name__ == "__main__":
    s = "a"
    t = "a"
    res = Solution().isAnagram(s, t)
    print res