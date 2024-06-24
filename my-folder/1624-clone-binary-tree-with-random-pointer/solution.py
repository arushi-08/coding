# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        if not root: return
        self.hmap = {}
        copyroot = self.dfs(root)

        self.map_random_pointers(root)

        return copyroot
    

    def dfs(self, root):
        if not root:
            return

        copyroot = NodeCopy(root.val)
        copyroot.left = self.dfs(root.left)
        copyroot.right = self.dfs(root.right)

        self.hmap[root] = copyroot
        return copyroot


    def map_random_pointers(self, root):

        if not root:
            return
        
        copyroot = self.hmap[root]
        if root.random:
            copyroot.random = self.hmap[root.random]
        
        self.map_random_pointers(root.left)
        self.map_random_pointers(root.right)
        
