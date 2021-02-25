class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X==Y: return 0
        if X>Y: return X-Y
        ans = 0
        while Y > X * 2:
            if Y % 2 == 0:
                ans += 1
                Y = Y/2
            else: 
                ans += 2
                Y = (Y+1)/2
        a = X * 2 - Y
        if a > 1:
            ans += a//2
            X -= a//2
        ans += (X * 2) % Y + 1
        return int(ans)