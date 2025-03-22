class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        

        # 0 to n-1
        # given 2d integer array edges

        # return number of complete connected comps of graph

        # edge bet every 2 vertex
        # edge not going to any outside comp

        # if path from each node to every other node
        # and path from each node is to a node in the same component

        graph = defaultdict(list)
        # 0:[1,2] 1:[0,2] 2:[0,1]
        # all paths from 0, check they are connected 
        # if they are, add them to queue, mark 0 as visited
        # if not return False

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        ans = 0
        for i in range(n):
            if i not in visited:
                ans += self.get_count_complete_comps(i, graph, visited)
        
        return ans

    def get_count_complete_comps(self, node, graph, visited):

        queue = deque()
        queue.append(node)
        visited.add(node)

        while queue:
            currnode = queue.popleft()
            
            next_nodes = set(graph[currnode])
            for nextnode in graph[currnode]:
                if (len(set(graph[nextnode])) != len(next_nodes)) or (set(graph[nextnode]) - next_nodes != {currnode}):
                    return 0
                
                visited.add(nextnode)
        
        return 1

