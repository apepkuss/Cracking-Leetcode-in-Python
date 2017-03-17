

class Solution(object):
    """
    @ Amazon

    Hash Table

    Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

    Strings consists of lowercase English letters only and the length of both strings s and p
    will not be larger than 20,100.

    The order of output does not matter.

    Example 1:

    Input:
    s: "cbaebabacd" p: "abc"

    Output:
    [0, 6]

    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    """

    def findAnagrams_ASCII(self, s, p): # O(n) time, O(1) space
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        m, n = len(s), len(p)
        if m < n: return res

        # hash table of string p
        table = [0] * 128
        # record each character in p to hash table
        for c in p:
            table[ord(c)] += 1

        # sliding window
        left = right = 0
        count = len(p)
        while right < m:
            key = ord(s[right])
            # current hash value >= 1 means the character is existing in p
            if table[key] >= 1:
                count -= 1
            table[key] -= 1
            right += 1

            # when b is down to 0, we found the right anagram,
            # then save left
            if count == 0:
                res.append(left)

            if right - left == len(p):
                key = ord(s[left])
                # only increase n if the character is in p
                if table[key] >= 0:
                    count += 1
                left += 1
                table[key] += 1

        return res

    def findAnagrams_HashTable(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if not s or not p or len(s) == 0 or len(p) == 0 or len(s) < len(p):
            return res

        m, n = len(s), len(p)
        # create a hash table
        table = {}
        for c in p:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1

        left = right = count = 0
        while (right < m):

            # check the char at right
            c = s[right]
            if c in table:
                # update value related to key
                table[c] -= 1
                if table[c] == 0:
                    # match a char in p
                    count += 1

            # check the window size
            if (right >= n):
                c = s[left]
                if c in table:
                    table[c] += 1
                    if table[c] == 1:
                        count -= 1
                left += 1

            # output left
            if count == len(table):
                res.append(left)

            right += 1

        return res


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    res = Solution().findAnagrams_slidingWindow(s, p)
    print res