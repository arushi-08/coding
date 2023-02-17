# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        queue = deque()
        queue.append(root)
        count = 0
        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            for node in [curr.left, curr.right]:
                if node:
                    queue.append(node)
        
        return root
            
