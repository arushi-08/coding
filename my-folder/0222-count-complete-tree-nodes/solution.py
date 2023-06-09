# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftheight(self, root):
        d=0
        while root:
            root = root.left
            d += 1
        return d

    def rightheight(self, root):
        d=0
        while root:
            root = root.right
            d += 1
        return d
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        lh = self.leftheight(root)
        rh = self.rightheight(root)

        if lh == rh:
            print('nodes:', (2**lh) - 1)
            return (2**lh) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
