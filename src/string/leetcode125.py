

class Solution(object):
    def isPalindrome1(self, s): # RT: O(n), Space: O(n)
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        if len(s) <= 1:
            return True

        # only extract alphanumeric characters
        text = [c for c in s.lower() if 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57]
        return text == text[::-1]
