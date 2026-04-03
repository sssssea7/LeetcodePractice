# https://leetcode.com/problems/climbing-stairs-ii/description/

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def dfs(i):
            if i==n: return 0
            ans = inf
            if i<n:
                ans = min(ans, dfs(i+1) + costs[i] + 1)
            if i+1<n:
                ans = min(ans, dfs(i+2) + costs[i+1] + 4)
            if i+2<n:
                ans = min(ans, dfs(i+3) + costs[i+2] + 9)
            return ans
        return dfs(0)

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i == 0:
                return 0
            return min(dfs(j) + (i - j) * (i - j) for j in range(max(i - 3, 0), i)) + costs[i - 1]
        return dfs(n)
