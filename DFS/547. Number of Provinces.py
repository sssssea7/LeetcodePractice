# https://leetcode.com/problems/number-of-provinces/
class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        n = len(A)
        def dfs(i):
            seen.add(i)
            for j in range(n):
                if j not in seen and A[i][j]:
                    dfs(j)
                    
        seen = set()
        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans
        
    