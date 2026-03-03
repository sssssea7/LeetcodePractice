# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []
        def dfs(op, cl):
            if len(path)==2*n:
                ans.append(''.join(path.copy()))
            if op<n:
                path.append("(")
                dfs(op+1, cl)
                path.pop()
            if op>cl:
                path.append(")")
                dfs(op, cl+1)
                path.pop()
        dfs(0, 0)
        return ans

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:     # too slow
        ans = []
        path = []
        def dfs(i, op, cl):
            if op>cl or op<0 or cl<0: return
            if len(path)==n*2:
                ans.append(''.join(path))
            for j in range(i, n*2):
                path.append("(")
                dfs(j+1, op-1, cl)
                path.pop()
                
                path.append(")")
                dfs(j+1, op, cl-1)
                path.pop()
        dfs(0, n, n)
        return ans

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