class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = op = cl = 0
        for c in s:
            if c=="(": op += 1
            else: cl += 1
            if cl==op: ans = max(ans, 2*cl)
            if cl>op: op = cl = 0
            
        op = cl = 0
        for c in s[::-1]:
            if c=="(": op += 1
            else: cl += 1
            if cl==op: ans = max(ans, 2*cl)
            if op>cl: cl = op = 0
                
        return ans