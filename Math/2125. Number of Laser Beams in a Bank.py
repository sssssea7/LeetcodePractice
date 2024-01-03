# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
class Solution:
    def numberOfBeams(self, A: List[str]) -> int:
        prev = A[0].count("1")
        ans = 0
        for i, s in enumerate(A[1:]):
            cur = A[i+1].count("1")
            if cur != 0:
                ans += prev*cur
                prev = cur
        return ans
                