class Solution:
    def findOrder(self, N: int, P: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        start = [0]*N
        for x in P:
            G[x[1]].append(x[0])
            start[x[0]] += 1
        Q = [i for i, d in enumerate(start) if d==0]
        ans = []
        while Q:
            i = Q.pop(0)
            ans.append(i)
            for j in G[i]:
                start[j] -= 1
                if not start[j]: Q.append(j)     
        return ans if len(ans)==N else []