# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.inorder_trav = deque()
        self.inorder(self.root, self.inorder_trav)

    def inorder(self, root, inorder_trav):
        if not root: return
        self.inorder(root.left, inorder_trav)
        inorder_trav.append(root.val)
        self.inorder(root.right, inorder_trav)

    def next(self) -> int:
        return self.inorder_trav.popleft()

    def hasNext(self) -> bool:
        return len(self.inorder_trav)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
