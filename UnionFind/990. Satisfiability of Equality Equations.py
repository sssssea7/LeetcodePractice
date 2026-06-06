# https://leetcode.com/problems/satisfiability-of-equality-equations/description/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        equal = []
        not_equal = []
        for s in equations:
            relation = s[1:3]
            if relation == "==":
                equal.append([s[0], s[-1]])
            else:
                not_equal.append([s[0], s[-1]])
                
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in equal:
            union(x, y)

        for x, y in not_equal:
            if find(x)==find(y):
                return False
        return True