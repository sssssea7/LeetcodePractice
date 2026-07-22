# https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = 0
        for c in s:
            if c.isdigit():
                current_num = current_num * 10 + int(c)
            elif c=="[":
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif c.isalpha():
                current_str += c
            else: # if c=="]":
                prev_str, num = stack.pop()
                current_str = prev_str + num*current_str
        return current_str