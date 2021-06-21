class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def F(s, cnt):
            for i in range(len(s)):
                if cnt>0: F(s[:i+1]+"()"+s[i+1:], cnt-1)
            if cnt==0 and s not in ans: ans.append(s)
        F("()", n-1)
        return ans