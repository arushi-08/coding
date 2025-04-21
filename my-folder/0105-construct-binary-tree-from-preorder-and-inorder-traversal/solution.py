# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # construct binary tree from preorder and inorder
        # 3,9,20,15,7 pre | 9,3,15,20,7 inorder
        # 

        if not preorder:
            return
        
        self.pre_index=0

        inorder_to_pos = {v:i for i,v in enumerate(inorder)}

        def dfs(st, ed):
            """
            idea:
            preorder first element is always the current root
            the left of this root in inorder is left subtree space and same for right
            find the inorder_ed[currnode.val], and pass it to next recursion
            keep doing self.pre_index += 1, that's all
            """
            if st >= ed:
                return

            node = TreeNode(preorder[self.pre_index])
            self.pre_index += 1
            inorder_ed = inorder_to_pos[node.val]

            node.left = dfs(st, inorder_ed)
            node.right = dfs(inorder_ed+1, ed)

            return node

        return dfs(0, len(inorder))
