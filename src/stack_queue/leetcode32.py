

class Solution(object):

    def longestValidParentheses(self, s): # RT: O(n), Space: O(n)
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0

        # store the indices of all unmatched left brackets
        stack = []

        # index of the last unmatched right bracket
        last_unmatched_right_bracket = -1

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                # if s[i] is ')'
                if stack == []:
                    last_unmatched_right_bracket = i
                else:
                    stack.pop()
                    if stack == []:
                        # current right bracket - the last unmatched right bracket
                        maxlen = max(maxlen, i - last_unmatched_right_bracket)
                    else:
                        # current right bracket - the last unmatched left bracket
                        maxlen = max(maxlen, i-stack[-1])
        return maxlen

