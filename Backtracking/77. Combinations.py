# https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            if k-len(path) > n-i+1:      # optimization: if the remaining numbers are not enough to fill the path, stop searching
                return
            if len(path)==k:
                ans.append(path.copy())
                return
            for j in range(i, n+1):
                path.append(j)
                dfs(j+1)
                path.pop()
        dfs(1)
        return ans

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        stack = []
        def dfs(i):
            if len(stack)==k:
                ans.append(stack.copy())
                return
            if i==n+1:
                return
            
            dfs(i+1)

            stack.append(i)
            dfs(i+1)
            stack.pop()
        dfs(1)
        return ans