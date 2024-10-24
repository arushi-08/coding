# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        if (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
            return False
    
        ans1 = False
        ans2 = False
        
        ans1 = self.flipEquiv(root1.left, root2.right)
        ans2 = self.flipEquiv(root1.right, root2.left)

        if ans1 and ans2:
            return True
        
        if not ans1:
            ans1 = self.flipEquiv(root1.left, root2.left)
        
        if not ans2:
            ans2 = self.flipEquiv(root1.right, root2.right)

        return ans1 and ans2

