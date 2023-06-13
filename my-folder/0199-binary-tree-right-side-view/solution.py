# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do bfs and print the right value
        if not root: return []
        queue = deque()
        queue.append(root)
        ans = []
        while len(queue):
            l = len(queue)
            temp = []
            for _ in range(l):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                temp.append(curr.val)
            ans.append(temp[-1])
        return ans


