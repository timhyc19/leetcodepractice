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
        d = {None: None}
        s = head
        while s:
            copy = Node(s.val)
            d[s] = copy
            s = s.next
        
        s = head
        while s:
            copy = d[s]
            copy.next = d[s.next]
            copy.random = d[s.random]
            s = s.next
        
        return d[head]
    