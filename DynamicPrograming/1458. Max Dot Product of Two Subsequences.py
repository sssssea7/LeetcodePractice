# https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        @cache
        def dfs(i, j):
            if i<0 or j<0:
                return -inf
            return max(max(dfs(i-1, j-1), 0)+nums1[i]*nums2[j], dfs(i-1, j), dfs(i, j-1))
        return dfs(n-1, m-1)

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[-inf] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = max(max(dp[i][j], 0)+nums1[i]*nums2[j], dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]