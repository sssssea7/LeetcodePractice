class Solution:
    def findSubsequences(self, A: List[int]) -> List[List[int]]:
        ans, stk = set(), []
        def dfs(i):
            if len(stk)>1: ans.add(','.join(stk.copy()))
            for j in range(i+1, len(A)):
                if A[j]>=A[i]: 
                    stk.append(str(A[j]))
                    dfs(j)
                    stk.pop()
                    
        for i in range(len(A)):
            stk.append(str(A[i]))
            dfs(i)
            stk.pop()
        return [x.split(',') for x in ans]