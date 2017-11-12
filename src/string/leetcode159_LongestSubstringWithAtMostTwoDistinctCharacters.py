

class Solution(object):
    """
    Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
    For example, Given s = 'eceba',
    T is 'ece' which its length is 3.

    Hashtable + fast/slow pointers
    """

    def lengthOfLongestSubstringTwoDistinct(self, s):

        # Define two pointers
        fast = slow = 0

        # Define a hash table for storing the elements and their index
        # The size of hash table is 2 according to the question's requirement: 
        # allow at most TWO distinct characters
        adict = {}

        # The length of longest substring with at most two distinct characters
        maxlen = 0

        while fast < len(s):
            if len(adict) == 2 and s[fast] not in adict:
                index = adict[s[slow]] + 1
                del adict[s[slow]]
                slow = index
            
            maxlen = max(maxlen, fast - slow + 1)
            adict[s[fast]] = fast
            fast += 1

            print "After round {0}".format(fast)
            print "hashtable: {0}".format(adict)
            print "fast pointer: {0}".format(fast)
            print "slow pointer: {0}".format(slow)
            print "maxlen: {0}\n".format(maxlen)
        
        return maxlen
                

if __name__ == "__main__":
    sol = Solution()
    res = sol.lengthOfLongestSubstringTwoDistinct('abcabbccc')
    print res

