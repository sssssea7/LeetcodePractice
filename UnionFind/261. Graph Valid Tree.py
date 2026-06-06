# https://leetcode.com/problems/graph-valid-tree/description/

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in edges:
            if find(x)==find(y):
                return False
            union(x, y)

        return True if len(set(find(x) for x in parent))==1 else False