# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q, result = deque(), []
        
        if root:
            q.append(root)
        
        while len(q):
            temp = []
            for _ in range(len(q)):
                x = q.popleft()
                temp.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                
            result.append(temp)
        
        return result
