class RandomizedSet:

    def __init__(self):
        self.S = set()

    def insert(self, val: int) -> bool:
        if val not in self.S:
            self.S.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.S:
            self.S.discard(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.sample(self.S, 1)[0]


# how to do it with O(1)