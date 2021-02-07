class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ballNum = list(range(lowLimit, highLimit+1))
        boxNum = [sum(map(int, str(n))) for n in ballNum]   # for n in range(lowLimit, highLimit+1)
        count = Counter(boxNum)
        return max(count.values())