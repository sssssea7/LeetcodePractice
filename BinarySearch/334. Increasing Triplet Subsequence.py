# https://leetcode.com/problems/increasing-triplet-subsequence/
class Solution:
    def increasingTriplet(self, A: List[int]) -> bool:
        dp = []
        for a in A:
            left = bisect_left(dp, a)
            if left == len(dp): dp.append(a)
            else: dp[left] = a
            if len(dp)==3: return True
        return False
        
class Solution:
    def increasingTriplet(self, A: List[int]) -> bool:
        prefix = []
        suffix = []
        mx, mn = -inf, inf
        for p, s in zip(A, A[::-1]):
            mx = max(s, mx)
            mn = min(p, mn)
            prefix.append(mn)
            suffix.append(mx)
        suffix.reverse()
        for a, p, s in zip(A, prefix, suffix):
            if p<a<s: return True
        return False