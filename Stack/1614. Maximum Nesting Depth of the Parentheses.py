class Solution:
    # standard solution
    def maxDepth(self, s: str) -> int:
        stk = []
        ans = 0
        for c in s:
            if c=='(':
                stk.append('(')
            elif c==')':
                stk.pop()
            ans = max(ans, len(stk))
        return ans
        
    # smart solution
    def maxDepth(self, s: str) -> int:
        op = 0
        ans = 0
        for c in s:
            if c=='(':
                op += 1
            elif c==')':
                op -= 1
            ans = max(ans, op)
        return ans