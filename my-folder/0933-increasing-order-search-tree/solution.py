# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        inorder_list = []
        self.inorder_traversal(root, inorder_list)
        self.change_order(inorder_list)
        return inorder_list[0]
    
    def inorder_traversal(self, root, inorder_list):
        if not root:
            return
        
        self.inorder_traversal(root.left, inorder_list)
        inorder_list.append(root)
        self.inorder_traversal(root.right, inorder_list)
    
    def change_order(self, inorder_list):
        
        for i in range(len(inorder_list)-1):
            inorder_list[i].left = None
            inorder_list[i].right = inorder_list[i+1]
        
        inorder_list[-1].left = None
        
        
        
