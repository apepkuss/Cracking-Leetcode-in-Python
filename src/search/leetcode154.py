
class Solution(object):
    def findMin_RecursiveBS(self, nums): # RT: O(logn), the worse case in O(n) time
        n = len(nums)
        minval = nums[0]
        if n==1 or nums[0]<nums[-1]:
            return minval
        start, end = 0, n-1
        while start <= end:
            mid = (start+end)/2
            minval = min(minval, nums[mid])
            if nums[mid] < nums[end]:
                end = mid-1
            elif nums[mid] > nums[end]:
                start = mid+1
            else:
                if start < mid:
                    minval = min(minval, self.findMin_RecursiveBS(nums[start:mid+1]))
                if mid+1 < end:
                    minval = min(minval, self.findMin_RecursiveBS(nums[mid+1:end+1]))
                break
        return minval

    def findMin_IterativeBS(self, nums):  # RT: O(logn), the worse case in O(n) time
        n = len(nums)
        minval = nums[0]
        if n == 1 or nums[0] < nums[-1]:
            return minval
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) / 2
            minval = min(minval, nums[mid])
            if nums[mid] < nums[end]:
                end = mid - 1
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                while start < mid and nums[start] == nums[mid]:
                    start += 1
                if start < mid: end = mid
                else:
                    while mid < end and nums[mid] == nums[end]:
                        end -= 1
                    if mid < end: start = mid
                    else:
                        break
        return minval
