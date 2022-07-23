# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        if not root: return ""
        
        start_path_from_root = self.findnode(root, startValue)
        dest_path_from_root = self.findnode(root, destValue)
        ans = ""
        while ((start_path_from_root.startswith("L") 
               and dest_path_from_root.startswith("L")
              )
              or (start_path_from_root.startswith("R") 
                 and dest_path_from_root.startswith("R")
                 )):
            start_path_from_root = start_path_from_root[1:]
            dest_path_from_root = dest_path_from_root[1:]
        
        start_path_from_root = list(start_path_from_root)
        start_path_from_root.reverse()
        for s in start_path_from_root[1:]:
            ans += "U"
        
        ans += dest_path_from_root[:-1]
        return ans
    
    def findnode(self, root, val):
        
        if not root: return ""
        
        if root.val == val: return "F"
        
        left = "L" + self.findnode(root.left, val)
        if "F" in left:
            return left
        right = "R" + self.findnode(root.right, val)
        if "F" in right:
            return right
        
        return "U"
        
        
        
        
