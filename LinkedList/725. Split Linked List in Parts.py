# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        l = len(arr)
        ans = []
        if k > len(arr):
            while arr:
                cur = ListNode(arr.pop(0))
                ans.append(cur)
            n = ListNode()
            for i in range(k-l):
                ans.append(head)
        else:
            l1 = l%k
            l2 = k-l1
            k1 = l//k+1
            k2 = l//k
            for i in range(l1):
                res = cur = ListNode(arr.pop(0))
                for j in range(k1-1):
                    cur.next = ListNode(arr.pop(0))
                    cur = cur.next
                ans.append(res)
            for i in range(l2):
                res = cur = ListNode(arr.pop(0))
                for j in range(k2-1):
                    cur.next = ListNode(arr.pop(0))
                    cur = cur.next
                ans.append(res)
        return ans
        


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        N = 0
        while cur:
            N += 1
            cur = cur.next
        L, ext = divmod(N, k)
        cur = head
        ans = []
        for i in range(k):
            tmp = cur
            for j in range(L+(i<ext)-1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
                # cur, cur.next = cur.next, None   # why this not working
                # tmp2 = cur.next
                # cur.next = None
                # cur = tmp2
            ans.append(tmp)
        return ans