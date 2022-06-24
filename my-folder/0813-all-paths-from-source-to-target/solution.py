class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
#         graph is adjacency list
        res = []
        curr = []
        chosen = [False]*len(graph)
        self.dfs(graph, 0, len(graph)-1, res, curr, chosen)
        return res
    
    def dfs(self, graph, source, target, res, curr, chosen):
        
        if source == target:
            curr.append(source)
            res.append(curr.copy())
            return
        
        # if not graph[source]: return
        
        curr.append(source)
        for i in range(len(graph[source])):
            if not chosen[graph[source][i]]:
                chosen[graph[source][i]] = True
                self.dfs(graph, graph[source][i], target, res, curr, chosen)
                chosen[graph[source][i]] = False
                curr.remove(graph[source][i])
                
        
        
