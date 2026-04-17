# https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/description/

class Solution:
    def lengthOfLongestSubsequence(self, A: List[int], target: int) -> int:
        
        @cache
        def dfs(i, c):
            if i==len(A):
                if c==0:
                    return 0
                else:
                    return -inf
            if c<A[i]:
                return dfs(i+1, c)
            return max(dfs(i+1, c), dfs(i+1, c-A[i])+1)
        ans = dfs(0, target)
        dfs.cache_clear()   # avoid memory limit exceeded
        return ans if ans!=-inf else -1

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-inf] * (target+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(n):
            for c in range(target+1):
                if c-nums[i] < 0:
                    dp[i+1][c] = dp[i][c]
                else:
                    dp[i+1][c] = max(1+dp[i][c-nums[i]], dp[i][c])
        ans = dp[-1][-1]
        return ans if ans != -inf else -1