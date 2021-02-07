# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # if not lists: return ListNode(None)
        ll = []
        for l in lists:
            cur = l
            while cur:
                ll.append(cur.val)
                cur = cur.next
        sortedll = sorted(ll)
        ans = res = ListNode(-1)
        for num in sortedll:
            ans.next = ListNode(num)
            ans = ans.next
        return res.next