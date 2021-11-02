class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in ht and ht[n] != i:
                return [i, nums.index(n)]
            ht[nums[i]] = i


class Solution:
    def twoSum(self, A: List[int], t: int) -> List[int]:
        M = {}
        for i in range(len(A)):
            x = t-A[i]
            if x in M: return [i, M[x]]
            M[A[i]] = i
            