# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root: return TreeNode(val)
        
        if root.val > val:
            self.insertIntoBST(root.left, val)
        else:
            self.insertIntoBST(root.right, val)
        
        if root.val > val and not root.left:
            root.left = TreeNode(val)
        
        elif root.val < val and not root.right:
            root.right = TreeNode(val)
        
        return root
