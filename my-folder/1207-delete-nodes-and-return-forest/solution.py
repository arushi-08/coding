# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        ans, childelete = self.helper(root, root, set(to_delete))
        return ans
    
    def helper(self, root, parent, to_delete):
        
        currdelete = False
        if not root:
            if parent:
                return [parent], currdelete
            return [], currdelete

        if not to_delete:
            return [parent], currdelete

        if root.val in to_delete:
            to_delete.remove(root.val)
            left, childelete = self.helper(root.left, root.left, to_delete)
            if childelete:
                root.left = None
            right, childelete = self.helper(root.right, root.right, to_delete)
            if childelete:
                root.right = None
            currdelete = True
        else:
            left, childelete = self.helper(root.left, parent, to_delete)
            if childelete:
                root.left = None
            right, childelete= self.helper(root.right, parent, to_delete)
            if childelete:
                root.right = None

            left.append(parent)
            
        left.extend(right)
        return list(set(left)), currdelete

        
