class Solution:
    def canPartition(self, A: List[int]) -> bool:
        if sum(A)&1: return False      # if sum is odd, can't be partitioned into 2 equal subsetsx
        s = sum(A)//2
        @cache
        def dfs(i, cur):
            if i==len(A) or cur<0: return False
            if cur==0: return True
            return dfs(i+1, cur-A[i]) or dfs(i+1, cur)
        return dfs(0, s)