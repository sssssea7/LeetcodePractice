# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, A: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i, s):
            if len(path)==len(A):
                ans.append(path.copy())
                return
            for x in s:
                path.append(x)
                dfs(i+1, s-{x})
                path.pop()
        dfs(0, set(A))
        return ans

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        def dfs(seq):
            if len(seq) == len(nums): 
                self.ans.append(seq)
                return
            for n in nums:
                if n not in seq:
                    dfs(seq + [n])
        dfs([])
        return self.ans
        