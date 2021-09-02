class Solution:
    def arrayNesting(self, nums: List[int]) -> int: 
        def dfs(k, s):
            if nums[k] in s: return
            s.add(nums[k])
            self.d += 1
            dfs(nums[k], s)

        ans = 0
        s = set()
        for n in nums:
            self.d = 0
            dfs(n, s)
            ans = max(self.d, ans)
        return ans