
class Solution(object):
    """
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2). You are given a target value
    to search. If found in the array return its index, otherwise return -1. You may
    assume no duplicate exists in the array.
    """
    def search(self, nums, target): # O(logn) time, O(1) space
        """
        :type nums: List[int]
        :type target: int
        :rtype int
        """
        if not nums or len(nums) == 0:
            return -1

        head, tail = 0, len(nums) - 1
        while head <= tail:
            mid = head + (tail - head) / 2

            print('head: ', head)
            print('tail: ', tail)
            print('mid: ', mid)
            print('num[%d]=%d' % (mid, nums[mid]))
            print('\n')

            if nums[mid] == target:
                return mid

            # target > nums[mid]
            elif target > nums[mid]:
                if nums[tail] >= target:
                    head = mid + 1

                elif nums[head] >= nums[mid]:
                    tail = mid - 1

                else:
                    break

            # target < nums[mid]
            else:
                if nums[head] <= target:
                    tail = mid - 1

                elif nums[mid] >= nums[tail]:
                    head = mid + 1

                else:
                    break

        return -1


