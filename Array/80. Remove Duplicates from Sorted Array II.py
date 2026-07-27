# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

# the idea is to use a stack-like approach to keep track of the number of duplicates. We can maintain a variable `stack_size` to keep track of the size of the stack, and we can iterate through the array starting from the third element. If the current element is not equal to the element at `stack_size - 2`, we can add it to the stack and increment `stack_size`. Finally, we return the minimum of `stack_size` and the length of the original array.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack_size = 2 # keep the first two elements
        for i in range(2, len(nums)):
            if nums[i] != nums[stack_size-2]:
                nums[stack_size] = nums[i]
                stack_size += 1
        return min(stack_size, len(nums))