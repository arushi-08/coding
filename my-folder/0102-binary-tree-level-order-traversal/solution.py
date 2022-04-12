# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root:
            return []
        
        q, result = deque(), []
        
        q.append(root)
        while len(q):
            temp_result = []
            for _ in range(len(q)):
                x = q.popleft()
                temp_result.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            
            result.append(temp_result)
        
        return result
        
