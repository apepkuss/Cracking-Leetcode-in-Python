
import random

class Solution(object):
    """
    @ Google

    Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

    Example:
    (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
    (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

    Note:
    You may assume all input has valid answer.

    Follow Up:
    Can you do it in O(n) time and/or in-place with O(1) extra space?
    """
    def wiggleSort(self, nums): # O(n) time on average, O(1) space
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        print 'n = ' + str(n)
        if n <= 1:
            return
        # quick-select: find the medium value in nums
        medium = self.findKthElement(nums, 0, n - 1, n / 2)

        # three-way partition: medium works as pivot
        # i for tracking odd position, k for tracking even position
        i, j, k = 0, 0, n-1
        while j <= k:
            # put all values bigger than pivot at odd position, e.g. 1,3,5,7,9
            if nums[(2*j+1) % (n|1)] > medium:
                nums[(2*i+1) % (n|1)], nums[(2*j+1) % (n|1)] = nums[(2*j+1) % (n|1)], nums[(2*i+1) % (n|1)]
                self.print_arr(nums, (2*i+1) % (n|1), (2*j+1) % (n|1))
                i += 1
                j += 1
            # put all values smaller than pivot at even position,
            elif nums[(2*j+1) % (n|1)] < medium:
                nums[(2*j+1) % (n|1)], nums[(2*k+1) % (n|1)] = nums[(2*k+1) % (n|1)], nums[(2*j+1) % (n|1)]
                self.print_arr(nums, (2*j+1) % (n|1), (2*k+1) % (n|1))
                k -= 1

            else:
                j += 1

    def findKthElement(self, nums, first, last, k): # O(n) time on average, same as QuickSelect
        pivot = self.partition(nums, first, last)
        if pivot == k:
            return nums[pivot]
        elif pivot > k:
            return self.findKthElement(nums, first, pivot - 1, k)
        else:
            return self.findKthElement(nums, pivot + 1, last, k)

    def partition(self, nums, first, last):
        pivot = random.randint(first, last)
        nums[pivot], nums[last] = nums[last], nums[pivot]
        for i in range(first, last):
            if nums[i] > nums[last]:
                nums[i], nums[first] = nums[first], nums[i]
                first += 1
        nums[first], nums[last] = nums[last], nums[first]
        return first

    def print_arr(self, nums, idx1 = None, idx2 = None):
        if idx1 and idx2:
            res = ''
            for i in range(len(nums)):
                if i == idx1 or i == idx2:
                    res += ', ' + '*'+str(nums[idx1])+'*'
                else:
                    res += ', ' + str(nums[i])
            print res[2:]
        else:
            res = ', '.join([str(c) for c in nums])
            print res


if __name__ == "__main__":
    nums = [1,5,1,1,2,3,2,2,2,2,6,4]
    Solution().wiggleSort(nums)
    print nums


