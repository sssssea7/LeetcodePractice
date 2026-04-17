# https://leetcode.com/problems/coin-change-ii/description/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def dfs(i, c):
            if i<0:
                return 1 if c==0 else 0
            if c-coins[i] < 0:
                return dfs(i-1, c)
            return dfs(i, c-coins[i]) + dfs(i-1, c)
        return dfs(n-1, amount)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n):
            for c in range(amount+1):
                if c-coins[i]<0:
                    dp[i+1][c] = dp[i][c]
                else:
                    dp[i+1][c] = dp[i+1][c-coins[i]] + dp[i][c]
        return dp[n][amount]