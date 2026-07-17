# https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def dfs(i, capacity):
            if i<0:
                return inf
            if capacity==0:
                return 0
            if capacity-coins[i]<0:
                return dfs(i-1, capacity)
            return min(dfs(i, capacity-coins[i])+1, dfs(i-1, capacity))
        ans = dfs(n-1, amount)
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