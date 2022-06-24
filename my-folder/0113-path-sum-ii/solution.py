# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root: return []
        curr, res = [], []
        chosen = []
        self.helper(root, curr, res, chosen, targetSum)
        ans = []
        for j in range(len(res)):
            temp_ans = []
            for i in range(len(res[j])):
                temp_ans.append(res[j][i].val)
            ans.append(temp_ans)
        return ans
    
    def helper(self, root, curr, res, chosen, target):
        if not root: return
        
        if root.val == target and not root.left and not root.right:
            chosen.append(root)
            res.append(chosen.copy())
            chosen.remove(root)
            return
        
        # if root.val != target and not root.left and not root.right:
        #     if root in chosen:
        #         curr.remove(root.val)
        #         chosen.remove(root)
        #     return
            
        
        if root not in chosen:
            # print(root.val)
            # curr.append(root.val)
            chosen.append(root)
            self.helper(root.left, curr, res, chosen, target-root.val)
            # chosen.remove(root)
            # curr.remove(root.val)
            self.helper(root.right, curr, res, chosen, target-root.val)
            chosen.remove(root)
            # curr.remove(root.val)
            # print(curr)
        


