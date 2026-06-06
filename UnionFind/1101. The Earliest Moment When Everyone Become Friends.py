# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/description/

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        logs.sort()
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)
        
        ans = logs[0][0]
        for time, x, y in logs:
            if find(x)==find(y):
                continue
            ans = time
            union(x, y)

        return ans if len(set(find(a) for a in parent))==1 else -1
