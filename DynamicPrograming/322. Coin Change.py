# https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, A: List[int], t: int) -> int:
        @cache
        def dfs(i, c):
            if i==len(A):
                if c==0:
                    return 0
                else:
                    return inf
            if c<0:
                return inf
            return min(dfs(i, c-A[i])+1, dfs(i+1, c))
        ans = dfs(0, t)
        return ans if ans!=inf else -1