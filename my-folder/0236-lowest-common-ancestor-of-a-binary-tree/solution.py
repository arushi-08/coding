# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # return lca, 
        # state root and parent path
        self.ans = None
        self.helper(root, p, q)
        return self.ans
    
    def helper(self, root, p, q):
        if not root:
            return False
        if root == p or root == q:
            self.ans = root
            return True
        
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)

        if left and right:
            self.ans = root
            return True        
        
        if left or right:
            return True
        
        return False
