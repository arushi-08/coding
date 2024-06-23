class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination: return True
        visited = set()
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        # print(graph)
        def dfs(node):
            if node == destination:
                return True
            
            for nnode in graph[node]:
                if nnode not in visited:
                    visited.add(nnode)
                    if dfs(nnode):
                        return True
            
            return False
            
        visited.add(source)
        for nextnode in graph[source]:
            if nextnode not in visited:
                visited.add(nextnode)
                if dfs(nextnode):
                    return True
        
        return False
