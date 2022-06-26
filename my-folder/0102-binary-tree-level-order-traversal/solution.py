# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        queue = deque()
        ans = []
        queue.append(root)
        while len(queue):
            temp = []
            l = len(queue)
            for _ in range(l):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(temp)
        
        return ans
        
        
#         if not root: return []
        
#         queue = deque()
#         queue.append((0,root))
#         ans = [[]]
#         while len(queue):
            
#             level, curr = queue.popleft()
#             try:
#                 ans[level].append(curr.val)
#             except:
#                 ans.append([curr.val])
            
#             if curr.left:
#                 queue.append((level + 1, curr.left))
#             if curr.right:
#                 queue.append((level + 1, curr.right))
#         return ans
