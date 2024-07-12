# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.addparent(root, None)
        visited = set()
        answer = []

        def dfs(root, k):
            if not root or root.val in visited:
                return
            visited.add(root.val)
            if k == 0:
                answer.append(root.val)
                
                return

            dfs(root.parent, k-1)
            dfs(root.left, k-1)
            dfs(root.right, k-1)

        dfs(target, k)
        return answer
            
    
    def addparent(self, root, parent):

        if not root:
            return
        
        root.parent = parent
        self.addparent(root.left, root)
        self.addparent(root.right, root)
