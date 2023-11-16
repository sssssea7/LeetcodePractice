class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0
        for letter in letters:
            l, r = s.index(letter), s.rindex(letter)
            cur = set()
            for k in range(l+1, r):
                cur.add(s[k])
            ans += len(cur)
        return ans