

class Solution(object):
    """
    @ Google

    A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

    Write a function to determine if a number is strobogrammatic. The number is represented as a string.

    For example, the numbers "69", "88", and "818" are all strobogrammatic.
    """
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        numbers = ['0', '1', '8']
        n = len(num)
        mid = n / 2
        if n & 1 == 1:
            if num[mid] not in numbers:
                return False
            left, right = mid-1, mid+1
        else:
            left, right = mid-1, mid
        while left >= 0 and right < n:
            if num[left] == num[right] and num[left] in numbers:
                left -= 1
                right += 1
            elif num[left]!=num[right] and ((num[left]=='6' and num[right]=='9') or (num[left]=='9' and num[right]=='6')):
                left -= 1
                right += 1
            else:
                return False
        return True