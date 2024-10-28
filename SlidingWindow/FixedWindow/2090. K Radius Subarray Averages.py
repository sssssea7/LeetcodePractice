# https://leetcode.com/problems/k-radius-subarray-averages/
class Solution:
    def getAverages(self, A: List[int], k: int) -> List[int]:
        sm = []
        t = 2 * k + 1
        if len(A)<t: return [-1]*len(A)
        cur_sm = sum(A[:t])
        sm = [cur_sm]
        for i in range(t, len(A)):
            cur_sm = cur_sm + A[i] - A[i-t]
            sm.append(cur_sm)
        # print(sm)
        sm = [s//t for s in sm]
        return [-1]*k + sm + [-1]*k