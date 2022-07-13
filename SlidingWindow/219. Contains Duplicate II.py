class Solution:
    def containsNearbyDuplicate(self, A: List[int], k: int) -> bool:
        n, i, seen = inf, 0, set()
        for j in range(len(A)):
            while A[j] in seen:
                if i!=j: n = min(n, j-i)
                seen.remove(A[i])
                i += 1
            seen.add(A[j])
        return n<=k