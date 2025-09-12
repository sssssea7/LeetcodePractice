# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, t: int, A: List[int]) -> int:
        sm = 0
        ans = inf
        i = 0
        for j in range(len(A)):
            sm += A[j]
            while sm >= t:
                ans = min(ans, j-i+1)
                sm -= A[i]
                i += 1
        return ans if ans != inf else 0
