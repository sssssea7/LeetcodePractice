# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, A: List[int], t: int) -> List[int]:
        i, j = 0, len(A)-1
        while i<=j:
            if A[i] + A[j] == t:
                return [i+1, j+1]
            elif A[i] + A[j] > t:
                j -= 1
            else:
                i += 1
        