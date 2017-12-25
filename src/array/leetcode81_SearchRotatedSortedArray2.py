
class Solution(object):
    """
    Follow up for "Search in Rotated Sorted Array": What if duplicates are allowed?
    Would this affect the run-time complexity? How and why? Write a function to
    determine if a given target is in the array.
    """
    def search(self, nums, target): # RT: O(n), space: O(1)
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums or len(nums) == 0:
            return -1

        # initialization
        start, end = 0, len(nums) - 1

        # binary search with linear search for duplicates
        while start <= end:
            mid = start + (end - start) / 2
            if target == nums[mid]:
                return mid

            # target > nums[mid]
            elif target < nums[mid]:
                if nums[start] <= target:
                    # duplicates
                    while mid - 1 >= start and nums[mid] == nums[mid - 1]:
                        mid -= 1
                    end = mid - 1

                elif nums[mid] >= nums[end]:
                    head = mid + 1

                else:
                    break

            # target < nums[mid]
            else:
                if target <= nums[end]:
                    # duplicates
                    while mid + 1 <= end and nums[mid] == nums[mid + 1]:
                        mid += 1
                    start = mid + 1

                elif nums[start] >= nums[mid]:
                    end = mid - 1

                else:
                    break
        return -1
