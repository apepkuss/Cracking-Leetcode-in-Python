
class Solution(object):
    def searchRange_BS(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin = end = -1
        # find the first occurrence of target in nums
        front, back = 0, len(nums)-1
        while front <= back:
            mid = (front+back)/2
            if nums[mid ] < target:
                front = mid+1
            elif nums[mid] > target:
                back = mid - 1
            else:
                begin = mid
                back = mid - 1

        # if begin is -1, it means there is no target in nums
        if begin == -1:
            return [-1, -1]

        # find the last occurrence of target in nums
        front, back = begin, len(nums) - 1
        while front <= back:
            mid = (front + back)/2
            if nums[mid] < target:
                front = mid + 1
            elif nums[mid] > target:
                back = mid - 1
            else:
                end = mid
                front = mid + 1
        return [begin, end]

    def searchRange_recursive(self, nums, target):
        def dfs(start, end):
            if start > end:
                return [-1, -1]
            if start == end:
                if nums[start] == target:
                    return [start, end]
                else:
                    return [-1, -1]
            mid = (start + end) / 2
            left = dfs(start, mid)
            rite = dfs(mid + 1, end)

            # merge the results
            if left == [-1, -1] and rite == [-1, -1]:
                return [-1, -1]
            elif left == [-1, -1]:
                return rite
            elif rite == [-1, -1]:
                return left
            else:
                return [left[0], rite[1]]

        if nums is None or len(nums) == 0:
            return [-1, -1]
        return dfs(0, len(nums) - 1)

if __name__ == "__main__":
    nums = [2,2]
    target = 2
    res = Solution().searchRange_recursive(nums, target)
    print res