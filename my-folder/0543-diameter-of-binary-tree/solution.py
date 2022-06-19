# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        lt_ht = self.height(root.left)
        # print("lt_ht", lt_ht, root.val)
        rt_ht = self.height(root.right)
        # print("rt_ht", rt_ht, root.val)
        return max(left, right, lt_ht + rt_ht)
    
    def height(self, root):
        
        if not root: return 0
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        return max(left, right) + 1
