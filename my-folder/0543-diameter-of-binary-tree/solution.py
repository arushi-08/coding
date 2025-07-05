# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # root of binary tree, return length of diam

        # find left_ht, right_ht
        # 
        # 2, 1
        # and store the max height seen -> diameter

        diameter = 0

        def get_height(node):
            nonlocal diameter

            if not node:
                return 0
            
            left = get_height(node.left)
            right = get_height(node.right)

            diameter = max(left + right + 1, diameter)

            return max(left, right) + 1

        get_height(root)
        return diameter - 1

