# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.recorded_depth = 0

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        # same depth & different parents

        parentx, xdepth = self.parent_n_depth(root, x, 0)
        parenty, ydepth = self.parent_n_depth(root, y, 0)

        print(xdepth, ydepth , parentx, parenty)
        if xdepth != ydepth or parentx == parenty:
            return False
        return True

    
    def parent_n_depth(self, root, val, depth):
        if not root:
            return None, 0

        if (root.left and root.left.val == val) or (root.right and root.right.val == val):
            if not self.recorded_depth:
                self.recorded_depth = depth
            return root, depth + 1
        
        if self.recorded_depth and depth >= self.recorded_depth:
            return None, 0

        parent, left = self.parent_n_depth(root.left, val, depth + 1)
        
        if left:
            return parent, left

        parent, right = self.parent_n_depth(root.right, val, depth + 1)
        
        return parent, right

        
        
