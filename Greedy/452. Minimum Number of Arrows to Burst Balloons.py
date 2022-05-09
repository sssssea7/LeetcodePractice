class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x:x[1])
        ans = 0
        j = -inf
        for i in range(len(A)):
            if A[i][0]>j: 
                ans+=1
                j=A[i][1]
        return ans