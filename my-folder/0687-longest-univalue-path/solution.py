# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        # given root of bt
        # return length of longest path -> where each node in the path has the same value
        # bottom-up appraoch
        longestunival_path_len = 0

        def dfs(node, parent):
            """
            idea: in longestunival_path_len, store the max path possible through node
            return to parent, the path that doesn't go through both left and right, instead the max of left and right

            """
            nonlocal longestunival_path_len

            if not node:
                return 0
            
            left_unival_length = dfs(node.left, node.val)
            right_unival_length = dfs(node.right, node.val)

            maxlen = 0
            longestunival_path_len = max(
                    longestunival_path_len, 
                    left_unival_length + right_unival_length
                )

            if node.val == parent:
                return max(left_unival_length, right_unival_length) + 1
            
            return 0

        dfs(root, -1)

        return longestunival_path_len

