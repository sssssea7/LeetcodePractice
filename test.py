class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solution(h, q):
        A = [i for i in range(2**h-1, 0, -1)]
        def dfs(arr, parent, val):
            if not arr: return
            r = arr.pop(len(arr)//2)
            l = arr.pop(0)
            print(l, r, arr, val, parent)
            if l==val: return parent
            elif r==val: return parent
            left = arr[:len(arr)//2]
            right = arr[len(arr)//2:]
            l = dfs(left, l, val)
            r = dfs(right, r, val)
            return l or r

        # ans = dfs(A[1:], A[0], 5)
        # for x in q:
        # print("ans: ", ans)
        
        p = []
        for i in q:
            if i==A[0]: p.append(-1)
            else: p.append(dfs(A[1:], A[0], i))
        print(p)
        return p

        # root = TreeNode(arr[0])
        # def constructTree(node, parent, d):
        #     if arr:
        #         if d<h:
        #             node.right = TreeNode(arr.pop(0))
        #             constructTree(node.right, node, d+1)
        #         else:
        #             node.left = TreeNode(arr.pop(0))
        #             constructTree(node.left, node, d+1)

        # constructTree(root, TreeNode(-1), 1)            
        
        # def dfs(node, parent, val):
        #     if not node: return
        #     if node.val==val: return parent.val
        #     dfs(node.left, node, val)
        #     dfs(node.right, node, val)
        # p = []
        # for i in q:
        #     p.append(dfs(root, TreeNode(-1), i))
        # print(p)
        # return p


Solution.solution(5, [19, 14, 28])