# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.helper(-float('inf'), root, float('inf'))
    
    def helper(self, left_val, root, right_val):
        if not root:
            return True
        
        left = self.helper(left_val, root.left, min(root.val, right_val))
        right = self.helper(max(root.val, left_val), root.right, right_val)

        if not left or not right:
            return False
        
        if left_val < root.val and root.val < right_val:
            return True
        
        return False
