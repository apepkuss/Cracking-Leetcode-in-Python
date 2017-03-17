
class MinStack(object):
    """
    @ Google, Uber, Zenefits, Amazon, Snapchat, Bloomberg

    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.minstack ) ==0 or x<= self.minstack[-1]:
            self.minstack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]