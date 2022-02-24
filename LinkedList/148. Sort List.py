# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        ans = head = ListNode(-1)
        while arr:
            head.next = ListNode(arr.pop(0))
            head = head.next
        return ans.next