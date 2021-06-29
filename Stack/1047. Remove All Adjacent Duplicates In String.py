class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = ""
        for c in s:
            if not ans: ans += c
            else:
                if c != ans[-1]: ans += c
                else: ans = ans[:-1]
        return ans