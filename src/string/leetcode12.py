

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        if num <= 0: return res

        units = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romans = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        
        for i in xrange(len(units)):
            if num >= units[i]:
                count = num/units[i]
                num = num%units[i]
                res += romans[i]*count
        return res
