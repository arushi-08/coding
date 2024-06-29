# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        # get all paths from root to leaves - X memory limit exceeded
        # pass freq of node values not node values to leaf.
        # in leaf check how many oddcounts - pseudo palindromic allows atmost 1 oddcount
        return self.helper(root, {})

    def helper(self, root, hmap):

        if not root:
            return 0
        
        hmap[root.val] = hmap.get(root.val, 0) + 1

        if not root.left and not root.right:
            oddcount = True
            ans = 1
            for k in hmap:
                if hmap[k] & 1 == 1:
                    if oddcount:
                        oddcount = False
                    else:
                        ans = 0
                        break
            
            hmap[root.val] -= 1
            if not hmap[root.val]:
                del hmap[root.val]
                
            return ans
        
        ans = self.helper(root.left, hmap) + self.helper(root.right, hmap)

        hmap[root.val] -= 1
        if not hmap[root.val]:
            del hmap[root.val]

        return ans


