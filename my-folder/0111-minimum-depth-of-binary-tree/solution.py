# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        q = deque()
        level = 1
        q.append(root)
        while len(q):
            l = len(q)
            for _ in range(l):
                curr = q.popleft()
                if not curr.left and not curr.right:
                    return level
                if curr.left:
                    q.append(curr.left) 
                if curr.right:
                    q.append(curr.right)
            level += 1
        return level
