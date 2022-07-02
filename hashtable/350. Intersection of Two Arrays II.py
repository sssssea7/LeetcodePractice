class Solution:
    def intersect(self, A: List[int], B: List[int]) -> List[int]:
        cnt = Counter(A)&Counter(B)
        ans = []
        for k, v in cnt.items():
            ans.extend([k]*v)
        return ans