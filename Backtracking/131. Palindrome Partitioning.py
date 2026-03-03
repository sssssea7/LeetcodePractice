# https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        def dfs(i):
            if i==len(s):
                ans.append(path.copy())
                return
            for j in range(i, len(s)):
                cur = s[i:j+1]
                if cur==cur[::-1]:
                    path.append(cur)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans