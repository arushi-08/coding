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
        queue.append(root)
        level_order_list = []

        while queue:
            queue_length = len(queue)
            curr_level_list = []
            for _ in range(queue_length):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                curr_level_list.append(curr.val)

            level_order_list.append(curr_level_list)
        
        return level_order_list
