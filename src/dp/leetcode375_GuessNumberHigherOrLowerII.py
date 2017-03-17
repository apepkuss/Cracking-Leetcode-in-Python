
class Solution(object):
    """
    @ Google

    We are playing the Guess Game. The game is as follows:

    I pick a number from 1 to n. You have to guess which number I picked. Every time you guess wrong, I'll tell you
    whether the number I picked is higher or lower. However, when you guess a particular number x, and you guess
    wrong, you pay $x. You win the game when you guess the number I picked.

    Example:

    n = 10, I pick 8.

    First round:  You guess 5, I tell you that it's higher. You pay $5.
    Second round: You guess 7, I tell you that it's higher. You pay $7.
    Third round:  You guess 9, I tell you that it's lower. You pay $9.

    Game over. 8 is the number I picked.

    You end up paying $5 + $7 + $9 = $21.
    Given a particular n >= 1, find out how much money you need to have to guarantee a win.

    Hint:

    1. The best strategy to play the game is to minimize the maximum loss you could possibly face. Another strategy is
       to minimize the expected loss. Here, we are interested in the first scenario.
    2. Take a small example (n = 3). What do you end up paying in the worst case?
    3. Check out this article if you're still stuck.
    4. The purely recursive implementation of minimax would be worthless for even a small n. You MUST use dynamic
       programming.
    5. As a follow-up, how would you modify your code to solve the problem of minimizing the expected loss, instead of
       the worst-case loss?
    """
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # table[i][j] indicates the minimum amount of money we need to guarantee a win
        table = [[0] * ( n +1) for _ in range( n +1)]
        self.solve(table, 1, n)
        return table[1][n]

    def solve(self, table, start, end):
        if start >= end:
            return 0
        if table[start][end]:
            return table[start][end]
        table[start][end] = min \
            (x + max(self.solve(table, start, x- 1), self.solve(table, x + 1, end)) for x in range(start, end + 1))
        return table[start][end]
