class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        if not self.cal: self.cal.append([start, end])
        for i in self.cal:
            if end > i[0] and start < i[1]:
                return False
        if flag: self.cal.append([start, end])
        return flag

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)