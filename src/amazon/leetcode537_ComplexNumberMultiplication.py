
class Solution(object):
    """
    @ Amazon
    
    Math, String
    
    Given two strings representing two complex numbers.

    You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
    
    Example 1:
    Input: "1+1i", "1+1i"
    Output: "0+2i"
    Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
    Example 2:
    Input: "1+-1i", "1+-1i"
    Output: "0+-2i"
    Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
    Note:
    
    The input strings will not have extra blank.
    The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range 
    of [-100, 100]. And the output should be also in this form.
    """
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        re_im = a.split('+')
        re1, im1 = int(re_im[0]), int(re_im[1][:-1])
        re_im = b.split('+')
        re2, im2 = int(re_im[0]), int(re_im[1][:-1])

        re = re1 * re2 - im1 * im2
        im = re1 * im2 + re2 * im1

        return '{0}+{1}i'.format(re, im)
