# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        ans, _ = self.helper(root)
        return ans
    
    def helper(self, root):
        
        if not root: return True, 0
        
        left, left_ht = self.helper(root.left)
        right, right_ht = self.helper(root.right)
        
        return (left and right and abs(left_ht - right_ht) <= 1,
               max(left_ht, right_ht) + 1)
