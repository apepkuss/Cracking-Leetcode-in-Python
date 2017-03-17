
class Solution(object):
    def majorityElement_dict(self, nums):  # RT: O(n), Space: O(n)
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        res = []
        for key in dict.keys():
            if dict[key] > len(nums)/3:
                res.append(key)
        return res

    def majorityElement_BM(self, nums):  # RT: O(n), Space: O(1)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        x, count1 = None, 0
        y, count2 = None, 0
        for num in nums:
            if num == x:
                count1 += 1
            elif num == y:
                count2 += 1
            elif count1 == 0:
                x, count1 = num, 1
            elif count2 == 0:
                y, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        return [i for i in (x, y) if nums.count(i) > n/3]
