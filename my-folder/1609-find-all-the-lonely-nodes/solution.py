# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        # find lonely node: only child of its parent node

        lonelynodes = []
        def dfs(node, islonely):
            if not node:
                return
            
            if islonely:
                lonelynodes.append(node.val)

            if node.left and node.right:
                dfs(node.left, False)
                dfs(node.right, False)
            elif node.left:
                dfs(node.left, True)
            else:
                dfs(node.right, True)
            
        
        dfs(root, False)
        return lonelynodes
