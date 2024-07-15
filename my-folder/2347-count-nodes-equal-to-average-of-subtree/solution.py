# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        _,_,ans = self.helper(root)

        return ans
    
    def helper(self, root):
        if not root:
            return 0, 0, 0
        
        left, leftcount, leftans = self.helper(root.left)
        right, rightcount, rightans = self.helper(root.right)

        currsum = left + root.val + right
        currcount = leftcount + 1 + rightcount

        if root.val == currsum//currcount:
            currans = leftans + rightans + 1
        else:
            currans = leftans + rightans
        
        return currsum, currcount, currans



