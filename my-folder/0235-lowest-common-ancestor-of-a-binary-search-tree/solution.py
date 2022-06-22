# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or not p or not q: return root
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
        
#         parent_p = []
#         self.dfs(parent_p, p, root)
#         parent_q = []
#         self.dfs(parent_q, q, root)
        
#         ancestor = None
    
#         for i,j in zip(parent_p, parent_q):
#             if i != j:
#                 break
#             ancestor = i
        
#         return ancestor
        
#     def dfs(self, parent, node, root):
        
#         if not root: return False
        
#         if root.val == node.val: 
#             # print("inside", [p1.val for p1 in parent])
#             parent.append(node)
#             return True
        
#         parent.append(root)
#         left = self.dfs(parent, node, root.left)
#         if left:
#             return True
#         right = self.dfs(parent, node, root.right)
#         if right: 
#             return True
#         parent.pop()
        
        
