class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        def dfs(op, cl, seq):
            if len(seq) == 2*n:
                self.ans.append(seq)
                return
            if op < n:
                dfs(op+1, cl, seq+"(")
            if op > cl:
                dfs(op, cl+1, seq+")")
        dfs(0, 0, "")
        return self.ans