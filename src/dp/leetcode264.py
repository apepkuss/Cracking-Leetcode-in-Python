
class Solution(object):

    def nthUglyNumber(self, n):  # O(n) time, O(n) space
        """
        :type n: int
        :rtype: int
        """
        if n== 0: return 0
        if n == 1: return 1
        target = 1
        x2, x3, x5 = [], [], []
        for i in range(n - 1):
            x2.append(target * 2)
            x3.append(target * 3)
            x5.append(target * 5)
            target = min(x2[0], x3[0], x5[0])

            # remove the duplicates
            if target == x2[0]: x2.pop(0)
            if target == x3[0]: x3.pop(0)
            if target == x5[0]: x5.pop(0)
        return target

