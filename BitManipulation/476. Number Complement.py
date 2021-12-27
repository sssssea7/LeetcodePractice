class Solution:
    def findComplement(self, n: int) -> int:
        b = format(n, "b")
        ans = ""
        for i in range(len(b)):
            ans += "1" if b[i]=="0" else "0"
        return int(ans, 2)
        