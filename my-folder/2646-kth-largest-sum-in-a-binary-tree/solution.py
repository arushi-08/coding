# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        queue = deque()
        queue.append(root)
        levels = []
        while queue:
            l = len(queue)
            temp = []
            for i in range(l):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                temp.append(curr.val)
            
            levels.append(sum(temp))
        
        levels.sort()
        if k > len(levels):
            return -1
        return levels[-k]
