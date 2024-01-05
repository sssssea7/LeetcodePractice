# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        i = 0
        ans = 0
        k = 1        
        for j in range(len(A)):
            k -= (A[j]==0)
            while k<0:
                k += (A[i]==0)
                i += 1
            ans = max(ans, j-i)
        return ans 