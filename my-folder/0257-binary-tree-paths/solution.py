# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if not root: return [""]
        self.ans = []
        self.helper(root, "")
        # print("ans",self.ans)
        return self.ans
    
    def helper(self, root, state):
        
        if not root: return []
        
        if not root.left and not root.right:
            self.ans.append(state+str(root.val))
            
        if root.left:
            self.helper(root.left, state+str(root.val)+"->")
            
        if root.right:
            self.helper(root.right, state+str(root.val)+"->")
        
        # return root.val
        
