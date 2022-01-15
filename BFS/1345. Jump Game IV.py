class Solution:
    def minJumps(self, A: List[int]) -> int:
        
        T = defaultdict(list)
        for i in range(len(A)): T[A[i]].append(i)
        seen = set()
        
        ans = 0
        seen = set()
        Q = [0]
        while Q:
            newq = []
            for n in Q:
                if n + 1 == len(A): return ans
                nxt = [n-1, n+1]
                if A[n] in T:
                    nxt += T.pop(A[n])
                for j in nxt:
                    if j not in seen and 0 <= j < len(A):
                        newq.append(j)
                        seen.add(j)
            Q = newq
            ans += 1