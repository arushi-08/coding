# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        return self.helper(root, 1)
    
    def helper(self, root, count):
        if not root:
            return 0
        lcount, rcount = 0, 0
        if root.left:
            if root.val + 1 == root.left.val:
                lcount = self.helper(root.left, count + 1)
            else:
                lcount = self.helper(root.left, 1)
        if root.right:
            if root.val + 1 == root.right.val:
                rcount = self.helper(root.right, count + 1)
            else:
                rcount = self.helper(root.right, 1)
        
        return max(lcount, rcount, count)


