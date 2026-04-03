# https://leetcode.com/problems/longest-alternating-subarray/description/

"""
https://leetcode.com/problems/longest-alternating-subarray/solutions/3737191/javacpython-two-pointers-and-dp-solution-4y71/
s1 - s0 = 1
s2 - s1 = -1,
s3 - s2 = 1
we can have
si - s0 = i % 2

So for each A[i],
find the longest alternating subarray where A[j] == A[i] + (j - i) % 2
"""

class Solution:
    def alternatingSubarray(self, A: List[int]) -> int:
        ans = 1
        cur = 1
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[j] == A[i] + (j-i)%2:
                    cur += 1
                else:
                    ans = max(ans, cur)
                    cur = 1
                    break
        ans = max(ans, cur)
        return ans if ans > 1 else -1
