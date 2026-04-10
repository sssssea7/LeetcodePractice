# https://leetcode.com/problems/count-number-of-texts/description/

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9+7
        @cache
        def dfs(letter_count, i):
            if i<0: return 0
            if i==0: return 1
            if letter_count==3:
                return (dfs(3, i-1) + dfs(3, i-2) + dfs(3, i-3))%MOD
            if letter_count==4: 
                return (dfs(4, i-1) + dfs(4, i-2) + dfs(4, i-3) + dfs(4, i-4))%MOD
        
        ans = 1
        for c, n in groupby(pressedKeys):
            n = len(list(n))
            if c in "79":
                ans = ans * dfs(4, n)%MOD
            else:
                ans = ans * dfs(3, n)%MOD
        return ans
