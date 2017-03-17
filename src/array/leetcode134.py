
class Solution(object):
    def canCompleteCircuit(self, gas, cost):    # O(n) time
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        station = 0
        diff = 0
        for i in range(len(gas)):
            if diff+gas[i] < cost[i]:
                station = i+1
                diff = 0
            else:
                diff = diff+gas[i]-cost[i]
        return station
