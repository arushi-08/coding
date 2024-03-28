# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left=self.helper(root.left, root.val)
        right=self.helper(root.right, root.val)
        return left+right+1
    
    def helper(self, root, max_val):
        if not root:
            return 0
        left = self.helper(root.left, max(root.val, max_val))
        right = self.helper(root.right, max(root.val, max_val))

        if root.val >= max_val:
            return left+right+1
        return left+right
            
