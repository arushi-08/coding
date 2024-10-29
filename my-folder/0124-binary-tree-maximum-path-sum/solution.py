# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # at each root calculate max path sum from each child
        maxsum = set()
        self.helper(root, maxsum)
        return max(maxsum)
    
    def helper(self, root, maxsum):

        if not root: return -float('inf')

        left_child, right_child = -float('inf'), -float('inf')
        if root.left:
            left_child = self.helper(root.left, maxsum)
        if root.right:
            right_child = self.helper(root.right, maxsum)
        
        maxsum.add(
            max(root.val, left_child, right_child, 
            root.val+left_child, root.val+right_child, 
            root.val+left_child+right_child)
            )

        result = max(root.val, root.val+left_child, root.val+right_child)

        # print('maxsum', maxsum,'root', root.val, 'result', result)
        return result


        

