# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        hmap = {}
        self.inorder(root, hmap)
        ans = []
        maxv = max(hmap.values())
        for k in hmap:
            if maxv == hmap[k]:
                ans.append(k)
        return ans

    def inorder(self, root, hmap):
        if not root:
            return
        
        self.inorder(root.left, hmap)
        hmap[root.val] = hmap.get(root.val, 0) + 1
        self.inorder(root.right, hmap)
