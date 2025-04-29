# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # path in BT
        # max path sum 
        """
        at each node, know max path through that node
        pass to the parent, max path through that node
        also track max path either on left or right side
        """
        if not root: return 0
        maxpath = root.val

        def dfs(node):
            nonlocal maxpath

            if not node:
                return 0
            
            leftmaxpath = max(dfs(node.left), 0 )
            rightmaxpath = max(dfs(node.right), 0 )

            maxpath = max(
                maxpath, 
                leftmaxpath + node.val + rightmaxpath,
            )

            return max(leftmaxpath, rightmaxpath) + node.val
        
        dfs(root)

        return maxpath
