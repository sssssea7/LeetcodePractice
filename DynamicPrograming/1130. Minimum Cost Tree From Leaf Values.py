# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/description/

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        @cache
        def dfs(i, j):
            if i>=j:
                return 0
            ans = inf
            for k in range(i, j):
                ans = min(ans, dfs(i, k)+dfs(k+1, j)+max([arr[p] for p in range(i,k+1)])*max([arr[q] for q in range(k+1,j+1)]))
            return ans
        return dfs(0, n-1)