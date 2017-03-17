
class Solution(object):
    """
    @ Microsoft, Snapchat, Apple, Bloomberg, Yelp, INRIX
    Given an input string, reverse the string word by word.

    For example,
    Given s = "the sky is blue",
    return "blue is sky the".
    """
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        text = s[::-1]
        words = text.split()
        res = [word[::-1] for word in words]
        return ' '.join(res)


if __name__ == "__main__":
    s = "hi!"
    res = Solution().reverseWords(s)
    print res
