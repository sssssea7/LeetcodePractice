# https://leetcode.com/problems/count-ways-to-build-good-strings/description/

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        @cache
        def dfs(cur_len):
            if cur_len < low:
                return dfs(cur_len+zero) + dfs(cur_len+one)
            elif cur_len > high:
                return 0
            else:
                return (1 + dfs(cur_len+zero) + dfs(cur_len+one))%(10**9 + 7)
            
        return dfs(0) % (10**9 + 7)

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9+7
        dp = [0] * (high+1+max(zero, one))
        for cur_len in reversed(range(high+1)):
            if cur_len<low:
                dp[cur_len] = dp[cur_len+zero] + dp[cur_len+one]
            elif cur_len>high:
                dp[cur_len] = 0
            else:
                dp[cur_len] = 1 + dp[cur_len+zero] + dp[cur_len+one]
            
        return dp[0]%MOD