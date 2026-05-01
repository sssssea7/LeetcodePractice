# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/



class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i, j, score):
            if i>=j:
                return 0
            ans = 0
            if nums[i]+nums[i+1]==score:
                ans = max(ans, dfs(i+2, j, score)+1)
            if nums[i]+nums[j]==score:
                ans = max(ans, dfs(i+1, j-1, score)+1)
            if nums[j]+nums[j-1]==score: 
                ans = max(ans, dfs(i, j-2, score)+1)
            return ans
        return max(dfs(2, n-1, nums[0]+nums[1]), dfs(1, n-2, nums[0]+nums[n-1]), dfs(0, n-3, nums[-1]+nums[-2])) + 1 # three cases
