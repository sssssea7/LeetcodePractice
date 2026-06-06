# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in edges:
            union(x, y)

        return len(set(find(x) for x in parent))