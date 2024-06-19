# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        _, ans= self.helper(root, target)
        return ans
    
    def helper(self, root, target):
        if not root:
            return float('inf'), root
        
        leftdist, lnode = self.helper(root.left, target)
        rightdist, rnode = self.helper(root.right, target)

        if leftdist != float('inf') and (leftdist <= rightdist and leftdist <= abs(target - root.val)):
            return leftdist, lnode
        
        if abs(target - root.val) <= rightdist:
            return abs(target - root.val), root.val

        return rightdist, rnode
