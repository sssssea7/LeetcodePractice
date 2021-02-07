class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        index = len(nums)//2
        if (len(nums))%2 != 0: return nums[index]
        return (nums[index]+nums[index-1])/2.0