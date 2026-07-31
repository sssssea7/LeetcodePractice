# https://leetcode.com/problems/ipo/description/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        data = [(c, p) for c, p in zip(capital, profits)]
        data.sort(key = lambda x:x[0])
        pq = []
        i = 0
        n = len(profits)
        for _ in range(k):
            while i<n and data[i][0]<=w:
                heappush(pq, -data[i][1])
                i += 1
            if pq:
                w -= heappop(pq)
            else:
                break

        return w