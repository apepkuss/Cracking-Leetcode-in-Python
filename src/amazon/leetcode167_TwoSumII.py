
class Solution(object):
    """
    @ Amazon
    
    Given an array of integers that is already sorted in ascending order, find 
    two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that they 
    add up to the target, where index1 must be less than index2. Please note that 
    your returned answers (both index1 and index2) are not zero-based.

    You may assume that each input would have exactly one solution.

    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2
    """
    def twoSum_hashtable(self, numbers, target):  # O(n) time, O(n) space
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        adict = {}
        for i in range(len(numbers)):
            if numbers[i] not in adict:
                adict[numbers[i]] = [i+1]
            else:
                adict[numbers[i]].append(i+1)
                
        for i in range(len(numbers)):
            num = target - numbers[i]
            if num == numbers[i] and len(adict[num])>1:
                return adict[num][0], adict[num][1]
            elif num in adict:
                return adict[numbers[i]][0], adict[num][0]
        return -1, -1

    def twoSum_twoPointers(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if numbers is None or len(numbers) < 2:
            return -1, -1

        left, right = 0, len(numbers) - 1
        while left < right:
            asum = numbers[left] + numbers[right]
            if asum == target:
                return left + 1, right + 1
            elif asum < target:
                left += 1
            else:
                right -= 1
        return -1, -1