class Solution:
    def topKFrequent(self, A: List[int], k: int) -> List[int]:
        cnt = Counter(A)
        cnt = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
        return [cnt[i][0] for i in range(k)]