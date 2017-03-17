

class Solution(object):
    def searchInsert(self, A, target):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid - 1
            else:
                return mid
        return left
