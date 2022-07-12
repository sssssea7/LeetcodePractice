class Solution:
    def lengthOfLongestSubstring(self, A: str) -> int:
        ans = 0
        i = 0
        seen = set()
        for j in range(len(A)):
            while A[j] in seen:
                seen.remove(A[i])
                i += 1
            seen.add(A[j])
            ans = max(ans, j-i+1)
        return ans