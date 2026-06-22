# https://leetcode.com/problems/next-greater-element-ii/description/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums*2
        ans = [-1] * n
        dec_stack = []
        for i in range(n*2):
            while dec_stack and nums[i]>nums[dec_stack[-1]]:
                j = dec_stack.pop()
                if j<n:
                    ans[j] = nums[i]
            dec_stack.append(i)
        return ans