# https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, A: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            if i==len(A): 
                ans.append(path.copy())
                return
            dfs(i+1)
            path.append(A[i])
            dfs(i+1)
            path.pop()

        dfs(0)
        return ans


class Solution:
    def subsets(self, A: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            ans.append(path.copy())
            if i==len(A): 
                return
            for j in range(i, len(A)):
                path.append(A[j])
                dfs(j+1)
                path.pop()

        dfs(0)
        return ans