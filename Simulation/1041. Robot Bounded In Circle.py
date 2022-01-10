class Solution:
    def isRobotBounded(self, A: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1
        for i in A:
            if i == "G":
                x += dx
                y += dy
            elif i == "L": dx, dy = -dy, dx
            else: dx, dy = dy, -dx
        return (x == 0 and y == 0) or (dx, dy) != (0, 1)