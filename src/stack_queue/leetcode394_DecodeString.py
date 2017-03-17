
class Solution(object):
    """
    @ Google

    Given an encoded string, return it's decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
    exactly k times. Note that k is guaranteed to be a positive integer.

    You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

    Furthermore, you may assume that the original data does not contain any digits and that digits are only for those
    repeat numbers, k. For example, there won't be input like 3a or 2[4].
    """
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] != ']':
                stack.append(s[i])
            else:
                # get the string
                tmp = ''
                while stack and stack[-1] != '[':
                    tmp = stack[-1] + tmp
                    stack.pop()
                # pop out '['
                stack.pop()

                # get repeat times
                times = ''
                while stack and stack[-1] in '0123456789':
                    times = stack[-1] + times
                    stack.pop()
                times = int(times.lstrip('0'))
                tmp *= times
                stack.append(tmp)
        return ''.join(stack)


if __name__ == "__main__":
    s = "3[a]2[bc]"
    res = Solution().decodeString(s)
    print res