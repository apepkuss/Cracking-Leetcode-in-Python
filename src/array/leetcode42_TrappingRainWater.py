
class Solution(object):
    """
    @ Google, Twitter, Zenefits, Amazon, Apple, Bloomberg

    Array, Stack, Two Pointers

    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
    water it is able to trap after raining.

    For example,
    Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
    """
    def trap(self, height):  # O(n) time, O(n) space
        """
        :type height: List[int]
        :rtype: int
        """
        assert height is not None

        water = 0
        if len(height) <= 2:
            return water

        # leftmost[i] indicates the largest value on the left side of height[i] so far
        leftmost = []
        for i in range(len(height)):
            if not leftmost:
                leftmost.append(height[i])
            else:
                leftmost.append(max(leftmost[-1], height[i]))
        print('left: ', leftmost)

        # rightmost indicates the largest value on the right side of height[i] so far
        rightmost = height[-1]
        for i in range(len(height) - 1, -1, -1):
            print('At {0}, left:{1}, right:{2}, height:{3}'.format(i, leftmost[i], rightmost, height[i]))

            # compute water
            if height[i] < leftmost[i] and height[i] < rightmost:
                water += min(leftmost[i], rightmost) - height[i]
                print('water: ', water)

            # update rightmost
            if height[i] > rightmost:
                rightmost = height[i]
                print('right: ', rightmost)

        return water
