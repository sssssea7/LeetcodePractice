""" L2: Hash Table + DP
Find left and right endpoint and sequence length then update DP table
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d, ans = {}, 0
        for n in nums:
            if n not in d:
                l = d.get(n-1, 0)
                r = d.get(n+1, 0)
                lens = l + r + 1
                ans = max(ans, lens)
                d[n-l] = d[n] = d[n+r] = lens
        return ans


# sort
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0: return 0
        ans, cur = 1, 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: continue
            if nums[i] == nums[i+1] - 1: cur += 1
            else: 
                ans = max(ans, cur)
                cur = 1
        return max(ans, cur)