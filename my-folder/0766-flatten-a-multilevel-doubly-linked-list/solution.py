"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def dfs(curr):
            if not curr:
                return
            
            if not curr.next and not curr.child:
                return curr
            
            if not curr.child:
                return dfs(curr.next)

            child_tail = dfs(curr.child)
            currnext = curr.next
            curr.next = curr.child
            curr.next.prev = curr
            curr.child = None
            child_tail.next = currnext
            if currnext:
                currnext.prev = child_tail
                return dfs(currnext)
            
            return child_tail
            

        dfs(head)
        
        return head

