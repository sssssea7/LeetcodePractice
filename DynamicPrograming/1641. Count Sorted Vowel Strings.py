class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1]*5
        if n == 1: return 5
        for i in range(n-1):
            dp[0] = sum(dp)
            dp[1] = sum(dp[1:])
            dp[2] = sum(dp[2:])
            dp[3] = sum(dp[3:])
        return sum(dp)


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for _ in range(n):
            for i in range(1, 5):
                dp[i] += dp[i-1]
        return dp[-1]