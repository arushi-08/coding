# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        return (
            self.helper(root.left, -float('inf'), root.val) 
         & self.helper(root.right, root.val, float('inf'))
        )
    
    def helper(self, root, left_limit, right_limit):
        if not root:
            return True
        
        ans = (self.helper(root.left, left_limit, root.val) 
         & self.helper(root.right, root.val, right_limit))
        
        
        if left_limit < root.val < right_limit:
            return ans & True
        return ans & False
            
            
