import unittest

class Elements(object):
    """
    elements 14.3:

    Given a string, print in alphabetical order each character that appears in the string, and the number
    of times that it appears. For example, if the string is "bcdacebe", output "(a,1),(b,2),(c,2),(d,1),(e,2)"
    """

    @classmethod
    def compute_frequency_array(cls, text):  # O(n) time, but needs extra space for the auxiliary array
        """
        This algorithm is better when text contains English characters only, as it just needs an array of length 26.
        If the characters in text are not restricted to English characters, it would be better to use hash table or
        dictionary instead of array, because Chinese, for example, has over 8000 distinct character.
        """
        res = ""
        if len(text) == 0:
            return res

        table = [0 for _ in xrange(26)]
        for char in text:
            table[ord(char)-97] += 1

        for i in xrange(26):
            if table[i] > 0:
                res += "(" + chr(i+97) + "," + str(table[i]) +"),"
        return res[0:-1]


class TestRune(unittest.TestCase):

    def test_case1(self):
        text = "bcdacebe"
        res = Elements.compute_frequency_array(text)
        unittest.TestCase.assertEqual(self, first="(a,1),(b,2),(c,2),(d,1),(e,2)", second=res)


if __name__ == "__main__":
    unittest.main()