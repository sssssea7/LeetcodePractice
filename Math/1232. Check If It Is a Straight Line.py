class Solution:
    def checkStraightLine(self, A: List[List[int]]) -> bool:
        x1, y1, x2, y2, = A[0][0], A[0][1], A[1][0], A[1][1]
        if all(a[1]==A[0][1] for a in A): return True
        else:
            for x, y in A[2:]:
                if (y2-y1)*(y-y1)==0: return False
                elif (x2-x1)/(y2-y1) == (x-x1)/(y-y1):
                    continue
                else: return False
        return True


class Solution:
    def checkStraightLine(self, A: List[List[int]]) -> bool:
        x1, y1, x2, y2, = A[0][0], A[0][1], A[1][0], A[1][1]
        for x, y in A[2:]:
            if (x2-x1)*(y-y1) != (x-x1)*(y2-y1):
                return False
        return True