def solution(A):
    A = [list(map(int, x.split('.'))) for x in A]
    return ['.'.join(map(str, x)) for x in sorted(A)]
ans = solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
print(ans)


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