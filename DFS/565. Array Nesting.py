# https://leetcode.com/problems/array-nesting/
class Solution:
    def arrayNesting(self, A: List[int]) -> int:
        seen = set()
        def dfs(i):
            if A[i] in seen: return 0
            seen.add(A[i])
            return 1+dfs(A[i])
        ans = -inf
        for i in range(len(A)):
            ans = max(ans, dfs(i))
        return ans

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