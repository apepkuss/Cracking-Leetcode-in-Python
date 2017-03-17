

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for x in tokens:
            if stack == [] or x not in '+-*/':
                stack.append(int(x))
            else:
                op1, op2 = stack.pop(), stack.pop()
                if x == '+':
                    stack.append(op1+op2)
                elif x == '-':
                    stack.append(op2-op1)
                elif x == '*':
                    stack.append(op1*op2)
                elif x == '/':
                    # Python2 uses "floor division"
                    # e.g., -1/2=-1, but not 0
                    if op1*op2 < 0:
                        stack.append(-(-op2/op1))
                    else:
                        stack.append(op2/op1)
        return stack.pop()
