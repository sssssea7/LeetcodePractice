class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        G = defaultdict(dict)
        for i, j in connections:
            G[i][j] = 0
            G[j][i] = 1
        # print(G)
        
        seen = set()
        Q = [0]
        ans = 0
        
        while Q:
            i =  Q.pop(0)
            seen.add(i)
            for j in G[i]:
                if j not in seen:
                    Q.append(j)
                    ans += G[j][i]
        return ans