class Solution:
    def carPooling(self, A: List[List[int]], c: int) -> bool:
        n = max([x for _, _, x in A])
        cnt = [0]*(n+1)
        for x, i, j in A:
            cnt[i] += x
            cnt[j] -= x
        for i in range(1, n+1):
            cnt[i] += cnt[i-1]
        return max(cnt)<=c