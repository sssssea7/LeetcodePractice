# https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        
        @cache
        def dfs(i, j):
            if i==len(s1):
                return len(s2)-j
            if j==len(s2):
                return len(s1)-i
            if s1[i]==s2[j]:
                return dfs(i+1, j+1)
            return min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))+1

        return dfs(0, 0)