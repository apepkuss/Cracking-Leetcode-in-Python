
class Solution(object):
    """
    There are N children standing in a line. Each child is assigned a rating value.
    You are giving candies to these children subjected to the following requirements:
     - Each child must have at least one candy.
     - Children with a higher rating get more candies than their neighbors.
     - What is the minimum candies you must give?
    """
    def candy(self, ratings):   # RT: O(n)
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        # each child gets one candy
        candynum = [1 for _ in range(n)]

        # if current child has higher rating value than left child,
        # then give current child one more candy than left child
        for i in xrange(1, n):
            if ratings[i] > ratings[i-1]:
                candynum[i] = candynum[i-1] + 1

        # if current child has higher rating value than right child,
        # then give current child one more candy than right child
        for i in xrange(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candynum[i] <= candynum[i+1]:
                candynum[i] = candynum[i+1] + 1

        return sum(candynum)
