
class Solution(object):
    """
    @ Amazon

    Backtracking

    The gray code is a binary numeral system where two successive values differ in only one bit.

    Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
    A gray code sequence must begin with 0.

    For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

    00 - 0
    01 - 1
    11 - 3
    10 - 2
    Note:
    For a given n, a gray code sequence is not uniquely defined.

    For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

    For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
    """
    def greyCode_fast(self, n): # RT: O(n)
        res=[]
        size=1<<n
        for i in range(size):
            res.append((i>>1)^i)
        return res

    def greyCode_dp(self, n):
        assert n >= 0

        # dp[i] indicates the sequence of i-bit gray code
        dp = [[0], [0, 1]]

        for i in range(2, n + 1):
            # Example: if dp[-1]=[0,1], then tmp=[0,1,1,0]
            tmp = dp[-1] + dp[-1][::-1]
            k = 1 << (i - 1)
            for j in range(len(tmp) / 2, len(tmp)):
                tmp[j] = tmp[j] ^ k
            dp.append(tmp)
            print('dp[{0}]={1}'.format(i, dp[-1]))

        return dp[n]


if __name__ == "__main__":
    mysolution = Solution()
    res = mysolution.greyCode_dp(3)
    print res
