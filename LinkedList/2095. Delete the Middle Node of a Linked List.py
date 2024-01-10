# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        node = ans = ListNode(-1)
        node.next = head
        m = n//2
        i = 0
        while node:
            if i==m:
                node.next = node.next.next
            else:
                node = node.next
            i += 1
        return ans.next