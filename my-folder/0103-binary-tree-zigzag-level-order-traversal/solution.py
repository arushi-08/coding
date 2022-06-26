# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        queue = deque()
        queue.append(root)
        ans = []
        while len(queue):
            l = len(queue)
            temp = []
            for _ in range(l):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(temp)
        
        for idx, i in enumerate(ans):
            if idx % 2 == 1:
                i.reverse()
        return ans
