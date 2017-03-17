
class Solution(object):
    """
    @ Amazon, Google, Zenefits\

    Heap

    Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

    For example,
    Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
    Therefore, return the max sliding window as [3,3,5,5,6,7].

    Note: 
    You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.

    Follow up:
    Could you solve it in linear time?

    Hint:
    How about using a data structure such as deque (double-ended queue)?
    The queue size need not be the same as the window's size.
    Remove redundant elements and the queue should store only elements that need to be considered.
    """
    # method 1
    def maxSlidingWindow_nonlinear(self, nums, k): # TLE: O(nk) time
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        if nums is None or len(nums) == 0:
            return res
        if len(nums)==1 or k==1:
            return nums
        
        for i in range(len(nums)-k+1):
            curr_max = nums[i]
            for j in range(i+1, i+k):
                curr_max = max(curr_max, nums[j])
            res.append(curr_max)
        return res
    
    # method 2
    def maxSlidingWindow_library(self, nums, k): # O(nlogk) time
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        if nums is None or len(nums)==0:
            return res
        if len(nums)==1 or k==1:
            return nums
        
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res
    
    # method 3: SegmentTree
    def maxSlidingWindow_segTree(self, nums, k): # O(nlogn) time
        res = []
        if nums is None or len(nums) == 0:
            return res
        if len(nums)==1 or k==1:
            return nums
        import math
        size = 2 * pow(2, int(math.ceil(math.log(len(nums),2)))) - 1 
        segTree = [None] * size
        self.construct_segTree(segTree, nums, 0, len(nums)-1, 0)
        for i in range(len(nums)-k+1):
            res.append(self.get_maxRangeValue(segTree, i, i+k-1, 0, len(nums)-1, 0))
        return res
    
    def construct_segTree(self, segTree, nums, low, high, pos):  # O(nlogn) time, O(n) space
        if low == high:
            segTree[pos] = nums[low]
        else:
            mid = (low+high)/2
            self.construct_segTree(segTree, nums, low, mid, 2*pos+1)
            self.construct_segTree(segTree, nums, mid+1, high, 2*pos+2)
            segTree[pos] = max(segTree[2*pos+1], segTree[2*pos+2])
    
    def get_maxRangeValue(self, segTree, qlow, qhigh, low, high, pos):  # O(logn) time
        if qlow<=low and qhigh>=high:
            return segTree[pos]
        if qlow > high or qhigh < low:
            import sys
            return -sys.maxint-1
        mid = (low+high)/2
        return max(self.get_maxRangeValue(segTree, qlow, qhigh, low, mid, 2*pos+1), self.get_maxRangeValue(segTree, qlow, qhigh, mid+1, high, 2*pos+2))


    # method 4: scan the array from 0 to n-1, keep indexes of good candidates in deque d. The algorithm is amortized
    # O(n) as each element is put and polled once.
    #
    # The indexes in d (from current window) are increasing, but their corresponding values are decreasing. Then the
    # first deque element is the index of the largest value in current window.
    #
    # For each index i,
    #   1. Pop (from the end) indexes of smaller elements (they'll be useless)
    #   2. Append the current index
    #   3. Pop (from the front) the index i-k, if it's still in the deque (it falls out of the windows)
    #   4. If our window has reached size k, append the current window maximum to the output
    #
    def maxSlidingWindow_deque(self, nums, k):
        import collections
        d = collections.deque()
        res = []

        for i, n in enumerate(nums):
            # 1. pop out indexes of smaller elements from the end (they'll be useless)
            while d and nums[d[-1]] < n:
                d.pop()

            # 2. append the current index
            d.append(i)

            # 3. pop out the index i-k (from the front), if it's still in the deque (it falls out of the windows)
            if d[0] == i - k:
                d.popleft()

            # 4. if our window has reached size k, append the current window maximum to the output
            if i >= k - 1:
                res.append(nums[d[0]])

        return res


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    res = Solution().maxSlidingWindow_deque(nums, k)
    print res
