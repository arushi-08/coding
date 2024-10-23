# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # [5,[4,9],[1,10,null,7],[2,3,4,5,null,null,6,7]]
        
        queue = deque()
        queue.append(root)
        while queue:
            l = len(queue)
            temp = []
            for i in range(l):
                curr = queue.popleft()
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    temp.append(curr)
                else:
                    temp.append(TreeNode(0))
            
            if len(temp) <= 2:
                for i in range(len(temp)):
                    temp[i].val = 0
            else:
                og_temp = temp.copy()
                total_sum = sum(t.val for t in temp)
                
                for i in range(0, len(temp), 2):
                    deduct = temp[i].val + temp[i+1].val
                    temp[i].val = total_sum - deduct
                    temp[i+1].val = total_sum - deduct
                
        return root
