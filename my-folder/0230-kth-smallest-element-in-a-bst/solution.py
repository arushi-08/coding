# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.inorderlist.append(root.val)
        self.inorder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # get leftheight of BST, if leftheight < k, search left side
        # decrease height, decrease k
        self.inorderlist = []
        self.inorder(root)
        if k > len(self.inorderlist): return -1
        return self.inorderlist[k-1]


