# https://leetcode.com/problems/count-dominant-indices/description/

class Solution:
    def dominantIndices(self, A: List[int]) -> int:
        suf = list(accumulate(A[::-1]))[::-1]
        ans = 0
        for i in range(len(A)-1):
            if A[i] > suf[i+1]/(len(A)-i-1):
                ans += 1
        return ans