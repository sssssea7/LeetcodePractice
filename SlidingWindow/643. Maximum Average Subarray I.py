# https://leetcode.com/problems/maximum-average-subarray-i/
class Solution:
    def findMaxAverage(self, A: List[int], k: int) -> float:
        i, j = 0, k
        mx_sm = sm = sum(A[:k])
        while j<len(A):
            sm = sm-A[i]+A[j]
            mx_sm = max(mx_sm, sm)
            i += 1
            j += 1
        return mx_sm/k

class Solution:
    def findMaxAverage(self, A: List[int], k: int) -> float:
        ans = sm = sum(A[:k])
        for i in range(len(A)-k):
            sm -= A[i]
            sm += A[i+k]
            ans = max(ans, sm)
        return ans/k