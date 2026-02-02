# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stk = []
        for i, c in enumerate(s):
            if c == "(":
                stk.append(i)
            elif c == ")":
                if stk:
                    stk.pop()
                else:
                    s[i] = ""
            # print(stk)
        while stk:
            s[stk.pop()] = ""
        return "".join(s)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        op = 0
        forward = []
        for c in s:
            if c == "(":
                op += 1
            elif c == ")":
                op -= 1
            forward.append(op)
            if op < 0:
                op = 0

        cl = 0
        backward = []
        for c in reversed(s):
            if c == ")":
                cl += 1
            elif c == "(":
                cl -= 1
            backward.append(cl)
            if cl < 0:
                cl = 0

        ans = ""
        for idx, (i, j) in enumerate(zip(forward, reversed(backward))):
            if i >= 0 and j >= 0:
                ans += s[idx]
        return ans