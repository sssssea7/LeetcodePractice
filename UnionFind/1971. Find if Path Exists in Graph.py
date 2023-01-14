class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find(x):
            if A[x]!=x: A[x] = find(A[x])
            return A[x]
        def union(x, y):
            A[find(x)] = find(y)

        A = list(range(n))

        for a, b in edges:
            union(a, b)
        return find(source)==find(destination)