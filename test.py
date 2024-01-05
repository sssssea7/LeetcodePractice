# from sortedcontainers import SortedList

# A = SortedList(key=lambda x: (x[0], -x[1]))
# A.add((5,6))
# A.add((1,2))
# A.add((2,2))
# A.add((1,1))
# print(A)


ans = []
n = 3
def dfs(op, cl, seq):
    if len(seq) == 2*n:
        ans.append(seq)
        return
    if op < n:
        dfs(op+1, cl, seq+"(")
    if op > cl:
        dfs(op, cl+1, seq+")")
dfs(0, 0, "")
print(ans)

