# https://leetcode.com/problems/seat-reservation-manager/ 
from sortedcontainers import SortedList
class SeatManager:

    def __init__(self, n: int):
        self.R = SortedList([0, i+1] for i in range(n+1))

    def reserve(self) -> int:
        [x, y] = self.R[0]
        self.R.remove([x,y])
        self.R.add([1,y])
        return y

    def unreserve(self, seatNumber: int) -> None:
        if [1, seatNumber] in self.R:
            self.R.remove([1, seatNumber])
            self.R.add([0, seatNumber])


class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in range(1, n+1)]

    def reserve(self) -> int:
        seatNumber = heapq.heappop(self.seats)
        return seatNumber

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)