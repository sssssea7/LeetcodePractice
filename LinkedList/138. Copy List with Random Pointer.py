# https://leetcode.com/problems/copy-list-with-random-pointer/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {}
        ans = dummy = Node(-1)
        origin = head
        while origin:
            dummy.next = Node(origin.val)
            dummy = dummy.next
            mp[origin] = dummy
            origin = origin.next
           
        dummy = ans.next
        origin = head
        while origin:
            # dummy.next = Node(head.val)
            if origin.random:
                dummy.random = mp[origin.random]
            else:
                dummy.random = None
            origin = origin.next
            dummy = dummy.next
        return ans.next