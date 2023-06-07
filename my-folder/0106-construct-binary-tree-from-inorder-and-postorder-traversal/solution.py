# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        return self.helper(
            len(inorder)-1, 0, len(inorder)-1, inorder, postorder
            )
    
    def helper(self, poststart, start, end, inorder, postorder):
        if poststart >= len(postorder) or start > end: return None

        root = TreeNode(postorder[poststart])
        root_idx_in_inorder = 0
        for i in range(start, end+1):
            if inorder[i] == root.val:
                root_idx_in_inorder = i
                break
        # print(postorder[poststart - (end -root_idx_in_inorder + 1)])
        root.left = self.helper(poststart - (end -root_idx_in_inorder + 1), start, root_idx_in_inorder-1, inorder, postorder)
        root.right = self.helper(poststart-1, root_idx_in_inorder+1, end, inorder, postorder)

        return root


