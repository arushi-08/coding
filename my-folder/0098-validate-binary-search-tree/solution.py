# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root, minleft, maxright):
        if not root: return True
        
        if minleft < root.val < maxright:
            return self.helper(root.left, minleft, max(root.val, minleft)) & self.helper(root.right, min(root.val, maxright), maxright)
        return False

