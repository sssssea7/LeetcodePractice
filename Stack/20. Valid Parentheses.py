class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c not in ")]}": stk.append(c)
            elif stk:
                if c == ")" and stk[-1] == "(": stk.pop()
                elif c == "]" and stk[-1] == "[": stk.pop()
                elif c == "}" and stk[-1] == "{": stk.pop()
                else: return False
            else: return False
        return True if not stk else False