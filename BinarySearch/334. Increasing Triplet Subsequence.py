class Solution:
    def increasingTriplet(self, A: List[int]) -> bool:
        dp = []
        for a in A:
            left = bisect_left(dp, a)
            if left == len(dp): dp.append(a)
            else: dp[left] = a
            if len(dp)==3: return True
        return False
        