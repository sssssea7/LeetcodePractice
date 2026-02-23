# https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, A: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(A)):
            ans += min(abs(A[i][0]-A[i-1][0]), abs(A[i][1]-A[i-1][1])) + abs(abs(A[i][0]-A[i-1][0]) - abs(A[i][1]-A[i-1][1]))
        return ans