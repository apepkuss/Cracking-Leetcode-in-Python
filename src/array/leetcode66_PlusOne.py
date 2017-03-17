
class Solution(object):
    """
    @ Google

    Given a non-negative number represented as an array of digits, plus one to the number.The digits are stored such
    that the most significant digit is at the head of the list.
    """
    def plusOne(self, digits):  # O(n)
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        carry = 1
        for x in xrange(n-1, -1, -1):
            val = digits[x] + carry
            carry = val / 10
            digits[x] = val % 10
        if carry == 1:
            digits = [1] + digits
        return digits
