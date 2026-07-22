# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        n = len(s)
        i = 0
        while i<n and s[i]==" ":
            i += 1
        sign = 1
        if i<n and s[i] in "+-":
            if s[i]=="-":
                sign = -1
            i += 1
        number = 0
        limit = INT_MAX if sign == 1 else 2**31
        while i<n and s[i].isdigit():
            digit = int(s[i])
            number = number * 10 + digit
            if number > limit:
                return INT_MAX if sign == 1 else INT_MIN
            i += 1
        return sign * number

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        n = len(s)
        i = 0
        while i<n and s[i]==" ":
            i += 1
        sign = 1
        if i<n and s[i] in "+-":
            if s[i]=="-":
                sign = -1
            i += 1
        number = 0
        while i<n and s[i].isdigit():
            digit = int(s[i])
            number = number * 10 + digit
            i += 1
        if sign == 1 and number > INT_MAX:
            return INT_MAX
        if sign == -1 and -number < INT_MIN:
            return INT_MIN
        return sign * number

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
