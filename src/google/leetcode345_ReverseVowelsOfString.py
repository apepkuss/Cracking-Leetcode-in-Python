
class Solution(object):
    """
    @ Google

    Write a function that takes a string as input and reverse only the vowels of a string.

    Example 1:
    Given s = "hello", return "holle".

    Example 2:
    Given s = "leetcode", return "leotcede".

    Note:
    The vowels does not include the letter "y".
    """
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 2:
            return s
        res = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(res) - 1
        while i < j:
            while i < j and res[i] not in vowels:
                i += 1
            if i == j: break
            while j > i and res[j] not in vowels:
                j -= 1
            if j == i: break
            # swap the elements at i and j
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1

        return ''.join(res)


if __name__ == "__main__":
    s = 'hello'
    res = Solution().reverseVowels(s)
    print res

