# https://leetcode.com/problems/string-compression-iii/
class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        for k, v in groupby(word):
            v = len(list(v))
            while v>9:
                ans += "9"
                v -= 9
                ans += k
            ans += str(v)
            ans += k
            
        return ans