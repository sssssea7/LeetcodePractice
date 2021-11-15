class Solution:
    def largestDivisibleSubset(self, A: List[int]) -> List[int]:
        A.sort()
        dp = []
        for i in range(len(A)):
            vals = max([dp[j] for j in range(i) if A[i]%A[j]==0], default=[], key=len)
            dp.append(vals+[A[i]])
        return max(dp, key=len)
        