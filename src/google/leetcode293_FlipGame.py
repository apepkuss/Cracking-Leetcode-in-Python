

class Solution(object):
    """
    @ Google

    You are playing the following Flip Game with your friend: Given a string that contains only these two characters:
    + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no
    longer make a move and therefore the other person will be the winner.

    Write a function to compute all possible states of the string after one valid move.

    For example, given s = "++++", after one move, it may become one of the following states:

    [
      "--++",
      "+--+",
      "++--"
    ]
    If there is no valid move, return an empty list [].
    """
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) < 2: return res
        i = 0
        while i < len(s)-1:
            if s[i:i+2] == "++":
                res.append(s[:i] + '--' + s[i+2:])
            i += 1
        return res