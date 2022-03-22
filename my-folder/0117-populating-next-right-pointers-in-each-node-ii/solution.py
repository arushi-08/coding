"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root == None:
            return None
        
        queue = []
        queue.append(root)
        
        temp = None
        while(len(queue) > 0):
            
            for i in range(len(queue)):
                prev = temp
                temp = queue.pop(0)
                if i > 0:
                    prev.next = temp
                if temp.left != None:
                    queue.append(temp.left)
                    
                if temp.right != None:
                    queue.append(temp.right)

            # temp.next = None

        return root
        
            
        
        
            
