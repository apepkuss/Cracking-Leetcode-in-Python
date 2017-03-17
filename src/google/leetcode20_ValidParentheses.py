

class Solution(object):
    """
    @ Google, Airbnb, Facebook, Twitter, Zenefits, Amazon, Microsoft, Bloomberg
    
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
    valid.The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in s:
            if x in '([{': stack.append(x)
            else:
                if stack==[]: return False
                top = stack.pop()
                if (top == '(' and x == ')') or \
                   (top == '[' and x == ']') or \
                   (top == '{' and x == '}'):
                    continue
                else:
                    return False
        if stack != []:
            return False
        return True


if __name__ == "__main__":
    print Solution().isValid("sdkjfajfajo")