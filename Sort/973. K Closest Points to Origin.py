class Solution:
    def kClosest(self, P: List[List[int]], k: int) -> List[List[int]]:
        def square(x):
            return x[0]**2+x[1]**2
        P.sort(key=square)
        return P[:k]

class Solution:
    def kClosest(self, P: List[List[int]], k: int) -> List[List[int]]:
        P.sort(key=lambda x: x[0]**2+x[1]**2)
        return P[:k]