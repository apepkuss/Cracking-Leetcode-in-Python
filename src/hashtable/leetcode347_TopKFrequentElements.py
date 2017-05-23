
import heapq

class Solution(object):
    """
    @ Pocket Gem, Yelp
    
    Hash Table, Heap
    
    Given a non-empty array of integers, return the k most frequent elements.

    For example,
    Given [1,1,1,2,2,3] and k = 2, return [1,2].
    
    Note: 
    You may assume k is always valid, 1 <= k <= number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    """
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []

        if not nums: return res

        # count frequency of each element in nums
        adict = {}
        for num in nums:
            if num not in adict:
                adict[num] = 1
            else:
                adict[num] += 1

        # declare and construct a min heap
        heap = []
        for key, value in adict.items():
            heapq.heappush(heap, (value, key))

        # pop out the first k elements from heap
        for value, key in heapq.nlargest(k, heap, key=lambda x: x[0]):
            res.append(key)

        return res


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    res = Solution().topKFrequent(nums, k)
    print res