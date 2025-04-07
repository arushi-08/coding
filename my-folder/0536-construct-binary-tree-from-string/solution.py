# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        if not s:
            return

        def dfs(s, idx):
            if idx >= len(s):
                return None, idx
            
            left, right = None, None
            
            new_val = []
            while idx < len(s) and s[idx] not in ['(', ')']:
                new_val.append(s[idx])
                idx += 1
            if new_val:
                node = TreeNode(int(''.join(new_val)))
            else:
                return None, idx

            if node and idx < len(s) and s[idx] == '(':
                node.left, idx = dfs(s, idx+1)
                idx += 1
            
            if node and idx < len(s) and s[idx] == '(':
                node.right, idx = dfs(s, idx+1)
                idx += 1
                
            return node, idx


        root, _ = dfs(s, 0)
        return root

# 4
# 4.left = 2
# 2.left = 3
# 2.right = 1
# 1.left = null
# 1.right = null

# node TreeNode{val: 4, left: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 1, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: None}}
"""

        4
      /.  \
    2      3 
  / |
3   1



"""

