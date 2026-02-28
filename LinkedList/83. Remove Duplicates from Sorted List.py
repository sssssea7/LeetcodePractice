# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        while head.next:
            if head.val==head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next

        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        ans.next = head
        while head:
            if head.next and head.val==head.next.val:
                head.next = head.next.next
            else: head = head.next
        return ans.next