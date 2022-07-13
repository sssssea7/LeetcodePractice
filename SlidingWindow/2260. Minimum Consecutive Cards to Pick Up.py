class Solution:
    def minimumCardPickup(self, A: List[int]) -> int:
        if len(A)==len(set(A)): return -1
        i, ans, seen = 0, inf, set()
        cur = inf
        for j in range(len(A)):
            while A[j] in seen:
                cur = j-i+1
                seen.remove(A[i])
                i += 1
            seen.add(A[j])
            ans = min(ans, cur)
        return ans


class Solution:
    def minimumCardPickup(self, A: List[int]) -> int:
        if len(A)==len(set(A)): return -1
        ans, i, seen = inf, 0, set()
        for j in range(len(A)):
            while A[j] in seen:
                ans = min(ans, j-i+1)
                seen.remove(A[i])
                i += 1
            seen.add(A[j])
        return ans