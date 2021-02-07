class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return ""
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue
            if (char.isupper()) and (stack[-1].islower()) and (stack[-1].upper() == char):
                stack.pop()
            elif (char.islower()) and (stack[-1].isupper()) and (stack[-1].lower() == char):
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
                
            