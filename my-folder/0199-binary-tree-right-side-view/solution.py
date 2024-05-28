# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        # do level order traversal
        queue = deque()
        queue.append(root)
        lot = []
        while queue:
            temp_ans = []
            k = len(queue)
            for i in range(k):
                curr = queue.popleft()
                temp_ans.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            lot.append(temp_ans)
        
        ans = []
        for i in range(len(lot)):
            ans.append(lot[i][-1])

        return ans
