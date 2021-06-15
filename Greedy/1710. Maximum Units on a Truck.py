class Solution:
    def maximumUnits(self, A: List[List[int]], k: int) -> int:
        A = sorted(A, key=lambda x:-x[1])
        ans = 0
        for box in A:
            ans += min(k, box[0])*box[1]
            k -= box[0]
            if k<0: break
        return ans


class Solution:
    def maximumUnits(self, box: List[List[int]], truckSize: int) -> int:
        box = sorted(box, key=lambda x:x[1], reverse=True)
        ans = 0
        for i in range(len(box)):
            if box[i][0] < truckSize:
                ans += box[i][0]*box[i][1]
                truckSize -= box[i][0]
            else:
                ans += truckSize*box[i][1]
                break
        return ans