class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        table = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        self.ans = []
        def dfs(curr_s, d):
            if not d:
                self.ans.append(curr_s)
                return
            for c in table[d[0]]:
                dfs(curr_s+c, d[1:])
        dfs("", digits)
        return self.ans

# similar dfs
# def dfs(i, cur):
#             if len(cur)==len(digits): 
#                 ans.append(cur)
#                 return
#             for c in table[digits[i]]:
#                 dfs(i+1, cur+c)
#         dfs(0, "")