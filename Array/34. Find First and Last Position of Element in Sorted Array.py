# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, A: List[int], t: int) -> List[int]:
        # if t not in A: return [-1, -1]
        def lower_bound(A, t):
            l, r = 0, len(A)-1
            while l<=r:
                m = (l+r)//2
                if A[m] < t:
                    l = m + 1
                else:
                    r = m - 1
            return l

        start = lower_bound(A, t)
        if start == len(A) or A[start] != t:
            return [-1, -1]
        end = lower_bound(A, t+1)
        return [start, end-1]

# groupby
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums: return [-1, -1]
        T = [[c, len(list(s))] for c, s in itertools.groupby(nums)]
        l = 0
        for i in range(len(T)):
            if T[i][0] == target: 
                target_i = i
                break
            l += T[i][1]
        r = l + T[target_i][1]
        return [l, r-1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums: return [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                l = r = i
                break
        
        while r<len(nums) and nums[r] == target:
            r += 1
        return [l, r-1]


# Binary Search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(l, h, t):
            while l<=h:
                m = (l+h)//2
                if nums[m]==t:
                    return m
                elif nums[m]>t:
                    h = m - 1
                else:
                    l = m + 1
            return l
            
        l, h = binSearch(0, len(nums)-1, target-0.5), binSearch(0, len(nums)-1, target+0.5)-1
        if l<=h: return [l, h]
        else: return [-1, -1]
