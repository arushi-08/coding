# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root : return ""
        
        tree_list = self.levelOrdertraversal(root)
        for i in range(len(tree_list)-1,-1,-1):
            if isinstance(tree_list[i],int):
                break
            del tree_list[i]
        
        ans = "["
        for i in range(len(tree_list)):
            if isinstance(tree_list[i], int):
                ans += str(tree_list[i]) + ","
            else:
                ans += "null,"
            if i == len(tree_list)-1:
                ans = ans[:-1]
        ans += "]"
        # print(ans) 
        return ans
    
    def levelOrdertraversal(self, root):
        
        queue = [root]
        ans = []
        while len(queue):
            curr = queue.pop(0)
            if not curr:
                ans.append(curr)
                continue
            
            ans.append(curr.val)
            
            if curr.left:
                queue.append(curr.left)
            else:
                queue.append(None)
            if curr.right:
                queue.append(curr.right)
            else:
                queue.append(None)
        
        return ans
        
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print("data", data)
        tree_list = data.strip("[").strip("]").split(",")
        if tree_list[0] in ["", "null"]:
            return None
        tree_list = [TreeNode(i) if i != "null" else None for i in tree_list ]
        # print("decode",tree_list)
        
        root = tree_list[0]
        i = 0
        idx = 0
        while i < len(tree_list):
            curr = tree_list[i]

            if not curr:
                i += 1
                continue
                
            # print("curr.val", curr.val, 2*idx+1, len(tree_list))
            if 2*idx+1 < len(tree_list):
                if tree_list[2*idx+1]:
                    curr.left = tree_list[2*idx+1]
                    # print(curr.val, "left", curr.left.val)
                
            if 2*idx+2 < len(tree_list):
                if tree_list[2*idx+2]:
                    curr.right = tree_list[2*idx+2]
                    # print(curr.val, "right", curr.right.val)
            
            i += 1
            idx += 1
            
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
