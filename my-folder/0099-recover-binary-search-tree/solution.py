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
        # 2 nodes are not in BST order
        if not root or (not root.left and not root.right): return
        
        inorder_path = self.inorder(root)
        # print([i.val for i in inorder_path])
        
        swap1_node = inorder_path[0]
        for i in range(1, len(inorder_path)):
            if inorder_path[i].val < inorder_path[i-1].val:
                swap1_node = inorder_path[i-1]
                # print("swap1_node", swap1_node.val)
                break
        swap2_node = inorder_path[-1]
        for i in range(len(inorder_path)-2, -1, -1):
            if inorder_path[i].val > inorder_path[i+1].val:
                swap2_node = inorder_path[i+1]
                # print("swap2_node", swap2_node.val)
                break
        swap1_node.val, swap2_node.val = swap2_node.val, swap1_node.val
            
    
    def inorder(self, root):
        if not root: return []
        
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        
        return left + [root] + right
