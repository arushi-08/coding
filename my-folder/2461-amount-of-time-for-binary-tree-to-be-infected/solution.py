# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        # get to where start is from root, 
        # create path from root to start
        # every second, infect 1 node on this path & children of infected nodes
        # 

        path = self.get_path_to_start(root, start)
        time = self.infect_nodes_dfs(root, start, path[::-1])
        return time
    
    def get_path_to_start(self, root, start):

        if not root:
            return
        
        if root.val == start:
            return [root]
        
        path = self.get_path_to_start(root.left, start)
        if path:
            path.append(root)
            return path
        path = self.get_path_to_start(root.right, start)
        if path:
            path.append(root)
            return path

    def infect_nodes_dfs(self, root, start, path):

        queue = deque()
        visited = set()
        visited.add(path[-1])
        queue.append(path.pop())
        time = -1
        while queue:
            size = len(queue)
            time += 1
            if path:
                prev = path.pop()
            else:
                prev = None
            for i in range(size):
                curr = queue.popleft()

                if curr.left:
                    if curr.left not in visited:
                        queue.append(curr.left)
                        visited.add(curr.left)
                
                if curr.right:
                    if curr.right not in visited:
                        queue.append(curr.right)
                        visited.add(curr.right)
                
                if prev and prev not in visited:
                    visited.add(prev)
                    queue.append(prev)
        return time



