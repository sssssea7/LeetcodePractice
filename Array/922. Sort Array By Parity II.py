class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = list(filter(lambda x:x%2!=0, nums))
        even = list(filter(lambda x:x%2==0, nums))
        for i in range(0, len(nums), 2):
            nums[i] = even[(i-1)//2]
        for i in range(1, len(nums), 2):
            nums[i] = odd[i//2]
        return nums