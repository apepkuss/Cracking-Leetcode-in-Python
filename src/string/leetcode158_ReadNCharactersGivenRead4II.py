
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
def read4(self, buf4):
    """API"""
    return 0

class Solution(object):
    """
    @ Bloomberg, Google, Facebook

    String

    The API: int read4(char *buf) reads 4 characters at a time from a file.

    The return value is the actual number of characters read. For example,
    it returns 3 if there is only 3 characters left in the file.

    By using the read4 API, implement the function int read(char *buf, int n)
    that reads n characters from the file.

    Note:
    The read function may be called multiple times.
    """
    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while True:
            buf4 = [''] * 4
            l = read4(buf4)
            self.queue.extend(buf4)
            curr = min(len(self.queue), n- i)
            if curr == 0: break
            for _ in range(curr):
                buf[i] = self.queue.pop(0)
                i += 1
        return i




