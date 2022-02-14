class Solution:
    def maximumANDSum(self, A: List[int], numSlots: int) -> int:
        @cache
        def dp(mask, i):
            if i==len(A): return 0
            ans = 0
            for j in range(numSlots):
                if mask & (1<<j*2) == 0 or mask & (1<<j*2+1) == 0:
                    if mask & (1<<j*2) == 0: nxt = mask ^ (1<<j*2)
                    else: nxt = mask ^ (1<<j*2+1)
                    ans = max(ans, (A[i]&(j+1))+dp(nxt, i+1))
            return ans
        return dp(0, 0)