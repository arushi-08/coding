# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # looks like inorder
        # except put upper level nodes first

        path = self.inorder(root, 0, 0)
        # path = [[(3,0)], [(9,1), (4,2)]]
        # print("path", path)
        path = {k:v for k, v in sorted(path.items())}
        
        ans = []
        for k in path:
            temp = []
            for i in path[k]:
                temp.append(i[0])
            ans.append(temp)
        return ans
    
    def inorder(self, root, level, depth):

        if not root:
            return {}
        
        left = self.inorder(root.left, level-1, depth+1)
        if level in left:
            left[level].insert(0, (root.val, depth))
        else:
            left[level] = [(root.val, depth)]
        right = self.inorder(root.right, level+1, depth+1)
        
        for k in right:
            if k in left:
                left[k].extend(right[k])
                left[k].sort(key=lambda x: x[1])
            else:
                left[k] = right[k]
        return left
