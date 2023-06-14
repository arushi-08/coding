# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxwidth = 0
        queue = deque()
        queue.append((root, 0))
        while len(queue):
            l = len(queue)
            _, level_head_idx = queue[0]
            for _ in range(l):
                curr, col_idx = queue.popleft()
                if curr.left:
                    queue.append((curr.left, 2*col_idx))
                if curr.right:
                    queue.append((curr.right, 2*col_idx+1))
            maxwidth = max(maxwidth, col_idx-level_head_idx + 1)
        
        return maxwidth



