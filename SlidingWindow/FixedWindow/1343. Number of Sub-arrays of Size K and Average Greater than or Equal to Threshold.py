# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
class Solution:
    def numOfSubarrays(self, A: List[int], k: int, threshold: int) -> int:
        t = threshold*k
        sm = sum(A[:k])
        ans = 0 if sm<t else 1
        for i in range(k, len(A)):
            sm = sm + A[i] - A[i-k]
            if sm >= t:
                ans += 1
        return ans