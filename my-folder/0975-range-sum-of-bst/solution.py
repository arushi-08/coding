# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        if not root:
            return 0
        
        lsum, rsum = 0, 0
        rsum = self.rangeSumBST(root.right, low, high)
        lsum = self.rangeSumBST(root.left, low, high)
        
        res = lsum + rsum
        if low <= root.val <= high:
            res += root.val
        
        return res
    


        

