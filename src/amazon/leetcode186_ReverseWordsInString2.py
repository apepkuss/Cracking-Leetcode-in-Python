

class Solution(object):
    """
    @ Amazon, Microsoft, Uber

    Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
    Could you do it in-place without allocating extra space?

    The input string does not contain leading or trailing spaces and the words are always separated by a single space.

    For example,
    Given s = "the sky is blue",
    return "blue is sky the".
    """
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        if s is None or len(s) <= 1:
            return

        # use two pointers to iterate the array from two sides, exchanging the values they point to.
        i, j = 0, len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        # after the first iteration, the s is reversed, but each string in s is also reversed, we need
        # to reverse the string.
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != ' ':
                j += 1
            if j < len(s):
                s[i:j] = s[i:j][::-1]
            else:
                s[i:] = s[i:][::-1]
            i = j + 1


if __name__ == "__main__":
    s = list("the sky is blue")
    Solution().reverseWords(s)
    print s

