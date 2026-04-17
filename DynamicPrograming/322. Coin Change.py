# https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, A: List[int], t: int) -> int:
        @cache
        def dfs(i, c):
            if i==len(A):
                if c==0:
                    return 0
                else:
                    return inf
            if c<0:
                return inf
            return min(dfs(i, c-A[i])+1, dfs(i+1, c))
        ans = dfs(0, t)
        return ans if ans!=inf else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[inf] * (amount+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(n):
            for j in range(amount+1):
                if j-coins[i] < 0:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = min(1+dp[i+1][j-coins[i]], dp[i][j])
        return dp[-1][-1] if dp[-1][-1] != inf else -1