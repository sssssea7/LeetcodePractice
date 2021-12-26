class Solution:
    def calculate(self, s: str) -> int:
        op, val = '+', 0
        stk = []
        for i, x in enumerate(s):
            if x.isdigit(): val = 10*val+int(x)
            if x in "+-*/" or i == len(s)-1:
                if op == '+': stk.append(val)
                if op == '-': stk.append(-val)
                if op == '*': stk.append(stk.pop()*val)
                if op == '/': stk.append(int(stk.pop()/val))
                op, val = x, 0
        return sum(stk)