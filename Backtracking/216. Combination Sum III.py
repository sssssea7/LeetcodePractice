# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, capacity):
            if len(path)==k:
                if capacity==0:
                    ans.append(path.copy())
                return
            if capacity<0 or i>9:
                return
            
            for j in range(i, 10):
                path.append(j)
                dfs(j+1, capacity-j)
                path.pop()

        dfs(1, n)
        return ans

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i, n):
            if n<0 or len(path)>k: return
            if n==0 and len(path)==k:
                ans.append(path.copy())
                return
            for j in range(i, 10):
                path.append(j)
                dfs(j+1, n-j)
                path.pop()
        dfs(1, n)
        return ans


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, capacity):
            if len(path)==k:
                if capacity==0:
                    ans.append(path.copy())
                return
            if capacity<0 or i>9:
                return
            
            dfs(i+1, capacity)
            
            path.append(i)
            dfs(i+1, capacity-i)
            path.pop()

        dfs(1, n)
        return ans