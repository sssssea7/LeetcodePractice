class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        p = [3**i for i in range(30)]
        if n in p: return True
        return False


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0: return False
        while n%3 == 0: n /= 3
        if n == 1: return True
        return False