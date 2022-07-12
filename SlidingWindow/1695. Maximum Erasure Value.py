class Solution:
    def maximumUniqueSubarray(self, A: List[int]) -> int:
        ans, seen = 0, set()
        sm = 0
        i = 0
        for j in range(len(A)):
            while A[j] in seen:
                seen.remove(A[i])
                sm -= A[i]
                i += 1
            seen.add(A[j])
            sm += A[j]
            ans = max(ans, sm)
        return ans