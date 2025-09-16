# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(head):
            pre = None
            while head:
                nxt = head.next
                head.next = pre
                pre = head
                head = nxt
            return pre

        l = reverse_list(head)

        carry = 0
        ans = cur = ListNode(-1)
        while l:
            sm = 2*l.val+carry
            l = l.next
            carry = sm//10
            cur.next = ListNode(sm%10)
            cur = cur.next
        
        if carry:
            cur.next = ListNode(carry)

        return reverse_list(ans.next)