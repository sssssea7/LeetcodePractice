class Solution:
    def canFinish(self, n: int, A: List[List[int]]) -> bool:
        D = defaultdict(list)
        inD = [0] * n
        for a, b in A:
            D[b].append(a)
            inD[a] += 1
        Q = [i for i in range(n) if inD[i]==0]
        ans = Q.copy()
        while Q:
            x = Q.pop()
            for j in D[x]:
                inD[j] -= 1
                if inD[j]==0:
                    Q.append(j)
                    ans.append(j)
        return len(ans)==n