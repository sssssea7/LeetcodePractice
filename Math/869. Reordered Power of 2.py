class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        nums = ["".join(x) for x in list(itertools.permutations(list(str(N))))]
        for n in nums:
            if int(n[0]) == 0:
                continue
            n = int(n)
            while n%2 == 0: n /= 2
            if n == 1: return True
        return False


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        P = [2**i for i in range(30)]
        for p in P:
            if Counter(str(p)) == Counter(str(N)): return True
        return False