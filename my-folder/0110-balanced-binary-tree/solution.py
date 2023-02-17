# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root: return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)
        if left and right and abs(leftheight - rightheight) <= 1:
            return True
        return False
    
    def height(self, root):
        if not root: return 0
        lh = self.height(root.left) + 1
        rh = self.height(root.right) + 1
        return max(lh, rh)


