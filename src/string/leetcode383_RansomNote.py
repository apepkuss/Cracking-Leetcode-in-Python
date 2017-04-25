
class Solution(object):
    """
    @ Apple
    
    String
    
    Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

    Each letter in the magazine string can only be used once in your ransom note.
    
    Note:
    You may assume that both strings contain only lowercase letters.
    
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
    """
    def canConstruct(self, ransomNote, magazine):  # O(n) time, O(m) space, where n is length of magazine, m is length of ransomNote
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m, n = len(ransomNote), len(magazine)

        if m > n: return False
        if m == 0: return True

        # keep info of characters in ransomNote, as ransomNote has less characters than magazine
        adict = {}

        for c in ransomNote:
            if c not in adict:
                adict[c] = 1
            else:
                adict[c] += 1

        for c in magazine:
            if c in adict:
                adict[c] -= 1
                if adict[c] == 0:
                    adict.pop(c)
                    if len(adict) == 0:
                        return True
        return False


if __name__ == "__main__":
    ransomNote = "bjaajgea"
    magazine = "affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec"
    res = Solution().canConstruct(ransomNote, magazine)
    print res
