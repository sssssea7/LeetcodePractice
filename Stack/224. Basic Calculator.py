class Solution:
    def calculate(self, s: str) -> int:
        ans, val, stk, sign = 0, 0, [], 1
        for c in s:
            if c.isdigit():
                val = 10*val + int(c)
            elif c in "+-":
                ans += sign*val
                val = 0
                sign = 1 if c=="+" else -1
            elif c=="(":
                stk.append(ans)
                stk.append(sign)
                ans, sign = 0, 1
            elif c==")":
                ans += sign*val
                ans *= stk.pop()
                ans += stk.pop()
                val = 0
        return ans + sign*val