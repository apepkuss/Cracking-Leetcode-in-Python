
class Solution(object):
    """
    There are N gas stations along a circular route, where the amount of gas at
    station i is gas[i]. You have a car with an unlimited gas tank and it costs
    cost[i] of gas to travel from station i to its next station i+1. You begin the
    journey with an empty tank at one of the gas stations. Return the starting gas
    station's index if you can travel around the circuit once, otherwise return -1.
    Note: The solution is guaranteed to be unique.
    """
    def canCompleteCircuit(self, gas, cost):    # O(n) time
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        assert gas is not None
        assert cost is not None

        # total gas volume is not enough for the total cost
        if sum(gas) < sum(cost):
            return -1

        # start driving from first station
        station = 0
        tank = 0
        for i in range(len(gas)):
            # if there is no enough gas from the i-th gas station to
            # next station, just need to move starting point from i
            # to i+1, and verify if we can finish the drive from i+1
            # to the last one. If so, it means we can finish the circuit
            # as the part from the first station to the i-th station has
            # enough gas
            if tank + gas[i] < cost[i]:
                station = i + 1
                tank = 0
            else:
                tank += gas[i] - cost[i]

        return station
