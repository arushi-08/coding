from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        queue = deque()
        queue.append((root, 0))
        res = []
        while queue:
            l = len(queue)
            temp = []
            for _ in range(l):
                node, level = queue.popleft()
                if node:
                    temp.append(node.val)
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))
            if temp:
                res.append(temp)
        for i in range(len(res)):
            if i%2==1:
                res[i].reverse()

        return res

