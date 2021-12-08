# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        arr = "".join(map(str, arr))
        return int(arr, 2)


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = ""
        while head:
            n += str(head.val)
            head = head.next
        ans = int(''.join(n), 2)
        return ans


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans*2+head.val  # equivalent to: ans = ans<<1 | head.val
            head = head.next
        return ans