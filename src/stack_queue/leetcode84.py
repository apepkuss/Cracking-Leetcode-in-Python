

class Solution(object):
    def largestRectangleArea(self, heights):  # RT: O(n)
        n = len(heights)
        maxarea, area = 0, 0
        stack = []
        x = 0
        while x < n:
            if stack == [] or (heights[stack[-1]] <= heights[x]):
                stack.append(x)
                x += 1
            else:
                top = stack.pop()
                if stack == []:
                    area = heights[top] * x
                else:
                    area = heights[top] * (x-stack[-1]-1)
                maxarea = max(maxarea, area)

        while stack != []:
            top = stack.pop()
            if stack == []:
                area = heights[top] * x
            else:
                area = heights[top] * (x-stack[-1]-1)
            maxarea = max(maxarea, area)
        return maxarea

if __name__ == "__main__":
    mysolution = Solution()
    res = mysolution.largestRectangleArea([3,6,5,7,4,8,1,0])