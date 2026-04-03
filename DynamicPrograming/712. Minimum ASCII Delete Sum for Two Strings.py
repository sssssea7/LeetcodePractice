# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @cache
        def dfs(i, j):
            if i==len(s1):
                return sum([ord(s2[idx]) for idx in range(j, len(s2))])
            if j==len(s2):
                return sum([ord(s1[idx]) for idx in range(i, len(s1))])
            if s1[i]==s2[j]:
                return dfs(i+1, j+1)
            return min(dfs(i+1, j)+ord(s1[i]), dfs(i, j+1)+ord(s2[j]))
        return dfs(0, 0)