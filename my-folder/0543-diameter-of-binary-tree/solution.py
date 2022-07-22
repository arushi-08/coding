# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #            1
        #          2   3
        #        4   5
        #      6       7
        #    8           9op
        if not root: return 0
        if not root.left and not root.right: return 0
        
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        # print(root.val, right)
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        # print(root.val, left_height, right_height)
        
        return max(left, right, left_height+right_height)
    
    def height(self, root):
        if not root: return 0
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        return max(left, right) + 1
    
