

class Solution(object):
    """
    @ Google

    A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

    Each LED represents a zero or one, with the least significant bit on the right.

    Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

    Example:

    Input: n = 1
    Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
    Note:
        The order of output does not matter.
        The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
        The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
    """
    def readBinaryWatch_bitwise(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def dfs(start, k, timer):
            if start == 0:
                hours = timer >> 6
                if hours >= 12: return
                hours = str(hours)
                mins = timer & 0x3f
                if mins >= 60: return
                mins = '0' + str(mins) if 0 <= mins <= 9 else str(mins)
                res.append(hours + ':' + mins)
                return
            for i in range(start-1, k):
                dfs(start-1, i, timer | (1 << i))

        if num == 0: return ['0:00']
        res = []
        dfs(num, 10, 0)
        return res


if __name__ == "__main__":
    num = 2
    res = Solution().readBinaryWatch_bitwise(num)
    print res

