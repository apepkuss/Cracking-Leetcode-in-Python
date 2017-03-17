

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0: return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0 for _ in xrange(n)]
        maxarea = 0
        for i in xrange(m):
            for j in xrange(n):
                heights[j] = heights[j]+1 if matrix[i][j]=='1' else 0
            maxarea = max(maxarea, self.largestRectangleArea(heights))
        return maxarea

    def largestRectangleArea(self, heights):
        """
        Compute the largest rectangle area in current row
        """
        stack=[]; area = 0
        i = 0
        while i<len(heights):
            if stack==[] or heights[i]>heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i if stack==[] else i-stack[-1]-1
                area = max(area, width * heights[top])
        while len(stack) > 0:
            top = stack.pop()
            width = i if stack==[] else len(heights) - stack[-1] - 1
            area = max(area, width * heights[top])
        return area
