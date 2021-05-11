class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        ans = 0
        for i in range(1, 100000):
            i = str(i)
            case1 = i + i[::-1]
            case2 = i + i[::-1][1:]
            sq1 = str(int(case1)**2)
            sq2 = str(int(case2)**2)
            if sq1 == sq1[::-1] and int(sq1) >= int(left) and int(sq1) <= int(right):
                ans += 1
            if sq2 == sq2[::-1] and int(sq2) >= int(left) and int(sq2) <= int(right):
                ans += 1
        return ans