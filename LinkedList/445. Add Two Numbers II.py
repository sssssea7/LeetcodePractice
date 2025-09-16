# https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(head):
            ans = ListNode(next=head)
            pre = None
            while head:
                nxt = head.next
                head.next = pre
                pre = head
                head = nxt
            return pre
        
        re_l1 = reverse_list(l1)
        re_l2 = reverse_list(l2)

        def addTwoNumbers(re_l1, re_l2):
            ans = curr = ListNode(-1)
            carry = 0
            while re_l1 or re_l2 or carry:
                s = 0
                if re_l1:
                    s += re_l1.val
                    re_l1 = re_l1.next
                if re_l2:
                    s += re_l2.val
                    re_l2 = re_l2.next
                s += carry
                carry = s//10
                curr.next = ListNode(s%10)
                curr = curr.next
            return ans.next

        l3 = addTwoNumbers(re_l1, re_l2)
        return reverse_list(l3)