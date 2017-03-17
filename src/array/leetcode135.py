
class Solution(object):
    def candy(self, ratings):   # RT: O(n)
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candynum = [1 for _ in range(n)]

        for i in xrange(1, n):
            if ratings[i] > ratings[i-1]:
                candynum[i] = candynum[i-1] + 1

        for i in xrange(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candynum[i] <= candynum[i+1]:
                candynum[i] = candynum[i+1] + 1

        return sum(candynum)
