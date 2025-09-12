# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(-1)
        cur = head
        dummy.next = head
        while cur and cur.next:
            prev.next, cur.next = cur.next, cur.next.next
            prev.next.next = cur
            prev, cur = cur, cur.next
        return dummy.next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(next=head)
        pre = ans
        cur = pre.next
        while cur and cur.next:
            nxt = cur.next
            n3 = nxt.next

            pre.next = nxt
            nxt.next = cur
            cur.next = n3

            pre = cur
            cur = n3
        return ans.next

