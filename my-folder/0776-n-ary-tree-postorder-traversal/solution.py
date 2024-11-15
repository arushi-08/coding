"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        postorder_traversal = []
        self.helper(root, postorder_traversal)
        return postorder_traversal
    
    def helper(self, root, postorder_traversal):

        if not root:
            return
        
        for child in root.children:
            self.helper(child, postorder_traversal)
        
        postorder_traversal.append(root.val)
