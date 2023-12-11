class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        ans, cnt, n = A[0], 1, len(A)
        for i in range(n-1):
            if cnt>n//4: return ans
            if A[i]==A[i+1]: 
                cnt += 1
            else:
                ans = A[i+1]
                cnt = 1
        return ans