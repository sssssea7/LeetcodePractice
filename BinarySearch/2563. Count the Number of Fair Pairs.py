# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, A: List[int], lower: int, upper: int) -> int:
        A.sort()
        ans = 0
        for i, a in enumerate(A):
            p_l = bisect_left(A, lower-a, i+1, len(A))
            p_r = bisect_right(A, upper-a, i+1, len(A))
            ans += p_r - p_l
        return ans

        # A.sort()
        # ans = 0
        # for j, x in enumerate(A):
        #     # 注意要在 [0, j-1] 中二分，因为题目要求两个下标 i < j
        #     r = bisect_right(A, upper - x, 0, j)
        #     l = bisect_left(A, lower - x, 0, j)
        #     ans += r - l  
        # return ans
