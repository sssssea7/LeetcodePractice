# https://leetcode.com/problems/subarray-product-less-than-k/
class Solution:
    def numSubarrayProductLessThanK(self, A: List[int], k: int) -> int:
        if k<=1: return 0
        i = 0
        ans = 0
        pro = 1
        for j in range(len(A)):
            pro *= A[j]
            while pro >= k:
                pro /= A[i]
                i += 1
            ans += j-i+1
        return ans