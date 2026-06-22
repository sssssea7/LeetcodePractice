# https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        dec_stack = []
        for i in reversed(range(len(heights))):
            while dec_stack and heights[i] > heights[dec_stack[-1]]:
                dec_stack.pop()
                ans[i] += 1
            if dec_stack:
                ans[i] += 1
            dec_stack.append(i)
        return ans


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        dec_stack = []
        for i, h in enumerate(heights):
            while dec_stack and h >= heights[dec_stack[-1]]:
                j = dec_stack.pop()
                ans[j] += 1
            if dec_stack:
                ans[dec_stack[-1]] += 1
            dec_stack.append(i)
        return ans