
class Solution(object):
    """
    @ Amazon, Dropbox, Google, Uber, Facebook

    Given a digit string, return all possible letter combinations that the number could represent.
    A mapping of digit to letters (just like on the telephone buttons) is given below.
    """
    def letterCombinations_iterative(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if len(digits) == 0: return res
        
        adict = {'0':' ', '1':'*', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        for i in digits:
            if res == []:
                for x in adict[i]:
                    res.append(x)
            else:
                tmp = []
                for k in xrange(len(res)):
                    for x in adict[i]:
                        tmp.append(res[k]+x)
                res = tmp
        return res
    


    def letterCombinations_dfs(self, digits):
        def dfs(start, valuelist):
            if start == len(digits):
                res.append(valuelist)
                return
            d = digits[start]
            for x in adict[d]:
                dfs(start+1, valuelist+x)
        
        res = []
        if len(digits) == 0:
            return res
        adict = {'0':' ', '1':'*', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        dfs(0, "")
        return res