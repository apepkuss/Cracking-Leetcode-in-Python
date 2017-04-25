
class Solution:
    """
    @ Apple, Airbnb
    
    Bit Manipulation
    
    Reverse bits of a given 32 bits unsigned integer.

    For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
    return 964176192 (represented in binary as 00111001011110000010100101000000).
    
    Follow up:
    If this function is called many times, how would you optimize it?
    """
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return n
        res = 0
        for _ in range(32):
            res <<= 1
            if n & 1:
                res |= 1
            n >>= 1
        return res




