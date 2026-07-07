# https://leetcode.com/problems/palindrome-partitioning/description/

# enumerate all possible partition, if the current substring is palindrome, then add it to the path and continue to search for the next substring
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

# select or not select, if select, must be palindrome
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        stack = []
        def dfs(i, start):
            if i==n:
                ans.append(stack.copy())
                return
            
            if i<n-1:
                dfs(i+1, start)

            cur = s[start:i+1]
            if cur==cur[::-1]:
                stack.append(cur)
                dfs(i+1, i+1)
                stack.pop()
        dfs(0, 0)
        return ans