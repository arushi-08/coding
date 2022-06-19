# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root: return 0
        
        return self.helper(root, root.val)
    
    def helper(self, root, max_val):
        
        if not root: return 0
        
        if max_val <= root.val:
            state = root.val
            return_val = 1
        else:
            state = max_val
            return_val = 0
            
        left = self.helper(root.left, state)
        right = self.helper(root.right, state)
        
        # print(return_val, root.val)
        return return_val + left + right
