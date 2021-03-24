class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:    
        SA = sorted(A)
        SB = sorted(B)
        ans = {b: [] for b in B}
        left = []
        i = 0
        for a in SA:
            if a > SB[i]: 
                ans[SB[i]].append(a)
                i += 1
            else: left.append(a)
        return [ans[b].pop() if ans[b] else left.pop() for b in B]