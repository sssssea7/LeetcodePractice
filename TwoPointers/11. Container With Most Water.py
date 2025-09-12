# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxArea(self, A: List[int]) -> int:
        i, j = 0, len(A)-1
        ans = 0
        while i<j:
            cur = (j-i) * min(A[i], A[j])
            ans = max(cur, ans)
            if A[i]<A[j]:
                i += 1
            else:
                j -= 1
        return ans