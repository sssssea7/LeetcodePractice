# https://leetcode.com/problems/number-of-provinces/

# union find solution
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        G = {}
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    union(i, j)
        
        return len(set(find(x) for x in parent))

# dfs solution
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
        
    