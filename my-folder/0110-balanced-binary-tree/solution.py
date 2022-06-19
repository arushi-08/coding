# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True
    
        left = self.height(root.left)
        right = self.height(root.right)
        left_bal = self.isBalanced(root.left)
        right_bal = self.isBalanced(root.right)
        
        return abs(left - right) < 2 and left_bal and right_bal
    
    
    def height(self, root):
        if not root: return 0
        
        return max(self.height(root.left), self.height(root.right)) + 1
