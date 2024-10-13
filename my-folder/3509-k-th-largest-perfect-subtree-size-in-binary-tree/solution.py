# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        
        # get all sizes of perfect subtree
        # sort in decreasing order 
        # return kth
        self.perfect_tree_size = []
        self.perfect_roots = set()

        self.helper(root)
        self.perfect_tree_size.sort(reverse=True)
        
        # print(self.perfect_tree_size)
        if k > len(self.perfect_tree_size):
            return -1
        return self.perfect_tree_size[k-1]
    
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        # print('root.val',root.val, left, right)
        if (not root.left and not root.right) or (root.left and root.right and root.left in self.perfect_roots and root.right in self.perfect_roots):
            if left == right:
                # print('enter',root.val, left+right+1)
                self.perfect_tree_size.append(left+right+1)
                self.perfect_roots.add(root)
        
        # print('root.val',root.val, left+right+1)
        return left+right+1
