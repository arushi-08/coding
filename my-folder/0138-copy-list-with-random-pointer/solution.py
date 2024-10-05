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
        
        # create a copy of the entire list
        # create new head
        # go to every next create new head
        # store og node : new node in a map

        hmap = {}
        curr = head
        while curr:
            hmap[curr] = Node(curr.val)
            curr = curr.next
        
        hmap[None] = None
        curr = head
        while curr:
            hmap[curr].next = hmap[curr.next]
            hmap[curr].random = hmap[curr.random]
            curr = curr.next
        
        return hmap[head]
        

        
