# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        if l == r: return head
        bf = ans = ListNode(0)
        bf.next = head
        for _ in range(l-1):
            bf = bf.next
            head = head.next
        prev = None
        for _ in range(r-l+1):
            head.next, prev, head = prev, head, head.next
            # nxt = head.next
            # head.next = prev
            # prev = head
            # head = nxt
        bf.next.next = head
        bf.next = prev
        return ans.next