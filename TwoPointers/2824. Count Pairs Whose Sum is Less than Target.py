# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

class Solution:
    def countPairs(self, A: List[int], t: int) -> int:
        A.sort()
        i, j = 0, len(A)-1
        ans = 0
        while i<j:
            if A[i] + A[j] < t:
                # print(i, j)
                ans += j-i
                i += 1
            else:
                j -= 1
        return ans