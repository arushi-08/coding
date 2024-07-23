"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        if self.helper(p, q):
            return p
        if self.helper(q, p):
            return q
        curr = p
        while curr.parent:
            if self.helper(curr.parent, q):
                return curr.parent
            curr = curr.parent
    
    def helper(self, p, q):
        if not p:
            return False
        if p == q:
            return True
        
        return self.helper(p.left, q) | self.helper(p.right, q)
