# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        stack = []
        nums1_to_idx = {x: i for i, x in enumerate(nums1)}
        for i, x in enumerate(nums2):
            while stack and x >= nums2[stack[-1]]:
                j = stack.pop()
                if nums2[j] in nums1:
                    ans[nums1_to_idx[nums2[j]]] = x
            stack.append(i)
        return ans


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = [-1] * len(nums2)
        dec_stack = []
        for i, x in enumerate(nums2):
            while dec_stack and nums2[i]>nums2[dec_stack[-1]]:
                j = dec_stack.pop()
                next_greater[j] = nums2[i]
            dec_stack.append(i)
        ans = []
        for x in nums1:
            ans.append(next_greater[nums2.index(x)])
        return ans


class Solution:
    def nextGreaterElement(self, A: List[int], B: List[int]) -> List[int]:
        mp = defaultdict(lambda: -1)
        stk = []
        for i in range(len(B)):
            while stk and B[stk[-1]]<B[i]:
                mp[B[stk.pop()]] = B[i]
            stk.append(i)
        return [mp[x] for x in A]


