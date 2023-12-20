from sortedcontainers import SortedList

A = SortedList(key=lambda x: (x[0], -x[1]))
A.add((5,6))
A.add((1,2))
A.add((2,2))
A.add((1,1))
print(A)