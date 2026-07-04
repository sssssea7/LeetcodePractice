# https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        right = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        ans = 0
        for x, l, r in zip(nums, left, right):
            if l<k<r:
                ans = max(ans, x * (r-l-1))
        return ans
