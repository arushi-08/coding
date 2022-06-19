# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root : return True
        if not root.left and not root.right: return True
        
        max_left = self.findmax(root.left)
        min_right = self.findmin(root.right)
        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)
        
        return root.val < min_right and root.val > max_left and left and right
        
        
    def findmin(self, root):
        
        if not root: return float("inf")
        
        left = self.findmin(root.left)
        right = self.findmin(root.right)
        
        return min(root.val, left, right)
    
    def findmax(self, root):
        
        if not root: return float("-inf")
        
        left = self.findmax(root.left)
        right = self.findmax(root.right)
        
        return max(root.val, left, right)
