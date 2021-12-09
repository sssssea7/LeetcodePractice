class Solution:
    def canReach(self, A: List[int], s: int) -> bool:
        seen = set()
        def dfs(i):
            if i>=len(A) or i< 0: return
            if A[i] == 0: return True
            if i not in seen: seen.add(i)
            else: return False
            return dfs(i+A[i]) or dfs(i-A[i])         
        return dfs(s)