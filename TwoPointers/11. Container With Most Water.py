class Solution:
    def maxArea(self, A: List[int]) -> int:
        ans = 0
        i, j = 0, len(A)-1
        while i<j:
            if A[i]<A[j]:
                ans = max(ans, (j-i)*A[i])
                i += 1
            else:
                ans = max(ans, (j-i)*A[j])
                j -= 1
        return ans
            