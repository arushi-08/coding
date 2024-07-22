# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return

        inorder_val_to_idx = {}
        for i in range(len(inorder)):
            inorder_val_to_idx[inorder[i]] = i
        
        preorder_idx = 0
        def helper(st, ed):
            nonlocal preorder_idx
            if st > ed:
                return
            root_val = preorder[preorder_idx] # root is always at preorder_idx, because otherwise inorder would be empty i.e., st > ed, which is base case 
            preorder_idx += 1
            root = TreeNode(root_val)
            root.left = helper(st, inorder_val_to_idx[root_val]-1)
            root.right = helper(inorder_val_to_idx[root_val]+1, ed)
            return root
        
        return helper(0, len(inorder)-1)

         
