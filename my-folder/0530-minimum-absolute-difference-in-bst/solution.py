# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        # do inorder, calculate mindiff between prev and currnodes
        self.prev = None
        self.mindiff = float('inf')
        def inorder(node):
            if not node: return 
            inorder(node.left)
            if self.prev:
                self.mindiff = min(self.mindiff, abs(node.val-self.prev.val))
            self.prev = node
            inorder(node.right)
        inorder(root)
        return self.mindiff

