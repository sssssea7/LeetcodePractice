class Solution:
    def countPoints(self, S: str) -> int:
        D = defaultdict(set)
        for i in range(0, len(S)-1, 2):
            D[S[i+1]].add(S[i])
        ans = 0
        for k, v in D.items():
            if len(v)==3: ans += 1
        return ans
        