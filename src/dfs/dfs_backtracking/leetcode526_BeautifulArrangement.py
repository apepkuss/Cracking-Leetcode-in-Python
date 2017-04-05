
class Solution(object):
    """
    @ Google
    
    Backtracking, dp
    
    Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these 
    N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

    The number at the ith position is divisible by i.
    i is divisible by the number at the ith position.
    Now given N, how many beautiful arrangements can you construct?
    
    Example 1:
    Input: 2
    Output: 2
    Explanation: 
    
    The first beautiful arrangement is [1, 2]:
    
    Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
    
    Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
    
    The second beautiful arrangement is [2, 1]:
    
    Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
    
    Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
    Note:
    N is a positive integer and will not exceed 15.
    """
    def __init__(self):
        self.count = 0

    # method1: dfs with backtracking
    def countArrangement_dfs(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N > 0:
            used = [False] * ( N +1)
            self.backtrack(N, 1, used)
        return self.count

    def backtrack(self, N, pos, used):
        if pos > N:
            self.count += 1
            return

        for i in range(1, N+1):
            if not used[i] and (i % pos == 0 or pos % i == 0):
                used[i] = True
                self.backtrack(N, pos+ 1, used)
                used[i] = False

    # method2: dfs with memoization
    def countArrangement_dp(self, N):
        """
        :type N: int
        :rtype: int
        """

        def dfs(N, nums, adict):
            if N == 1:
                return 1

            # the key should be a combination of N and nums,
            # as same N could be correlated to different nums.
            key = (N, nums)
            if key in adict:
                return adict[key]

            count = 0
            for i in range(len(nums)):
                if nums[i] % N == 0 or N % nums[i] == 0:
                    count += dfs(N - 1, nums[:i] + nums[i + 1:], adict)
            adict[key] = count
            return adict[key]

        # the type of second argument cannot be a list, as list type
        # cannot be used as part of key of a dictionary
        return dfs(N, tuple(range(1, N + 1)), {})


if __name__ == "__main__":
    N = 4
    res = Solution().countArrangement_dp(N)
    print res

