# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        ans = []
        ans.append(root.val)
        ans.extend(self.preorderTraversal(root.left))
        ans.extend(self.preorderTraversal(root.right))
        
        print(root.val, ans)
            
        return ans
        
