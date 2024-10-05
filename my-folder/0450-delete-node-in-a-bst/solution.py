# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # delete node
        # replace it with its child node

        # if root == key
        #   root's parent has to point to 1 of root's left child, or right child
        #       such that its still a bst

        #              10
        #           6
        #       3      8
        #     1. 4   7.  9

        #       replace root with leftmost element on right child
        #           or rightmost element on left child

        if not root:
            return None
        
        parent = TreeNode(0, left = root)
        self.helper(parent, root, key)
        return parent.left
    
    def helper(self, parent, root, key):
        
        if not root:
            return

        if root.val == key:
            new_node = self.rebalance_bst(root, root.left, root.right)
            if parent.left == root:
                parent.left = new_node
            else:
                parent.right = new_node
        else:
            self.helper(root, root.left, key)
            self.helper(root, root.right, key)
    

    def rebalance_bst(self, root, left, right):
        # make the key's left as parent's left or key's right as parent's right
        # make the other side of key's the child of this given key
        
        if not left and not right:
            return
        
        if left:
            left_right = left.right
            prev = left
            while left_right:
                prev = left_right
                left_right = left_right.right
            
            prev.right = right
            return left
        else:
            right_left = right.left
            prev = right
            while right_left:
                prev = right_left
                right_left = right_left.left

            prev.left = left
            return right


