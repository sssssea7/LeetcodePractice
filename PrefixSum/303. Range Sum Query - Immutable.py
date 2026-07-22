# https://leetcode.com/problems/range-sum-query-immutable/description/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixes = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixes[right+1]-self.prefixes[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)