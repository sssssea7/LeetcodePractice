# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = [], []
        while l1:
            n1.append(l1.val)
            l1=l1.next
        while l2:
            n2.append(l2.val)
            l2=l2.next
        s1 = [str(n) for n in n1[::-1]]
        s2 = [str(n) for n in n2[::-1]]
        n1 = int(''.join(s1))
        n2 = int(''.join(s2))
        n = str(n1 + n2)[::-1]
        ans = res = ListNode(n[0])
        for num in n[1:]:
            ans.next = ListNode(num)
            ans = ans.next
        return res


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = curr = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            s += carry
            carry = s//10
            curr.next = ListNode(s%10)
            curr = curr.next
            
        return ans.next