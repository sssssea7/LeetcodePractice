class Solution:
    def twoCitySchedCost(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x:(x[0]-x[1]))
        return sum([a if i+1<=len(A)//2 else b for i, (a, b) in enumerate(A)])