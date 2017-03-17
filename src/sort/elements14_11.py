import unittest


class Elements(object):
    """
    Taking pictures of pairs of opposing teams. All teams have the same number of players. A team photo consists
    of a front row of players and a back row of players. A player in the back row must be taller than the player
    in front of him. All players in a row must be from the same time.

    Deign an algorithm that takes as input two teams and the heights of the players in the teams and checks if it
    is possible to place players to take the photo subject to the placement constraint.
    """

    @classmethod
    def can_take_photo(cls, team1, team2):  # O(nlogn) time
        front = team1
        back = team2

        # sort each team by heights of players
        front.sort()
        back.sort()

        if back[0] <= front[0] or back[-1] <= front[-1]:
            front, back = back, front
            if back[0] <= front[0] or back[-1] <= front[-1]:
                return False

        for i in xrange(1, len(team1)-1):
            if front[i] >= back[i]:
                return False

        return True


class TestRun(unittest.TestCase):

    def test_case1(self):
        heights_of_team1 = [3,6,8,4,7,6,3,6,3,4]
        heights_of_team2 = [2,1,5,3,3,4,2,6,3,3]
        res = Elements.can_take_photo(heights_of_team1, heights_of_team2)
        unittest.TestCase.assertTrue(self, res)


if __name__ == "__main__":
    unittest.main()


