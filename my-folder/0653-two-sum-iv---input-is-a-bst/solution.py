# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        inorder = self.helper(root)
        i = 0
        j = len(inorder)-1
        while i < j:
            currsum = inorder[i] + inorder[j]
            if currsum == k:
                return True
            elif currsum > k:
                j -= 1
            else:
                i += 1
        return False
    
    def helper(self, root):
        if not root:
            return []
        
        return self.helper(root.left) + [root.val] + self.helper(root.right)
