# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        
        if not root: return -1
        
        left = self.helper(root.left, res)
        right = self.helper(root.right, res)
        
        level = max(left, right) + 1
        
        if len(res) <= level:
            res.append([])
        
        res[level].append(root.val)
        
        return level
        
