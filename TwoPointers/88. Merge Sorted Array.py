# two pointers
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        i, j = m-1, n-1
        for k in reversed(range(len(A))):
            if j<0 or i>=0 and A[i]>=B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        idx = m+n-1
        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1

        if i>=0:
            nums1[:idx+1] = nums1[:i+1]
        if j>=0:
            nums1[:idx+1] = nums2[:j+1]


# sort
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        A[m:] = B
        A.sort()