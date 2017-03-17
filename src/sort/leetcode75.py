

class Solution(object):
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 0:
            red = white = blue = 0
            for num in nums:
                if num == 0:
                    red += 1
                elif num == 1:
                    white += 1
                elif num == 2:
                    blue += 1
            for i in xrange(len(nums)):
                if i < red:
                    nums[i] = 0
                elif i < red+white:
                    nums[i] = 1
                elif i < red+white+blue:
                    nums[i] = 2


    def sortColors(self, nums):
        if len(nums) <= 1:
            return
        i, j = 0, len(nums) - 1
        while i < len(nums) and nums[i] == 0:
            i += 1
        if i == len(nums):
            return
        while j >= 0 and nums[j] == 2:
            j -= 1
        if j < 0:
            return
        x = i
        while x <= j:
            if nums[x] == 1:
                x += 1
            else:
                if nums[x] == 0:
                    if x == i:
                        x += 1
                    else:
                        nums[i], nums[x] = nums[x], nums[i]
                    i += 1
                elif nums[x] == 2:
                    nums[j], nums[x] = nums[x], nums[j]
                    j -= 1
        return


if __name__ == "__main__":
    nums = [2,0]
    Solution().sortColors(nums)
    print nums