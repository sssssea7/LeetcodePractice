# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# solution explaination: https://www.bilibili.com/video/BV162PVzPECg/?share_source=copy_web&vd_source=e15d81161453174d0e9cd6d90343cb39

# 
# nums1: [ ... left1 | right1 ... ]
# nums2: [ ... left2 | right2 ... ]
# The partition is correct if left1 <= right2 and left2 <= right1, and the median is either max(left1, left2) or (max(left1, left2)+min(right1, right2))/2 depending on the total length of the two arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        total = n + m
        half = (total+1)//2

        l, r = 0, n
        while l<=r:
            i = (l+r)//2
            j = half - i

            left1 = -inf if i==0 else nums1[i-1]
            right1 = inf if i==n else nums1[i]
            left2 = -inf if j==0 else nums2[j-1]
            right2 = inf if j==m else nums2[j]

            if left1 <= right2 and left2 <= right1:
                largest_left = max(left1, left2)
                if total % 2 == 1:
                    return largest_left
                else:
                    smallest_right = min(right1, right2)
                    return (largest_left+smallest_right)/2
            elif left1 > right2: # too many left elements in nums1
                r = i - 1
            else:                # too many right elements in nums1
                l = i + 1