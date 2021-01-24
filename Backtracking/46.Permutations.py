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
        