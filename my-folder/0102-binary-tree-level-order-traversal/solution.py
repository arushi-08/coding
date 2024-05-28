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
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            k = len(queue)
            temp_ans = []
            for _ in range(k):
                curr = queue.popleft()
                temp_ans.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            ans.append(temp_ans)
        
        return ans

