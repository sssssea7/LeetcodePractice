class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [0] * (len(nums)+1)
        for n in nums:
            arr[n] += 1
        du, mi = 0, 0
        for i in range(1, len(arr)):
            if arr[i]==0: mi = i
            if arr[i]==2: du = i
        return [du, mi]