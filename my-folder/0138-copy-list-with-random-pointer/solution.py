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
        
        if not head: return 
        
        old_to_new = {}

        curr = head

        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        copy_curr = old_to_new[head]
        curr = head
        while copy_curr:
            copy_curr.next = old_to_new.get(curr.next)
            copy_curr.random = old_to_new.get(curr.random)
            copy_curr = copy_curr.next
            curr = curr.next
        
        return old_to_new[head]


