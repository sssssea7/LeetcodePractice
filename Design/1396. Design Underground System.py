class UndergroundSystem:
    def __init__(self):
        self.in_ = {}
        self.out = defaultdict(lambda: defaultdict(lambda: [0, 0]))

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.in_[id] = (startStation, t)

    def checkOut(self, id: int, endStation: str, t1: int) -> None:
        ss, t = self.in_[id]
        self.out[ss][endStation][0] += t1 - t
        self.out[ss][endStation][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t, n = self.out[startStation][endStation]
        return t/n


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)