class Solution:
    def longestIncreasingPath(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        @cache
        def dfs(i, j, val):
            ans = 1
            if 0<=i<len(A) and 0<=j<len(A[0]) and A[i][j]>val:
                for dx, dy in D:
                    ans = max(ans, 1+dfs(i+dx, j+dy, A[i][j]))
            else: return 0
            return ans
        
        arr = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                arr.append(dfs(i, j, -1))
        return max(arr)
