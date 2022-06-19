"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root: return 0
        
        values = []
        for child in root.children:
            values.append(self.maxDepth(child))
        
        if not values: return 1
        return max(values) + 1
