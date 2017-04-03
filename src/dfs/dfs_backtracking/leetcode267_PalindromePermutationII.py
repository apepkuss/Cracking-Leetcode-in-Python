class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        n = len(s)
        if n == 0:
            return res

        # step1: parse s into a hashmap and counter the number of each character in s
        adict = {}
        for c in s:
            if c not in adict:
                adict[c] = 1
            else:
                adict[c] += 1

        # step2: check which characters appear odd times
        key = None
        count = 0
        for k, v in adict.items():
            if v & 1 > 0:
                if count == 0:
                    count += 1
                    key = k

                # if more than one characters appear odd time, it
                # means input s is not a palindrome.
                else:
                    return res

        # step3: initialize values with the character that appears only one time in s.
        values = ''
        if key:
            adict[key] -= 1
            values += key

        # step4: dfs remaining characters with backtracking technique
        self.backtrack(n, adict, values, res)
        return res

    def backtrack(self, total_length, adict, values, res):
        if len(values) == total_length:
            res.append(values)
        else:
            for key in adict.keys():
                if adict[key] > 0:
                    adict[key] -= 2
                    self.backtrack(total_length, adict, key + values + key, res)
                    adict[key] += 2


if __name__ == "__main__":
    s = 'aabb'
    res = Solution().generatePalindromes(s)
    print res



