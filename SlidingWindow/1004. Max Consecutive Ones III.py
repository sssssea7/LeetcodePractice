# https://leetcode.com/problems/max-consecutive-ones-iii/
class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        i = 0
        ans = 0
        for j in range(len(A)):
            k -= (A[j]==0)
            while k<0:
                k += (A[i]==0)
                i += 1
            ans = max(ans, j-i+1)
        return ans

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


