class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        dp = []
        for i in A:
            left = bisect_left(dp, i)
            if left == len(dp): dp.append(i)
            else: dp[left] = i
        return len(dp)