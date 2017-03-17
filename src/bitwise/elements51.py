
class Elements(object):

    @classmethod
    def compute_parity(cls, bin_word):  # O(n) time
        """
        Compute the parity of a very large number of 64-bit words
        """
        count = 0
        for i in xrange(64):
            if i != 0:
                bin_word >>= 1
            if bin_word & 1 == 1:
                count += 1
        return count

if __name__ == "__main__":
    bin_word = 0xfffff
    res = Elements.compute_parity(bin_word)
    print res

