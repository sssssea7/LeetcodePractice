class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        @cache
        def fn(i):
            if i>=len(A): return 0
            ans = 0
            for j in range(i):
                if A[j]<A[i]:
                    ans = max(ans, fn(j))
            return ans+1
        return max(fn(i) for i in range(len(A)))