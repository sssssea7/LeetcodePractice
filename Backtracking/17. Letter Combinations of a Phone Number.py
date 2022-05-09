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


class Solution:
    def letterCombinations(self, A: str) -> List[str]:
        if not A: return []
        T = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        ans = []
        stk = []
        def fn(i):
            if i==len(A): return ans.append(''.join(stk.copy()))
            for x in T[A[i]]:
                stk.append(x)
                fn(i+1)
                stk.pop()
                
        fn(0)
        return ans


class Solution:
    def letterCombinations(self, A: str) -> List[str]:
        if not A: return []
        T = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        ans = []
        def fn(i, cur):
            if len(cur)==len(A): ans.append(cur)
            if i==len(A): return
            for c in T[A[i]]:
                fn(i+1, cur+c)
        fn(0, "")
        return ans