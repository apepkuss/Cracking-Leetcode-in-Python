
class ValidWordAbbr(object):
    """
    @ Google

    An abbreviation of a word follows the form <first letter><number><last letter>.

    Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
    A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

    Example:
    Given dictionary = [ "deer", "door", "cake", "card" ]

    isUnique("dear") -> false
    isUnique("cart") -> true
    isUnique("cane") -> false
    isUnique("make") -> true
    """
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.adict = {}
        for word in dictionary:
            abbr = self.getAbbr(word)
            if abbr in self.adict:
                self.adict[abbr].add(word)
            else:
                self.adict[abbr] = set([word])

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.getAbbr(word)
        if abbr in self.adict:
            if len(self.adict[abbr]) == 1 and word in self.adict[abbr]:
                return True
            else:
                return False
        else:
            return True

    def getAbbr(self, word):
        n = len(word)
        if n <= 2:
            return word
        return word[0] + str(n - 2) + word[n - 1]


if __name__ == "__main__":
    dictionary = ["hello"]
    vwa = ValidWordAbbr(dictionary)
    res = vwa.isUnique("hello")
    print res

