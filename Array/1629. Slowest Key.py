class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = keysPressed[0]
        maxTime = releaseTimes[0]
        T = [releaseTimes[0]] + [0]*(len(keysPressed)-1)
        for i in range(1, len(releaseTimes)):
            curTime = releaseTimes[i]-releaseTimes[i-1]
            if curTime == maxTime:
                ans = max(ans, keysPressed[i])
            if curTime > maxTime:
                maxTime = curTime
                ans = keysPressed[i]
        return ans