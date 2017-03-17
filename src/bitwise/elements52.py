
# Two ways to accelerate bit manipulations:
# x & (x-1) equals x with the lowest set bit cleared
# x & ~(x-1) extracts the lowest set bit of x (all other bits are cleared)

class Elements(object):
    """
    A 64-bit integer can be viewed as an array of 64 bits, with the bit at index 0 corresponding to the least
    significant bit (LSB), and the bit at index 63 corresponding to the most significant bit (MSB). Implement
    code that takes as input a 64-bit integer and swaps the bits in that integer at indices i and j.
    """
    def swap_bits(self, n, i, j):
        """
        nums: a 64-bit integer
        i, j: the indices of two bits to swap
        """
        if (n >> i & 1) != (n >> j & 1):
            n ^= 1 << i | 1 << j
        return n

    def swap_integers(self, x, y):
        """
        Swaps two integers without additional memory (based on bit-fiddling idiom)
        x: integer
        y: integer
        """
        if x != y:
            x = x ^ y
            y = y ^ x
            x = x ^ y
        return x, y

if __name__ == "__main__":
    mysolution = Elements()
    n = 154
    print format(n, '08b')
    n = mysolution.swap_bits(n, i=1, j=5)
    print format(n, '08b')
    x, y = mysolution.swap_integers(9, 10)
    print format(x, '08b'), format(y, '08b')
