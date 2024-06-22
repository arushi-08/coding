# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        leaf1 = self.helper(root1)
        leaf2 = self.helper(root2)
        return leaf1 == leaf2
    
    def helper(self, root):
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        return self.helper(root.left) + self.helper(root.right)
