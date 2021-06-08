class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2: return min(cost[0], cost[1])
        dp = [cost[0]] + [cost[1]] + [0]* (len(cost)-2)
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])
        return min(dp[i], dp[i-1])