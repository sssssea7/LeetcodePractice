# https://leetcode.com/problems/trapping-rain-water/

# two pointers
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

# monotonic stack
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        dec_stack = []
        for i in range(n):
            while dec_stack and height[i] >= height[dec_stack[-1]]:
                bottom_h = height[dec_stack.pop()]
                if not dec_stack:
                    break
                left = dec_stack[-1]
                h = min(height[left], height[i]) - bottom_h
                ans += h * (i-left-1)
            dec_stack.append(i)
        return ans