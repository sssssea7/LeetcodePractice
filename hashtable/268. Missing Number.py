class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [0] * (len(nums)+1)
        for n in nums:
            arr[n] += 1
        for i in range(0, len(arr)):
            if arr[i]==0: return i


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = len(nums)*(len(nums)+1)//2
        return s2-s1