# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        return self.helper(root, "")
    
    def helper(self, root, type):
        if not root:
            return 0

        if not root.left and not root.right and type == "left":
            return root.val

        lnode =  self.helper(root.left, "left")
        rnode = self.helper(root.right, "right") 
        
        return lnode + rnode
        
