class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, ans, n0 = 0, 0, 0
        for r in range(len(nums)):
            if nums[r]==0: n0 += 1
            while n0 > k:
                if nums[l] == 0: n0 -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans