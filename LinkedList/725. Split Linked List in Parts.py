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
        