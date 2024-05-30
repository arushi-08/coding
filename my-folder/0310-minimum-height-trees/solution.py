from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1: return [0]
        # do topological sort

        adjlist = defaultdict(list)
        for i in range(len(edges)):
            adjlist[edges[i][0]].append(edges[i][1])
            adjlist[edges[i][1]].append(edges[i][0])
        
        queue = deque()

        for i in range(n):
            if len(adjlist[i])==1:
                queue.append(i)
        
        new_leaves = []
        
        while queue:
            if n <= 2:
                return list(queue)
            
            for i in range(len(queue)):
                curr = queue.popleft()
                n -= 1
                for node in adjlist[curr]:
                    adjlist[node].remove(curr)
                    if len(adjlist[node]) == 1:
                        queue.append(node)
                        new_leaves.append(node)
                    
        return queue




