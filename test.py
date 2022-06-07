# fuel-injection-perfection
def solution(n):
    n = int(n)
    ans = 0
    while n>1:
        if n&1:
            if n&2 and n!=3: n += 1
            else: n -= 1
        else: n >>= 1
        ans += 1 
    return ans

ans = solution(0)
print(ans)


# # prepare-the-bunnies-escape
# import heapq
# def solution(A):
#     m = len(A)
#     n = len(A[0])
#     D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
#     if A[0][0]==1: pq = [(0, 0, 0, 0)]
#     else: pq = [(1, 0, 0, 1)]

#     seen = {}
#     seen[(0, 0)] = (A[0][0]==0)
#     while pq:
#         cost, x, y, canRemove = heapq.heappop(pq)
#         if x==m-1 and y==n-1: return cost
#         for dx, dy in D:
#             if 0<=x+dx<m and 0<=y+dy<n and ((x+dx, y+dy) not in seen or canRemove>seen[(x+dx, y+dy)]) :
#                 if A[x+dx][y+dy]==1:
#                     if canRemove: 
#                         seen[(x+dx, y+dy)] = 0
#                         heapq.heappush(pq, (cost+1, x+dx, y+dy, 0))
#                 else: 
#                     seen[(x+dx, y+dy)] = canRemove
#                     heapq.heappush(pq, (cost+1, x+dx, y+dy, canRemove))
# ans = solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1]])
# print(ans)


# def solution(A):
#     A = [list(map(int, x.split('.'))) for x in A]
#     return ['.'.join(map(str, x)) for x in sorted(A)]
# ans = solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
# print(ans)


# class Solution:
#     def solution(h, q):        
#         A = [i for i in range(2**h-1, 0, -1)]
#         def dfs(arr, parent, val):
#             if not arr: return
#             r = arr.pop(len(arr)//2)
#             l = arr.pop(0)
#             if l==val: return parent
#             elif r==val: return parent
#             left = arr[:len(arr)//2]
#             right = arr[len(arr)//2:]
#             l = dfs(left, l, val)
#             r = dfs(right, r, val)
#             return l or r
#         p = []
#         for i in q:
#             if i==A[0]: p.append(-1)
#             else: p.append(dfs(A[1:], A[0], i))
#         return p
# Solution.solution(5, [19, 14, 28])