# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root or not root.val: return False
        
        if not root.left and not root.right: return True
        
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        
        if root.val == 2: return left or right
        
        if root.val == 3: return left and right
        
        return False