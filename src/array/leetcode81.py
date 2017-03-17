
class Solution(object):
    def search(self, nums, target): # RT: O(n), space: O(1)
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        first, last = 0, len(nums)-1
        while first <= last:
            mid = (first+last)/2

            # base case
            if nums[mid] == target: return True

            # recursive step
            if nums[first] < nums[mid]:
                if nums[first] <= target <= nums[mid]:
                    last = mid
                else:
                    first = mid + 1
            elif nums[first] > nums[mid]:
                if nums[mid] <= target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid
            else:
                # deal with duplicates
                first += 1

        return False
