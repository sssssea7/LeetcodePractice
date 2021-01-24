class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.ans=[]
        def dfs(cand, s, path):
            if s>target: return
            if s==target: self.ans.append(path)
            for i, c in enumerate(cand):
                if s+c>target:break
                dfs(cand[i:], s+c, path+[c])
        dfs(candidates, 0, [])
        return self.ans