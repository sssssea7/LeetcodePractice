# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = dummy = ListNode(-1)
        ans.next = head
        while dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:                
                dummy = dummy.next
        return ans.next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = node = ListNode(next=head)
        while node.next:
            if node.next.val==val: node.next = node.next.next
            else: node = node.next
        return ans.next