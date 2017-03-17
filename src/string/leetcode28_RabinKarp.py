

class Solution(object):
    def strStr_RabinKarp(self, haystack, needle):  # O(m*n) time, O(1) space
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        if n == 0: return 0
        if m < n: return -1

        keys = list('abcdefghijklmnopqrstuvwxyz')
        values = [i+1 for i in xrange(26)]
        self.value_dict = dict(zip(keys, values))

        # set up a prim number, which can be any prime number
        prime = 3
        # compute the hash number of the pattern, needle
        hash_needle = self.get_hash(needle, prime)

        res = []
        hash_value = self.get_hash(haystack[0:n], prime)
        if hash_needle == hash_value:
            res.append(0)
        for i in xrange(1, m-n+1):
            hash_value = (hash_value - self.value_dict[haystack[i-1]]) / prime
            hash_value += self.value_dict[haystack[i+n-1]] * pow(prime, (n-1))
            if hash_needle == hash_value:
                res.append(i)

        if res == []:
            return -1
        else:
            return res[0]

    def get_hash(self, text, prime):
        hashcode = 0
        for i in xrange(len(text)):
            hashcode += self.value_dict[text[i]] * pow(prime, i)
        return hashcode


if __name__ == "__main__":
    mysolution = Solution()
    res = mysolution.strStr_RabinKarp("aaa", "aa")
    print res
