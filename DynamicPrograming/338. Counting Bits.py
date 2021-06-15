class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0: return [0]
        dp = [0, 1]
        for i in range(1, n+1):
            dp.extend([x+1 for x in dp])
            if len(dp)>n: return dp[:n+1]