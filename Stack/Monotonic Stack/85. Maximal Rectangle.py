# https://leetcode.com/problems/maximal-rectangle/description/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int: # problem 84
        n = len(heights)
        left = [-1] * n
        stack = []
        for i, h in enumerate(heights):
            while stack and h <= heights[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        right = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        ans = 0
        for h, l , r in zip(heights, left, right):
            ans = max(ans, h * (r-l-1))
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0]) 
        heights = [0] * m
        ans = 0
        for row in matrix:
            for i in range(m):
                if row[i]=="0":
                    heights[i] = 0
                else:
                    heights[i] += 1
            ans = max(ans, self.largestRectangleArea(heights))
        return ans