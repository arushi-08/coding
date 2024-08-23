# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        # check if total - current exists in hmap
        # do again - with psum
        # recursion - 
        # what will i store in hmap?
        # store total - current if it exists
        # 5 - store 8-5 = 3 {5:0}
        # 3 - 8-3 = 5 exists in hmap {5:1} -> ans += 1
        # 3 - 

        # still confused about what is stored in hmap
        # confused about the value in hmap - how to use it

        # 

        hmap = {0:1}
        psum = 0
        count = 0

        def dfs(node, targetSum, psum):
            nonlocal count
            if not node:
                return
            
            psum += node.val

            if psum - targetSum in hmap:
                # print('psum', psum, 'node',node.val, 'count', count, hmap)
                count += hmap[psum-targetSum]
                   
            hmap[psum] = hmap.get(psum, 0) + 1

            dfs(node.left, targetSum, psum)
            dfs(node.right, targetSum, psum)
            
            hmap[psum] -= 1
            if hmap[psum] == 0:
                del hmap[psum]
                
        dfs(root, targetSum, psum)

        return count

        
