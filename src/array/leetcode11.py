
class Solution(object):
    def maxArea(self, height): # RT: O(n)
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right = 0, n-1
        water = 0
        while left < right:
            area = min(height[left], height[right]) * abs(right-left)
            water = max(water, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water
