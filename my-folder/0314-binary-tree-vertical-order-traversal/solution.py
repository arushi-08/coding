# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # given root of bt, return vertical order traversal of its nodes values
        # (from top to bottom, column to column)

        # [9],[3,15],[20],[7]

        # left most, store height
        # [9], [3, 15], 20, 7

        # [left kids] + [current] + [right kids] 
        # merge parent with left / right kids
        # left kids = f(parent.left)
        # merge left kids' right kid with parent
        # [left kids] + [current] + [parent + right kids] 
        # 
        # parent.left, height - 1

        # parent.right, height + 1


        if not root:
            return []
        
        memo = defaultdict(list)

        def helper(node, height, level):
            if not node:
                return []

            memo[height].append((level, node.val))
            helper(node.left, height - 1, level + 1)
            helper(node.right, height + 1, level + 1)
            
        helper(root, 0, 0)
        
        res = []
        memo = sorted(memo.items(), key=lambda x:x[0])

        for k, v in memo:
            v_list = sorted(v, key=lambda x: x[0])
            temp_res = [i[-1] for i in v_list]
            res.append(temp_res)

        return res

