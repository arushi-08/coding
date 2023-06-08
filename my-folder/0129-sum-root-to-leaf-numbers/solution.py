# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        sumval = 0

        def preorder(root, curr):
            nonlocal sumval
            if not root: return
            curr = curr*10 + root.val
            if not root.left and not root.right:
                sumval += curr
                return
            preorder(root.left, curr)
            preorder(root.right, curr)
        preorder(root, 0)
        return sumval


