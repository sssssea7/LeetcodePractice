class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        x, y = 1, 100
        while x <= 100 and 1 <= y: 
            if customfunction.f(x, y) < z: x += 1
            elif customfunction.f(x, y) > z: y -= 1
            else:
                ans.append([x, y])
                x += 1
                y -= 1
        return ans 


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1, 101):
            for y in range(1, 101):
                if customfunction.f(x, y)==z: ans.append([x, y])
        return ans