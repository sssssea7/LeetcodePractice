# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = list(accumulate(nums, initial=0))
        if prefix[-1] < target:
            return 0
            
        def is_greater(length):
            for i in range(length, len(prefix)):
                if prefix[i]-prefix[i-length]>=target:
                    return True
            return False

        left, right = 0, len(nums)
        while left<right:
            mid = (left+right)//2
            if is_greater(mid):
                right = mid
            else:
                left = mid + 1
        return left