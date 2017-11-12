
class Solution(object):
    """
    Given a string, find the length of the longest substring T that contains at most k distinct characters.
    For example, Given s = “eceba” and k = 2,
    T is "ece" which its length is 3.

    Hashtable + fast/slow pointers
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Compute the length of longest substring with at most k distinct characters.
        Input:
        - s: the target string
        - k: the number of distinct characters allowed

        Output:
        - maxlen: the length of longest substring with at most k distinct characters
        """
        
        if len(s) < 2: 
            return len(s)

        if k < 0: return -1
    
        # Define two pointers
        fast = slow = 0

        # Define a hash table for storing appeared elements and their index.
        # The size of the hash table is k.
        adict = {}

        # The length of longest substring with at most two distinct characters
        maxlen = 0

        while fast < len(s):
            if len(adict) == k and s[fast] not in adict:
                index = adict[s[slow]] + 1
                del adict[s[slow]]
                slow = index
            
            maxlen = max(maxlen, fast - slow + 1)
            adict[s[fast]] = fast
            fast += 1
        
        return maxlen