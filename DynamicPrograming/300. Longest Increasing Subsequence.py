# https://leetcode.com/problems/longest-increasing-subsequence/

# O(nlogn)
# the idea is to maintain a list g where g[i] is the smallest possible tail value of an increasing subsequence of length i+1. For each number x in nums, we can use binary search to find the index i of the smallest number in g that is greater than or equal to x. If such a number exists, we replace it with x; otherwise, we append x to g. The length of g at the end will be the length of the longest increasing subsequence.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []
        for x in nums:
            i = bisect_left(g, x)
            if i==len(g):
                g.append(x)
            else:
                g[i] = x
        return len(g)

# dp: O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            ans = 0
            for j in range(i):
                if nums[i]>nums[j]:
                    ans = max(ans, dfs(j))
            return ans+1
        return max(dfs(i) for i in range(n))

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return max(dp)

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