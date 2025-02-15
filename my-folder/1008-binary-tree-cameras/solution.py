# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        # given root
        # install cam on nodes where each cam at a node can monitor parent itself and children
        # return min num of cam to monitor all nodes

        # do dfs
        # can do dp

        # start from root
        # if node has child as leaf -> +1 (cam)
        # if added cam, set child, current and parent as set nodes
        # when coming back, see if child is set,
        # if it is set, then return unset
        # if child is not set, add cam, set child, set parent
        ans = self.helper(root, root)
        if root.val == 0:
            ans += 1
        return ans 

    def helper(self, node, root):
        if not node:
            return 0
        
        if not node.left and not node.right:
            return 0
        
        left_count = self.helper(node.left, root)
        right_count = self.helper(node.right, root)

        add_cam = False
        if node.left and node.left.val == 0:
            node.left.val = 1
            add_cam = True

        elif node.left and node.left.val == 1:
            node.val = 2
        
        if node.right and node.right.val == 0:
            node.right.val = 1
            add_cam = True
        
        elif node.right and node.right.val == 1:
            node.val = 2

        if not add_cam and node == root and root.val == 0:
            add_cam = True
        
        if add_cam:
            node.val = 1
            return left_count + right_count + 1
        else:
            return left_count + right_count



