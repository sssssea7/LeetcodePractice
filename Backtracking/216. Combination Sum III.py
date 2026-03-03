# https://leetcode.com/problems/combination-sum-iii/

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
        def fn(cur, n, i):
            if n<0 or len(cur)>k: return
            if n==0 and len(cur)==k: return ans.append(cur)
            for j in range(i, 10):
                fn(cur+[j], n-j, j+1)
        fn([], n, 1)
        return ans