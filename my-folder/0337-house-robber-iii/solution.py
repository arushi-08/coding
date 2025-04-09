# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 1 entrance to area = root
        # besides root, each has 1 parent
        # don't use 2 adj nodes

        self.memo = {}
        return max(self.helper(root))
    
    def helper(self, root):
        if not root:
            return 0, 0
        
        if root in self.memo:
            return self.memo[root]
        # forced, as previous stolen
        free_left, forced_left = self.helper(root.left)
        free_right, forced_right = self.helper(root.right)
        forced_ans = max(free_left, forced_left) + max(free_right, forced_right)

        self.memo[root] = (forced_ans, free_left + free_right + root.val)
        return self.memo[root]
