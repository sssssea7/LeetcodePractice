class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        s = sum(A)
        n = len(A)
        ans = 0
        A = list(accumulate(A, initial=0))
        for i in range(k+1):
            ans = max(ans, s-(A[i+n-k]-A[i]))
        return ans