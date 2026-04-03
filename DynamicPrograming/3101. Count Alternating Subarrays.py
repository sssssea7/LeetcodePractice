# https://leetcode.com/problems/count-alternating-subarrays/description/

class Solution:
    def countAlternatingSubarrays(self, A: List[int]) -> int:
        dp = [1] * len(A)
        for i in range(1, len(A)):
            if A[i-1] != A[i]:
                dp[i] = dp[i-1] + 1
        return sum(dp)

class Solution:
    def countAlternatingSubarrays(self, A: List[int]) -> int:
        ans = 1
        cur = 1
        for j in range(1, len(A)):
            if A[j]!=A[j-1]:
                cur += 1
            else:
                cur = 1
            ans += cur
        return ans

class Solution:
    def countAlternatingSubarrays(self, A: List[int]) -> int:
        ans = 0
        cur = 1
        for j in range(1, len(A)):
            if A[j]!=A[j-1]:
                cur += 1
            else:
                ans += cur*(cur+1)//2
                cur = 1
        ans += cur*(cur+1)//2
        return ans

