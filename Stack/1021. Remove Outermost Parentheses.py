class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        cnt = 0
        ans = ''
        for s in S:
            if s == "(": 
                if cnt > 0: ans += "("
                cnt += 1
            else: 
                cnt -=1
                if cnt > 0: ans += ")"
        return ans