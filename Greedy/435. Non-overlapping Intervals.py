class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x:x[1])
        ans = 0
        j = A[0][1]
        for i in range(1, len(A)):
            if A[i][0]<j: ans += 1
            else: j=A[i][1]
        return ans