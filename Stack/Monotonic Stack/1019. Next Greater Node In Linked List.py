# https://leetcode.com/problems/next-greater-node-in-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []
        idx = 0
        while head:
            ans.append(0)
            while stack and head.val > stack[-1][1]:
                ans[stack.pop()[0]] = head.val
            stack.append((idx, head.val))
            head = head.next
            idx += 1
        return ans