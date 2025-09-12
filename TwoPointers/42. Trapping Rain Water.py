# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, A: List[int]) -> int:
        i, j = 0, len(A)-1
        pre, suf = 0, 0
        ans = 0
        while i<=j:
            pre = max(pre, A[i])
            suf = max(suf, A[j])
            if pre < suf:
                ans += pre - A[i]
                i += 1
            else:
                ans += suf - A[j]
                j -= 1
        return ans

class Solution:
    def trap(self, A: List[int]) -> int:
        pre = [A[0]]
        for i in range(1, len(A)):
            cur = max(pre[i-1], A[i])
            pre.append(cur)

        suf = [0] * len(A)
        suf[-1] = A[-1]
        for i in range(len(A)-2, -1, -1):
            cur = max(suf[i+1], A[i])
            suf[i] = cur
        
        ans = 0
        for p, s, h in zip(pre, suf, A):
            ans += min(p, s) - h

        return ans


