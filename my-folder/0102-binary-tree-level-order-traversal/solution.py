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
        queue = deque()
        queue.append((root, 0))
        ans = [[root.val]]
        while queue:
            level = []
            curr, level_no = queue.popleft()
            for child in [curr.left, curr.right]:
                if child:
                    level.append(child.val)
                    queue.append((child, level_no+1))
            if level:
                if level_no+1 >= len(ans):
                    ans.append(level)
                else:
                    ans[level_no+1].extend(level)
        return ans
