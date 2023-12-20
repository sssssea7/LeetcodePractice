from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.idx2n = {}
        self.n2i = defaultdict(SortedList)
        
    def change(self, index: int, number: int) -> None:
        # index --> number
        if index in self.idx2n:
            # remove old
            old_n = self.idx2n[index]
            self.n2i[old_n].remove(index)
            # update mp
        self.idx2n[index] = number
        self.n2i[number].add(index)
        

    def find(self, number: int) -> int:
        if self.n2i[number]:
            return self.n2i[number][0]
        else:
            return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)