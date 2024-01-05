# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sub = s[:k]
        mx = cnt = sum([1 for c in sub if c in "aeiou"])
        for i in range(len(s)-k):
            if s[i] in "aeiou":
                cnt -= 1
            if s[i+k] in "aeiou":
                cnt += 1
            mx = max(mx, cnt)
        return mx