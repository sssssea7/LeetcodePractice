# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n # Rotating an array by its full length returns it to the original position.

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)