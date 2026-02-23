# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s: return 0
        sign = -1 if s[0]=="-" else 1
        if s[0]=="-" or s[0]=="+":
            s = s[1:]
        s = s.lstrip("0")
        ans = ""
        for c in s:
            if c.isdigit():
                ans += c
            else:
                break
        if not ans: ans = 0
        if int(ans) > 2**31 - 1:
            if sign == 1:
                ans = 2**31 - 1
            else:
                ans = 2**31
        return sign * int(ans)
