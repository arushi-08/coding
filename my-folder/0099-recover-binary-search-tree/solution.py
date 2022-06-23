# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root: return
        inorder = []
        self.helper(root, inorder)
        wrong_idx_elements = []
        for i in range(len(inorder)-1):
            if inorder[i].val < inorder[i+1].val:
                continue
            else:
                if wrong_idx_elements:
                    wrong_idx_elements.append(i+1)
                else:
                    wrong_idx_elements.append(i)
        
        if len(wrong_idx_elements) == 1:
            self.swap(inorder, wrong_idx_elements[0], wrong_idx_elements[0]+1)
        else:
            self.swap(inorder, wrong_idx_elements[0], wrong_idx_elements[1])
    
    def swap(self, inorder, node1_idx, node2_idx):
        
        inorder[node1_idx].val, inorder[node2_idx].val = inorder[node2_idx].val, inorder[node1_idx].val
        
            
        
    def helper(self, root, inorder):
        
        if not root: return
        
        self.helper(root.left, inorder)
        inorder.append(root)
        self.helper(root.right, inorder)
