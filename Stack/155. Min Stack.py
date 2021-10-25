# O(1)
class MinStack:

    def __init__(self):
        self.S = []

    def push(self, val: int) -> None:
        if not self.S:
            self.S.append([val, val])
        else:
            self.S.append([val, min(val, self.S[-1][1])])
            
    def pop(self) -> None:
        self.S.pop()

    def top(self) -> int:
        return self.S[-1][0]

    def getMin(self) -> int:
        return self.S[-1][1]


# O(n)
class MinStack:

    def __init__(self):
        self.S = []

    def push(self, val: int) -> None:
        self.S.append(val)

    def pop(self) -> None:
        self.S.pop()

    def top(self) -> int:
        return self.S[-1]

    def getMin(self) -> int:
        return min(self.S)