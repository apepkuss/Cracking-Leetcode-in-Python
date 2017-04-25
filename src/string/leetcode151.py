
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
        if not s: return s

        # use two pointers pointing to head and tail of s
        p, q = 0, len(s) - 1
        chars = list(s)

        # reverse the entire string
        while p < q:
            # exchange two characters at p and q position
            chars[p], chars[q] = chars[q], chars[p]
            p += 1
            q -= 1

        text = ''.join(chars).strip(' ')
        words = text.split()

        return ' '.join([word[::-1] for word in words])


if __name__ == "__main__":
    s = "hi!"
    res = Solution().reverseWords(s)
    print res
