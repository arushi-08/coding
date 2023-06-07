# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.helper(0,0,len(preorder)-1, inorder, preorder)
    def helper(self, prestart_idx, instart_idx, inend_idx, inorder, preorder):
        
        if prestart_idx >= len(preorder) or instart_idx > inend_idx: return None
        rootval = preorder[prestart_idx]
        root = TreeNode(rootval)

        root_idx_in_inorder = 0
        for i in range(instart_idx, inend_idx+1):
            if rootval == inorder[i]:
                root_idx_in_inorder = i

        root.left = self.helper(
            prestart_idx+1,
            instart_idx,
            root_idx_in_inorder-1,
            inorder, 
            preorder)
        root.right = self.helper(
            prestart_idx+root_idx_in_inorder - instart_idx + 1,
            root_idx_in_inorder+1,
            inend_idx,
            inorder, 
            preorder
            )
    # 3,9,100, 30, 40, 20,15,7 - preorder
    # 30 100 40 9 3 15 20 7 - inorder
    # 0 + (root_idx_in_inorder - inorder_start + 1)
        return root
            
