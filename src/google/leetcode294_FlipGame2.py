

class Solution(object):
    """
    @ Google

    You are playing the following Flip Game with your friend: Given a string that contains only these two characters:
    + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no
    longer make a move and therefore the other person will be the winner.

    Write a function to determine if the starting player can guarantee a win.

    For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to
    become "+--+".

    Follow up: Derive your algorithm's runtime complexity.
    """
    def canWin_dp1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def win(s):
            if s not in memo:
                memo[s] = any(s[i: i +2] == '++' and not win(s[:i ] + '-' +s[ i +2:]) for i in range(len(s)))
            return memo[s]

        memo = {}
        return win(s)

    def canWin_dp2(self, s):
        def win(piles):
            piles = tuple(sorted(p for p in piles if p >= 2))
            if piles not in memo:
                memo[piles] = False
                for i, pile in enumerate(piles):
                    for j in range(pile-1):
                        new_piles = piles[:i] + (j, pile-2-j) + piles[i+1:]
                        if not win(new_piles):
                            memo[piles] = True
                            break
                    if memo[piles]: break
            return memo[piles]

        memo = {}
        import re
        piles = map(len, re.findall(r'\+\++', s))
        return win(piles)


if __name__ == "__main__":
    s = "-+++---++--"
    res = Solution().canWin_dp2(s)
    print res