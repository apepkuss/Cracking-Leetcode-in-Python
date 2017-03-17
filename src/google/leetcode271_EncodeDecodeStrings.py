
class Codec:
    """

    Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and
    is decoded back to the original list of strings.

    Note:
    1. The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be
       generalized enough to work on any possible characters.
    2. Do not use class member/global/static variables to store states. Your encode and decode algorithms should
       be stateless.
    3. Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode
       algorithm.
    """
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        # Encoding rule: len_1.len_2. ... .len_k#str_1str_2...str_k
        n = len(strs)
        if n == 0:
            return ''
        lenstr = ''
        encoded_str = ''
        for s in strs:
            lens = str(len(s))
            lenstr += lens + '.'
            encoded_str += s
        encoded_str = lenstr[:-1] + '#' + encoded_str
        return encoded_str

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) > 0:
            # find the index of delimiter
            idx = s.find('#')
            lenstr = s[:idx]
            encoded_str = s[idx+1:]
            idx = 0
            for lstr in lenstr.split('.'):
                l = int(lstr)
                res.append(encoded_str[idx: idx +l])
                idx += l
        return res


if __name__ == "__main__":
    strs = ["0"]
    codec = Codec()
    encoded = codec.encode(strs)
    print encoded
    decoded = codec.decode(encoded)
    print decoded

