class Solution:
    def countDigits(self, num: int) -> int:
        cnt = Counter(str(num))
        ans = 0
        for k, v in cnt.items():
            if num%int(k)==0: ans += v
        return ans