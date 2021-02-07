class Solution:
    def maximumUnits(self, A: List[List[int]], k: int) -> int:
        A = sorted(A, key=lambda x:-x[1])
        ans = 0
        for box in A:
            ans += min(k, box[0])*box[1]
            k -= box[0]
            if k<0: break
        return ans