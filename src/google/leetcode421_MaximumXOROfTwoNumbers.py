
class TrieNode(object):
    def __init__(self):
        self.children = [None, None]

class Solution(object):
    """
    @ Google
    
    Given a list of numbers, a[0], a[1], a[2],..., a[N-1], where 0 <= a[i] < 2^32. Find the maximum result of a[i] XOR a[j].

    Could you do this in O(n) runtime?

    Input: [3, 10, 5, 25, 2, 8]
    Output: 28
    """
    def findMaximumXOR_bitwise(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxval, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = set()
            for num in nums:
                prefixes.add(num & mask)

            tmp = maxval | (1 << i)
            # in each iteration, there are pair(s) whose left bits can XOR to maxval
            for prefix in prefixes:
                if tmp ^ prefix in prefixes:
                    maxval = tmp
                    break
        return maxval

    def findMaximumXOR_Trie(self, nums):  # TLE
        if nums is None or len(nums) == 0:
            return 0
        # build up a trie
        root = TrieNode()
        for num in nums:
            curr_node = root
            for i in range(31, -1, -1):
                curr_bit = (num >> i) & 1
                if curr_node.children[curr_bit] is None:
                    curr_node.children[curr_bit] = TrieNode()
                curr_node = curr_node.children[curr_bit]
        import sys
        maxval = -sys.maxint - 1
        for num in nums:
            curr_node = root
            curr_maxval = 0
            for i in range(31, -1, -1):
                curr_bit = (num >> i) & 1
                if curr_node.children[curr_bit ^ 1]:
                    curr_maxval += (1 << i)
                    curr_node = curr_node.children[curr_bit ^ 1]
                else:
                    curr_node = curr_node.children[curr_bit]
            maxval = max(maxval, curr_maxval)
        return maxval