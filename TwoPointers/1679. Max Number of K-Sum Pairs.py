# https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution:
    def maxOperations(self, A: List[int], k: int) -> int:
        ans = 0
        i, j = 0, len(A)-1
        A.sort()
        while i<j:
            if A[i]+A[j] == k:
                ans += 1
                i += 1
                j -= 1
            elif A[i]+A[j] < k: 
                i += 1
            else:
                j -= 1
        return ans