class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = cnt = 0
        for i in range(2, len(A)):
            if A[i-1]-A[i-2]==A[i]-A[i-1]: cnt += 1
            else: cnt=0
            ans += cnt
        return ans