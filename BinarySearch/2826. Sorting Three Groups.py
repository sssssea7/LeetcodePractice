# https://leetcode.com/problems/sorting-three-groups/description/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            i = bisect_right(tails, x)
            if i==len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(nums)-len(tails)