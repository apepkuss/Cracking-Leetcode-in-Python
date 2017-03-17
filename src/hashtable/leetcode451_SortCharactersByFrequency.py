


class Solution(object):
    """
    @ Amazon, Google

    Hash Table, Heap

    Given a string, sort it in decreasing order based on the frequency of characters.

    Example 1:

    Input:
    "tree"

    Output:
    "eert"

    Explanation:
    'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
    """
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        adict = {}
        for c in s:
            if c not in adict:
                adict[c] = 1
            else:
                adict[c] += 1
        # sort keys by values
        sorted_keys = sorted(adict, key=lambda x : adict[x], reverse=True)
        for k in sorted_keys:
            res += k * adict[k]
        return res