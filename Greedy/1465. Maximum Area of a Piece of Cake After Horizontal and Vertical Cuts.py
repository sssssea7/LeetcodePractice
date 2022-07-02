class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc = [0]+sorted(hc)+[h]
        vc = [0]+sorted(vc)+[w]
        diffh = [hc[i+1]-hc[i] for i in range(len(hc)-1)]
        diffv = [vc[i+1]-vc[i] for i in range(len(vc)-1)]
        return max(diffh)*max(diffv)%(10**9+7)