# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/

class Solution:
    def minElement(self, nums: List[int]) -> int:
        def get_sum(num):
            sm = 0
            while num>0:
                num, remainder = divmod(num, 10)
                sm += remainder
            return sm
            
        ans = inf
        for num in nums:
            ans = min(ans, get_sum(num))
        return ans