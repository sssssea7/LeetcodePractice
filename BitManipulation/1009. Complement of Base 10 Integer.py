class Solution:
    def findComplement(self, n: int) -> int:
        b = format(n, "b")
        ans = ""
        for i in range(len(b)):
            ans += "1" if b[i]=="0" else "0"
        return int(ans, 2)


class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask < n: mask = mask << 1 | 1
        return n ^ mask