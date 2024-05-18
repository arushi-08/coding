# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        self.helper(root)
        return self.moves
    
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        self.moves += abs(left) + abs(right) # no of moves at each root subtree
        return root.val + left + right - 1 # no of coins sent to parent after balancing root tree

