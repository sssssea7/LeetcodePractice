class Solution:
    def findComplement(self, n: int) -> int:
        b = format(n, "b")
        ans = ""
        for i in range(len(b)):
            ans += "1" if b[i]=="0" else "0"
        return int(ans, 2)
        

class Solution:
    def findComplement(self, n: int) -> int:
        k = 0
        while 2**k<=n: k += 1
        mask = 2**k-1
        return n^mask


class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        while mask < num: mask = (mask << 1) + 1
        return num ^ mask