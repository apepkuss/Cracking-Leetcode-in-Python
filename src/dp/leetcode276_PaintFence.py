
class Solution(object):
    """
    @ Google

    There is a fence with n posts, each post can be painted with one of the k colors.

    You have to paint all the posts such that no more than two adjacent fence posts have the same color.

    Return the total number of ways you can paint the fence.

    Note:
    n and k are non-negative integers.
    """
    def numWays_dfs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def dfs(n, sameColor):
            if n == 1:
                if sameColor:
                    return 1
                else:
                    return k- 1
            if sameColor:
                return 1 * dfs(n - 1, False)
            else:
                return (k - 1) * (dfs(n - 1, True) + dfs(n - 1, False))

        if n == 0 or k == 0: return 0
        if n == 1: return k
        return k * (dfs(n - 1, True) + dfs(n - 1, False))

    def numWays_dp1(self, n, k): # O(n**2) time, O(n**2) space
        if n == 0 or k == 0: return 0
        if n == 1: return k
        table = [[0] * n for _ in range(n)]
        table[0][0] = k
        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                if i == n - 1:
                    if j & 1 == 1:
                        table[i][j] = 1
                    else:
                        table[i][j] = k - 1
                elif i == 0:
                    table[i][j] = k * (table[i+1][j] + table[i+1][j+1])
                else:
                    if j & 1 == 1:
                        table[i][j] = table[i + 1][j + 1]
                    else:
                        table[i][j] = (k - 1) * (table[i + 1][j] + table[i + 1][j + 1])
        return table[0][0]

    def numWays_dp2(self, n, k): # O(n**2) time, O(n) space
        if n == 0 or k == 0: return 0
        if n == 1: return k

        table = [0] * n
        for i in range(n):
            if i & 1 == 1:
                table[i] = 1
            else:
                table[i] = k-1

        for j in range(0, n-2):
            for i in range(n-j-1):
                if i & 1 == 1:
                    table[i] = table[i+1]
                else:
                    table[i] = (k-1) * (table[i] + table[i+1])
        return k * (table[0] + table[1])


if __name__ == "__main__":
    n, k = 3, 4
    res = Solution().numWays_dp2(n, k)
    print res
