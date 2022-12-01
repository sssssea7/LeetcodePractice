class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = s[:len(s)//2], s[len(s)//2:]
        return sum(a.count(c) for c in "aeiouAEIOU")==sum(b.count(c) for c in "aeiouAEIOU")


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        cnt1, cnt2 = 0, 0
        for i in range(len(s1)):
            if s1[i] in v:
                cnt1 += 1
            if s2[i] in v:
                cnt2 += 1
        return cnt1==cnt2
        