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
        ans = ''
        def preorder(root):
            nonlocal ans
            if not root:
                ans += 'null,'
                return 
            
            ans+=str(root.val) + ','
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ans[:-1]


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return 
        data = data.split(',')
        idx = 0
        def preorder():
            nonlocal idx, data

            if data[idx] == 'null':
                idx += 1
                return
            root = TreeNode(int(data[idx]))
            idx += 1
            root.left = preorder()
            root.right = preorder()
            return root

        return preorder()
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
