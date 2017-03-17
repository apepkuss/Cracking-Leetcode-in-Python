
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
        m, n = len(s), len(t)

        # check if their length are same
        if m != n: return False

        # use hashtable to compute the number of each character in s and t
        s_table = {}
        t_table = {}

        for i in range(len(s)):
            if s[i] not in s_table:
                s_table[s[i]] = 1
            else:
                s_table[s[i]] += 1
            if t[i] not in t_table:
                t_table[t[i]] = 1
            else:
                t_table[t[i]] += 1

        # check if s and t have same number of characters
        for k, v in s_table.items():
            if k not in t_table or v != t_table[k]:
                return False
        return True


if __name__ == "__main__":
    s = "a"
    t = "a"
    res = Solution().isAnagram(s, t)
    print res