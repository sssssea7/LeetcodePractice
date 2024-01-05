class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def F(s, cnt):
            for i in range(len(s)):
                if cnt>0: F(s[:i+1]+"()"+s[i+1:], cnt-1)
            if cnt==0 and s not in ans: ans.append(s)
        F("()", n-1)
        return ans

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