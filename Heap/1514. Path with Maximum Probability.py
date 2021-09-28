class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        e = defaultdict(dict)
        for idx, (i, j) in enumerate(edges):
            e[i][j] = succProb[idx]
            e[j][i] = succProb[idx]
        seen = {}
        pq = [(-1, start)]
        while pq:
            prob1, i = heapq.heappop(pq)
            if i not in seen:
                seen[i] = prob1
                for j in e[i]:
                    prob2 = prob1*e[i][j]
                    if j not in seen:
                        heapq.heappush(pq, (prob2, j))
        
        if end in seen: return -seen[end]
        else: return 0
        