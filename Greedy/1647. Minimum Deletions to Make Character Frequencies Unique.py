class Solution:
    def minDeletions(self, s: str) -> int:
        A = sorted(list(Counter(s).values()))
        ans = 0
        seen = set()
        for a in A:
            while a in seen:
                a -= 1
                ans += 1
            if a: seen.add(a)
        return ans