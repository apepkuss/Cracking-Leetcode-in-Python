
class Solution(object):
    """
    @ Amazon
    
    Math, String
    
    Given a list of positive integers, the adjacent integers will perform the float division. 
    For example, [2,3,4] -> 2 / 3 / 4.

    However, you can add any number of parenthesis at any position to change the priority of operations. 
    You should find out how to add parenthesis to get the maximum result, and return the corresponding 
    expression in string format. Your expression should NOT contain redundant parenthesis.
    
    Example:
    Input: [1000,100,10,2]
    Output: "1000/(100/10/2)"
    Explanation:
    1000/(100/10/2) = 1000/((100/10)/2) = 200
    However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
    since they don't influence the operation priority. So you should return "1000/(100/10/2)". 
    
    Other cases:
    1000/(100/10)/2 = 50
    1000/(100/(10/2)) = 50
    1000/100/10/2 = 0.5
    1000/100/(10/2) = 2
    Note:
    
    The length of the input array is [1, 10].
    Elements in the given array will be in range [2, 1000].
    There is only one optimal division for each test case.
    """

    # Regardless of parentheses, every element is either in the numerator or denominator of the final fraction.
    # The expression A[0] / ( A[1] / A[2] / ... / A[N-1] ) has every element in the numerator except A[1], and
    # it is impossible for A[1] to be in the numerator, so it is the largest.

    # Method 1
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        if len(nums) <= 2: return '/'.join(nums)
        return '{}/({})'.format(nums[0], '/'.join(nums[1:]))

    # Method 2
    def optimalDivision_dfs(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums: return ''

        n = len(nums)
        _, res = self.get_max(nums, 0, n-1)
        return res

    def get_max(self, nums, start, end):
        if start == end:
            return nums[start], str(nums[start])

        # for this case, a float result must be returned
        if start + 1 == end:
            return nums[start] * 1.0 / nums[end], str(nums[start]) + '/' + str(nums[end])

        maxval = -1
        expr = ''
        for i in range(start, end):
            numerator, left = self.get_max(nums, start, i)
            denominator, right = self.get_min(nums, i+1, end)
            if maxval < numerator / denominator:
                maxval = numerator / denominator
                expr = left + '/' + ('(' + right + ')' if end - i >= 2 else right)

        return maxval, expr

    def get_min(self, nums, start, end):
        if start == end:
            return nums[start], str(nums[start])

        # for this case, a float result must be returned
        if start + 1 == end:
            return nums[start] * 1.0 / nums[end], str(nums[start]) + '/' + str(nums[end])

        minval = 2**32-1
        expr = ''
        for i in range(start, end):
            numerator, left = self.get_min(nums, start, i)
            denominator, right = self. get_max(nums, i+1, end)
            if minval > numerator / denominator:
                minval = numerator / denominator
                expr = left + '/' + ('(' + right + ')' if end - i >= 2 else right)

        return minval, expr


if __name__ == "__main__":
    nums = [1000,100,10,2]
    res = Solution().optimalDivision_dfs(nums)
    print res
