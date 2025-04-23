# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        # tilt is abs diff between sum of all left subtree and all right subtree node values
        totaltiltsum = 0

        def dfs(node):
            nonlocal totaltiltsum

            if not node:
                return 0
            
            leftsum = dfs(node.left)
            rightsum = dfs(node.right)

            totaltiltsum += abs(leftsum - rightsum)
            return leftsum + rightsum + node.val

        dfs(root)

        return totaltiltsum
