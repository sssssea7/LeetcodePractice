# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        tails = []
        left = []
        
        for x in nums:
            i = bisect_left(tails, x)
            left.append(i+1)
            if i==len(tails):
                tails.append(x)
            else:
                tails[i] = x
        
        tails = []
        right = []
        for x in reversed(nums):
            i = bisect_left(tails, x)
            right.append(i+1)
            if i==len(tails):
                tails.append(x)
            else:
                tails[i] = x
        
        ans = inf
        n = len(nums)
        for l, r in zip(left, right[::-1]):
            if l>1 and r>1:
                ans = min(ans, n-(l+r-1))
        return ans