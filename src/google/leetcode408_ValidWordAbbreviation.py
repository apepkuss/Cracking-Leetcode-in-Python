
class Solution(object):
    """
    @ Google
    
    Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

    A string such as "word" contains only the following valid abbreviations:
    ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

    Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

    Note:
    Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

    Example 1:
    Given s = "internationalization", abbr = "i12iz4n":

    Return true.
    Example 2:
    Given s = "apple", abbr = "a2e":

    Return false.
    """
    def validWordAbbreviation(self, word, abbr): # O(n) time
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        chars = "abcdefghijklmnopqrstuvwxyz"
        nums = "0123456789"
        if len(abbr) > len(word):
            return False
        word = word.lower()
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].lower() in chars:
                if abbr[j].lower() == word[i]:
                    i += 1
                    j += 1
                else:
                    return False
            elif abbr[j] == '0':
                return False
            elif abbr[j] in nums:
                k = j
                while k < len(abbr) and abbr[k] in nums:
                    k += 1
                i += int(abbr[j:k])
                j = k
                if j == len(abbr) or i == len(word):
                    break
        return i == len(word) and j == len(abbr)