class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(1, len(heights)):
            h = heights[i]-heights[i-1]
            if h > 0:
                heappush(pq, -h)
                bricks -= h
                if bricks < 0:
                    if ladders == 0: return i-1
                    bricks += -heappop(pq)
                    ladders -= 1
        return i