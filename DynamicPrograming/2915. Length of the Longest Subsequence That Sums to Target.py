# https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/description/

class Solution:
    def lengthOfLongestSubsequence(self, A: List[int], target: int) -> int:
        
        @cache
        def dfs(i, c):
            if i==len(A):
                if c==0:
                    return 0
                else:
                    return -inf
            if c<A[i]:
                return dfs(i+1, c)
            return max(dfs(i+1, c), dfs(i+1, c-A[i])+1)
        ans = dfs(0, target)
        dfs.cache_clear()   # avoid memory limit exceeded
        return ans if ans!=-inf else -1